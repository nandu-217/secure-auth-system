from app.extensions import db

class RefreshToken(db.Model):

    __tablename__ = "refresh_tokens"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    token = db.Column(
        db.Text,
        nullable=False
    )

    revoked = db.Column(
        db.Boolean,
        default=False
    )

    created_at = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )