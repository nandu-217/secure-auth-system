from flask import Flask
from flask_cors import CORS

from app.config import Config

from app.extensions import (
    db,
    bcrypt,
    jwt,
    mail,
    migrate
)

from app.models.user_model import User
from app.models.refresh_token import RefreshToken
from app.models.password_reset import PasswordReset

from app.routes.auth_routes import auth_bp
from app.routes.reset_routes import reset_bp

from app.middleware.token_blacklist import blacklisted_tokens


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)
    
    CORS(app)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    migrate.init_app(
    app,
    db
)

    app.register_blueprint(auth_bp)
    app.register_blueprint(reset_bp)
    app.register_blueprint(otp_bp)

    @jwt.token_in_blocklist_loader
    def check_token(jwt_header, jwt_payload):
        return jwt_payload["jti"] in blacklisted_tokens

    return app
from app.routes.otp_routes import otp_bp
from app.models.otp import OTP
from app.routes.reset_routes import (
    reset_bp
)