import json
import datetime as dt
import smtplib


def send_email(class_soon):
    with open("mail_template.txt") as file:
        content = file.read()
        content = content.replace("[Class]", class_soon)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="shaurya01singh06@gmail.com", password="testing@123")
            connection.sendmail(from_addr="shaurya01singh06@gmail.com",
                                to_addrs="shaurya01singh06@gmail.com",
                                msg=f"Subject: Class about to start!!!\n\n{content}")


def check_time():
    now = dt.datetime.now()
    current_time = now.strftime("%H:%M").split(":")
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        for entry in data[now.strftime("%A")]:
            class_times = entry[1].split(":")
            if (class_times[0] == current_time[0]) and (int(class_times[1]) - int(current_time[1]) == 5):
                send_email(entry[0])
