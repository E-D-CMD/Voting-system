import smtplib
from email.message import EmailMessage

print("""
#############################################################
##  Hello voter                                            ##
##  Please follow the easy steps to sign up as a new voter  ##
##  Enter (1) to sign up                                   ##
##  Enter (2) to cancel                                    ##
#############################################################
""")

# MENU INPUT
try:
    usr_option = int(input("Enter here: "))
except ValueError:
    print("Invalid input. Numbers only.")
    exit()


def send_confirmation(receiver_email):
    sender_email = "onlineVoter@gmail.com"
    sender_password = "YOUR_APP_PASSWORD"  # use app password

    msg = EmailMessage()
    msg.set_content(
        "Thank you for registering as a voter.\n"
        "You have successfully registered."
    )
    msg["Subject"] = "Voter Registration Confirmation"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print("Confirmation email sent!")


def sign_up():
    print("Let's proceed")

    name = input("Please enter your name: ")

    # AGE LOOP
    while True:
        try:
            age = int(input("Enter your age: "))
            if age >= 18:
                break
            print("You must be at least 18 years old.")
        except ValueError:
            print("Please enter a valid number.")

    # EMAIL LOOP
    while True:
        email = input("Enter your email address: ")
        if "@" in email and "." in email:
            break
        print("Invalid email. Please try again.")

    district = input("Enter district: ")

    # NRC LOOP
    while True:
        nrc_no = input("Enter your NRC number: ")
        if len(nrc_no) == 8:
            break
        print("NRC number must contain exactly 8 characters.")

    print(f"\n{name}, you have successfully registered as a voter!")
    print(f"Confirmation will be sent to {email}")

    send_confirmation(email)


if usr_option == 1:
    sign_up()
elif usr_option == 2:
    print("Thank you for visiting.")
else:
    print("Invalid option.")
