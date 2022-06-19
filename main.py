import smtplib

# put here your own mail and recipient details
my_email = "your_email@gmail.com"
password = "your_password"
recipient_email = "recipient_mail"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()#starttls attribute will make sure that no one can read our data while we are sending
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=recipient_email,
                        msg="Subject: Hello\n\nThis is the body of my mail.")

