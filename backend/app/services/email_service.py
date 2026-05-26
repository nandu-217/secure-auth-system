import os
import resend

resend.api_key = os.getenv(
    "RESEND_API_KEY"
)


# EMAIL VERIFICATION
def send_verification_email(
    recipient,
    verification_link
):
    try:

        resend.Emails.send({

            "from":
            "onboarding@resend.dev",

            "to":
            recipient,

            "subject":
            "Verify Your Email",

            "html":
            f"""
            <h2>Email Verification</h2>

            <p>
            Thank you for registering.
            </p>

            <p>
                <a href="{verification_link}">
                    Verify Email
                </a>
            </p>
            """
        })

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

        resend.Emails.send({

            "from":
            "onboarding@resend.dev",

            "to":
            recipient,

            "subject":
            "Password Reset Request",

            "html":
            f"""
            <h2>Password Reset</h2>

            <p>
                <a href="{reset_link}">
                    Reset Password
                </a>
            </p>
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


# OTP EMAIL
def send_otp_email(
    recipient,
    otp_code
):
    try:

        resend.Emails.send({

            "from":
            "onboarding@resend.dev",

            "to":
            recipient,

            "subject":
            "Your Login OTP",

            "html":
            f"""
            <h2>Your OTP</h2>

            <h1>{otp_code}</h1>
            """
        })

        print(
            f"OTP email sent to {recipient}"
        )

    except Exception as e:

        print(
            f"OTP Email Error: {str(e)}"
        )

        raise