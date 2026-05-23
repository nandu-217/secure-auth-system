from app.extensions import db


class OTP(db.Model):

    __tablename__ = "otps"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    email = db.Column(
        db.String(120),
        nullable=False
    )

    otp_code = db.Column(
        db.String(6),
        nullable=False
    )

    is_used = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )