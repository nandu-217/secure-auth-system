import smtplib

server = smtplib.SMTP(
    "smtp.gmail.com",
    587,
    timeout=10
)

server.starttls()

server.login(
    "garanandini067@gmail.com",
    "dphconlqkyjjuqpo"
)

print("LOGIN SUCCESS")

server.quit()