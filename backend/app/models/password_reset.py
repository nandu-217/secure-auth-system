from app.extensions import db


class PasswordReset(db.Model):

    __tablename__ = "password_resets"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    reset_token = db.Column(
        db.String(255),
        unique=True,
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

    expires_at = db.Column(
        db.DateTime,
        nullable=True
    )

    def __repr__(self):

        return (
            f"<PasswordReset {self.user_id}>"
        )