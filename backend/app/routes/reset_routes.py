import secrets

from flask import (
    Blueprint,
    request,
    jsonify
)

from app.extensions import (
    db,
    bcrypt
)

from app.models.user_model import User

from app.models.password_reset import (
    PasswordReset
)

from app.services.reset_email_service import (
    send_reset_email
)
from datetime import datetime, timedelta

expires_at = (
    datetime.utcnow() +
    timedelta(minutes=30)
)

reset_bp = Blueprint(

    "reset_bp",

    __name__,

    url_prefix="/api/auth"
)


# FORGOT PASSWORD

@reset_bp.route(
    "/forgot-password",
    methods=["POST"]
)
def forgot_password():

    data = request.get_json()

    email = data.get(
        "email"
    )

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:

        return jsonify({
            "message":
            "Email not found"
        }), 404

    token = secrets.token_urlsafe(
        32
    )
    expires_at = (
    datetime.utcnow() +
    timedelta(minutes=30)
)
    reset_record = PasswordReset(

        user_id=user.id,

        reset_token=token,
        expires_at=expires_at
        
    )

    db.session.add(
        reset_record
    )

    db.session.commit()

    reset_link = (

        "http://127.0.0.1:5500/"
        f"reset-password.html?token={token}"
    )

    send_reset_email(
        email,
        reset_link
    )

    return jsonify({

        "message":
        "Password reset link sent"

    }), 200


# RESET PASSWORD

@reset_bp.route(
    "/reset-password/<token>",
    methods=["POST"]
)
def reset_password(token):

    record = PasswordReset.query.filter_by(

        reset_token=token,

        is_used=False

    ).first()

    if record.expires_at < datetime.utcnow():

         return jsonify({

        "message":
        "Reset link has expired"

    }), 400

    data = request.get_json()

    password = data.get(
        "password"
    )

    if not password:

        return jsonify({

            "message":
            "Password is required"

        }), 400

    if len(password) < 6:

        return jsonify({

            "message":
            "Password must be at least 6 characters"

        }), 400

    user = User.query.get(
        record.user_id
    )

    if not user:

        return jsonify({

            "message":
            "User not found"

        }), 404

    hashed_password = (
        bcrypt.generate_password_hash(
            password
        ).decode("utf-8")
    )

    user.password = (
        hashed_password
    )

    record.is_used = True

    db.session.commit()

    return jsonify({

        "message":
        "Password updated successfully"

    }), 200