import smtplib, ssl

def send_email(msg):
    host = "smtp.gmail.com"
    port = 465
    username = "correo.aplicaciones.ardit@gmail.com"
    password = "cyjw awse agna egda"
    receiver = "correo.aplicaciones.ardit@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port,
                           context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg)
