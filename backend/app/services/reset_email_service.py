import os
import resend

resend.api_key = os.getenv(
    "RESEND_API_KEY"
)

def send_reset_email(
    recipient,
    reset_link
):
    try:

        resend.Emails.send({

            "from":
            "onboarding@resend.dev",

            "to":
            recipient,

            "subject":
            "Password Reset",

            "html":
            f"""
            <h2>Password Reset</h2>

            <p>
                Click below to reset password:
            </p>

            <a href="{reset_link}">
                Reset Password
            </a>
            """
        })

        print(
            f"Password reset email sent to {recipient}"
        )

    except Exception as e:

        print(
            f"Password Reset Email Error: {str(e)}"
        )

        raise