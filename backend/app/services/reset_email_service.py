from flask_mail import Message

from app.extensions import mail


def send_reset_email(
    recipient,
    reset_link
):

    msg = Message(

        subject=
        "Password Reset Request",

        sender=
        "garanandini067@gmail.com",

        recipients=[
            recipient
        ]
    )

    msg.body = f"""
Hello,

A password reset request was made
for your account.

Click the link below:

{reset_link}

If you did not request this,
please ignore this email.

Regards,
Secure Auth Team
"""

    mail.send(msg)