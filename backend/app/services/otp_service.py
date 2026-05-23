import random

from app.extensions import db

from app.models.otp import OTP


def generate_otp(email):

    code = str(
        random.randint(
            100000,
            999999
        )
    )

    otp = OTP(
        email=email,
        otp_code=code
    )

    db.session.add(otp)

    db.session.commit()

    return code


def verify_otp(email, code):

    otp = OTP.query.filter_by(
        email=email,
        otp_code=code,
        is_used=False
    ).first()

    if not otp:
        return False

    otp.is_used = True

    db.session.commit()

    return True