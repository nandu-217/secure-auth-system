import secrets
from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

from app.models.user_model import User

from app.extensions import (
    db,
    bcrypt
)

from app.services.auth_service import (
    create_user
)

from app.services.email_service import (
    send_verification_email
)

from app.utils.validators import (
    validate_email,
    validate_password
)

from app.middleware.token_blacklist import (
    blacklisted_tokens
)

auth_bp = Blueprint(
    "auth_bp",
    __name__,
    url_prefix="/api/auth"
)


# REGISTER
@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:

        return jsonify({
            "message":
            "All fields are required"
        }), 400

    if not validate_email(email):

        return jsonify({
            "message":
            "Invalid email"
        }), 400

    if not validate_password(password):

        return jsonify({
            "message":
            "Password must be at least 6 characters"
        }), 400

    existing_user = User.query.filter(
        (User.email == email) |
        (User.username == username)
    ).first()

    email_exists = User.query.filter_by(email=email).first()

    if email_exists:
      return jsonify({
        "message": "Email already exists"
    }), 409

    username_exists = User.query.filter_by(username=username).first()

    if username_exists:
      return jsonify({
        "message": "Username already exists"
    }), 409
    user = create_user(
        username,
        email,
        password
    )

    verification_link = (
       f"https://secure-auth-system-bp36.onrender.com/api/auth/"
       f"verify-email/{user.verification_token}"
)

    try:

        send_verification_email(
            email,
            verification_link
        )

    except Exception as e:

        print(
            "EMAIL ERROR:",
            str(e)
        )

        return jsonify({
            "message":
            "User created but verification email could not be sent"
        }), 500

    return jsonify({
        "message":
        "Registration successful. Please check your email and verify your account."
    }), 201


# VERIFY EMAIL
@auth_bp.route(
    "/verify-email/<token>",
    methods=["GET"]
)
def verify_email(token):

    user = User.query.filter_by(
        verification_token=token
    ).first()

    if not user:

        return """
        <html>
        <body style="
        font-family:Arial;
        text-align:center;
        margin-top:100px;">
        <h1>❌ Invalid or Expired Verification Link</h1>
        <p>Please request a new verification email.</p>
        </body>
        </html>
        """

    user.is_verified = True
    user.verification_token = None

    db.session.commit()

    return """
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>
Verification Successful
</title>

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{

height:100vh;

display:flex;

justify-content:center;

align-items:center;

background:
linear-gradient(
135deg,
#0f172a,
#1e40af,
#06b6d4
);

font-family:
Arial,
sans-serif;
}

.card{

padding:50px;

border-radius:25px;

background:
rgba(
255,
255,
255,
0.15
);

backdrop-filter:
blur(20px);

text-align:center;

color:white;

box-shadow:
0 10px 40px rgba(
0,
0,
0,
0.3
);

animation:
zoomIn .8s ease;
}

.icon{

font-size:90px;

margin-bottom:20px;

animation:
pulse 1.5s infinite;
}

h1{

margin-bottom:15px;
}

p{

margin-top:10px;

font-size:18px;
}

.loader{

width:50px;

height:50px;

margin:25px auto;

border-radius:50%;

border:4px solid rgba(
255,
255,
255,
0.3
);

border-top:4px solid white;

animation:
spin 1s linear infinite;
}

@keyframes spin{

to{
transform:rotate(360deg);
}
}

@keyframes pulse{

0%{
transform:scale(1);
}

50%{
transform:scale(1.08);
}

100%{
transform:scale(1);
}
}

@keyframes zoomIn{

from{

opacity:0;

transform:
scale(.5);
}

to{

opacity:1;

transform:
scale(1);
}
}

</style>

</head>

<body>

<div class="card">

<div class="icon">
✅
</div>

<h1>
Email Verification Successful
</h1>

<p>
Registration completed successfully.
</p>

<p>
Your account is now verified.
</p>



</div>

<script>
<div style="margin-top:25px;">

<button
onclick="window.location.href='https://gilded-licorice-bd735c.netlify.app/index.html'"
style="
padding:12px 24px;
border:none;
border-radius:10px;
cursor:pointer;
background:white;
color:#1e40af;
font-weight:bold;
font-size:16px;
">

Go To Login

</button>

</div>

</script>

</body>

</html>
"""

# RESEND VERIFICATION EMAIL
@auth_bp.route(
    "/resend-verification",
    methods=["POST"]
)
def resend_verification():

    data = request.get_json()

    email = data.get(
        "email"
    )

    if not email:

        return jsonify({
            "message":
            "Email is required"
        }), 400

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:

        return jsonify({
            "message":
            "User not found"
        }), 404

    if user.is_verified:

        return jsonify({
            "message":
            "Account already verified"
        }), 400

    token = secrets.token_urlsafe(
        32
    )

    user.verification_token = token

    db.session.commit()

    verification_link = (
    f"https://secure-auth-system-bp36.onrender.com/api/auth/verify-email/{token}"
)

    try:

        send_verification_email(
            email,
            verification_link
        )

    except Exception as e:

        print(
            "EMAIL ERROR:",
            str(e)
        )

        return jsonify({
            "message":
            "Unable to send verification email"
        }), 500

    return jsonify({
        "message":
        "Verification email sent successfully"
    }), 200



# LOGIN
@auth_bp.route(
    "/login",
    methods=["POST"]
)
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:

        return jsonify({
            "message":
            "Invalid email"
        }), 401

    if not user.is_verified:

        return jsonify({
            "message":
            "Please verify your email first"
        }), 403

    valid_password = (
        bcrypt.check_password_hash(
            user.password,
            password
        )
    )

    if not valid_password:

        return jsonify({
            "message":
            "Invalid password"
        }), 401

    access_token = (
        create_access_token(
            identity=str(user.id)
        )
    )

    refresh_token = (
        create_refresh_token(
            identity=str(user.id)
        )
    )

    return jsonify({

        "message":
        "Login successful",

        "access_token":
        access_token,

        "refresh_token":
        refresh_token,

        "username":
        user.username

    }), 200


# REFRESH TOKEN
@auth_bp.route(
    "/refresh",
    methods=["POST"]
)
@jwt_required(refresh=True)
def refresh():

    user_id = get_jwt_identity()

    access_token = (
        create_access_token(
            identity=user_id
        )
    )

    return jsonify({
        "access_token":
        access_token
    }), 200


# DASHBOARD
@auth_bp.route(
    "/dashboard",
    methods=["GET"]
)
@jwt_required()
def dashboard():

    current_user = get_jwt_identity()

    user = User.query.get(
        int(current_user)
    )

    return jsonify({

        "message":
        "Dashboard loaded",

        "username":
        user.username,

        "email":
        user.email,

        "role":
        user.role,

        "verified":
        user.is_verified

    }), 200


# LOGOUT
@auth_bp.route(
    "/logout",
    methods=["POST"]
)
@jwt_required()
def logout():

    jti = get_jwt()["jti"]

    blacklisted_tokens.add(
        jti
    )

    return jsonify({
        "message":
        "Logout successful"
    }), 200