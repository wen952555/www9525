import pyotp

def generate_otp_secret() -> str:
    """
    生成用户的 TOTP 秘钥
    """
    return pyotp.random_base32()

def verify_otp(secret: str, otp: str) -> bool:
    """
    验证用户输入的 OTP
    """
    totp = pyotp.TOTP(secret)
    return totp.verify(otp)