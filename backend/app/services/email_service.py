from flask_mail import Message
from app.extensions import mail


# EMAIL VERIFICATION
def send_verification_email(
    recipient,
    verification_link
):
    try:

        msg = Message(
            subject="Verify Your Email",
            sender="garanandini067@gmail.com",
            recipients=[recipient]
        )

        msg.body = f"""
Hello,

Thank you for registering.

Please click the link below to verify your account:

{verification_link}

Regards,
Secure Auth Team
"""

        mail.send(msg)

        print(
            f"Verification email sent to {recipient}"
        )

    except Exception as e:

        print(
            f"Verification Email Error: {str(e)}"
        )

        raise


# PASSWORD RESET
def send_reset_email(
    recipient,
    reset_link
):
    try:

        msg = Message(
            subject="Password Reset Request",
            sender="garanandini067@gmail.com",
            recipients=[recipient]
        )

        msg.body = f"""
Hello,

A password reset request was received.

Click the link below to reset your password:

{reset_link}

If you did not request this change,
please ignore this email.

Regards,
Secure Auth Team
"""

        mail.send(msg)

        print(
            f"Password reset email sent to {recipient}"
        )

    except Exception as e:

        print(
            f"Password Reset Email Error: {str(e)}"
        )

        raise


# OTP EMAIL
def send_otp_email(
    recipient,
    otp_code
):
    try:

        msg = Message(
            subject="Your Login OTP",
            sender="garanandini067@gmail.com",
            recipients=[recipient]
        )

        msg.body = f"""
Hello,

Your One-Time Password (OTP) is:

{otp_code}

This OTP can only be used once.

If you did not request this OTP,
please ignore this email.

Regards,
Secure Auth Team
"""

        mail.send(msg)

        print(
            f"OTP email sent to {recipient}"
        )

    except Exception as e:

        print(
            f"OTP Email Error: {str(e)}"
        )

        raise