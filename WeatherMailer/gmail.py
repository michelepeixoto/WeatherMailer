import smtplib
import socket


def server_connect():
    while True:
        try:
            print("Connecting to gmail server...")
            server = smtplib.SMTP_SSL("smtp.gmail.com", "587", local_hostname=None, timeout=10.0)
            break
        except socket.timeout:
            choice = input("Connection failed. Try again? y/n\n")
            if choice == "y":
                continue
            else:
                quit()
    server.starttls()
    while True:
        try:
            from_email = input("Send emails from:\n")
            password = input("Enter your password:\n")
            server.login(from_email, password)
            break
        except smtplib.SMTPAuthenticationError:
            print("Authentication Error, try again.")
    print("Connection successful.")
    return server, from_email


def server_disconnect(server):
    server.quit()
    print("Disconnected.")
    pass
