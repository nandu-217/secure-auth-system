from flask import (
    Blueprint,
    request,
    jsonify
)

from app.services.otp_service import (
    generate_otp,
    verify_otp
)

from app.services.email_service import (
    send_otp_email
)

otp_bp = Blueprint(
    "otp_bp",
    __name__,
    url_prefix="/api/otp"
)


@otp_bp.route(
    "/send",
    methods=["POST"]
)
def send_otp():

    data = request.get_json()

    email = data.get("email")

    code = generate_otp(email)

    send_otp_email(
        email,
        code
    )

    return jsonify({
        "message": "OTP sent"
    })


@otp_bp.route(
    "/verify",
    methods=["POST"]
)
def verify():

    data = request.get_json()

    email = data.get("email")

    otp = data.get("otp")

    valid = verify_otp(
        email,
        otp
    )

    if not valid:
        return jsonify({
            "message": "Invalid OTP"
        }), 400

    return jsonify({
        "message": "OTP verified"
    })