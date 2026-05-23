from flask_mail import Message
from app.extensions import mail


# EMAIL VERIFICATION
def send_verification_email(
    recipient,
    verification_link
):

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


# PASSWORD RESET
def send_reset_email(
    recipient,
    reset_link
):

    msg = Message(
        subject="Password Reset Request",
        sender="garanandini067@gmail.com",
        recipients=[recipient]
    )

    msg.body = f"""
Hello,

Click below link to reset password:

{reset_link}

If you did not request this,
ignore this email.

Regards,
Secure Auth Team
"""

    mail.send(msg)


# OTP EMAIL
def send_otp_email(
    recipient,
    otp_code
):

    msg = Message(
        subject="Your Login OTP",
        sender="garanandini067@gmail.com",
        recipients=[recipient]
    )

    msg.body = f"""
Hello,

Your OTP is:

{otp_code}

This OTP can be used only once.

Regards,
Secure Auth Team
"""

    mail.send(msg)