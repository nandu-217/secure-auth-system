
from flask import current_app


import resend
import os

# EMAIL VERIFICATION
import smtplib
from flask import current_app

def send_verification_email(
    recipient,
    verification_link
):

    print("STEP 1")

    server = smtplib.SMTP(
        current_app.config["MAIL_SERVER"],
        current_app.config["MAIL_PORT"],
        timeout=10
    )

    print("STEP 2")

    server.starttls()

    print("STEP 3")

    server.login(
        current_app.config["MAIL_USERNAME"],
        current_app.config["MAIL_PASSWORD"]
    )

    print("STEP 4")

    server.quit()

    print("STEP 5")


# PASSWORD RESET
def send_reset_email(
    recipient,
    reset_link
):
    try:

        print(
            "Sending password reset email to:",
            recipient
        )

        msg = Message(
            subject="Password Reset Request",
            sender=current_app.config[
                "MAIL_DEFAULT_SENDER"
            ],
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

        print(
            "Sending OTP email to:",
            recipient
        )

        msg = Message(
            subject="Your Login OTP",
            sender=current_app.config[
                "MAIL_DEFAULT_SENDER"
            ],
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