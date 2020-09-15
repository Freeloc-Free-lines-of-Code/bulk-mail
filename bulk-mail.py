from tkinter import *
import smtplib

# Functions
def send():
    try:
        conn = smtplib.SMTP("smtp.gmail.com", 587)
        conn.ehlo()
        conn.starttls()
        conn.login("email@gmail.com", "password")
        mail_from = "email@gmail.com"
        allmails = recipients.get()
        # split
        mail_to = allmails.split(",")
        print(mail_to)
        mail_content = """Subject: This is Automated mail. \n\n
        Testing!  testing!! Testing!
        From: Freeloc IT Solutions"""

        conn.sendmail(mail_from, mail_to, mail_content)
        conn.close()

        notif.config(fg="green", text="Mail sent SuccessFully !!")
    except Exception:
        notif.config(fg="red", text="Error Occured while sending mail.")


# Main screens
master = Tk()
master.title("SEND BULK MAIL - Freeloc It Solutions")
# labels
Label(master, text="SEND BULK MAIL", fg="blue", font=("Arial", 15)).grid(
    sticky=N, padx=220, row=0
)
Label(master, text="Enter Recipients separated by ,", font=("Arial", 12)).grid(
    sticky=N, pady=25, row=1
)
notif = Label(master, font=("Arial", 12))
notif.grid(sticky=N, pady=1, row=4)
# Vars
recipients = StringVar()
# Entry
Entry(master, width=70, textvariable=recipients).grid(sticky=N, row=2)
# Button
Button(master, width=20, text="SPAM !!", font=("Arial", 12), command=send).grid(
    sticky=N, pady=15, row=3
)
master.mainloop()
