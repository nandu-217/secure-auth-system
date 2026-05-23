import secrets

from app.extensions import db, bcrypt

from app.models.user_model import User

def create_user(username, email, password):

    hashed_password = bcrypt.generate_password_hash(
        password
    ).decode("utf-8")

    verification_token = secrets.token_urlsafe(32)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password,
        verification_token=verification_token,
        is_verified=False
    )

    db.session.add(new_user)

    db.session.commit()

    return new_user