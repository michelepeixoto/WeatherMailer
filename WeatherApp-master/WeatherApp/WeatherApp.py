import requests
import smtplib
import socket


class Contact:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        pass
    def __str__(self):
        return self.name+": "+self.email


class Schedule:
    def __init__(self, event, time):
        self.event = event
        self.time = time
        pass
    def __str__(self):
        return self.event+" - "+self.time


def get_weather():
    url = "http://api.openweathermap.org/data/2.5/weather?q=Bellevue,us&units=imperial&appid=96669274ea5b65e65143e45f1e5dd99f"
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    description = weather_json["weather"][0]["description"]
    max_temp = weather_json["main"]["temp_max"]
    min_temp = weather_json["main"]["temp_min"]
    weather = str(description).title() + " with a high of " + str(max_temp) + "F and a low of " + str(min_temp) + "F."
    return weather


def new_file(file_name, obj_type):
    file_items = []
    path = "C:\\Users\\mpeixoto\\Documents\\"+file_name
    try:
        file = open(path, "r")
    except FileNotFoundError:
        print(obj_type+" file not found.")
        pass
    for line in file:
        file_items.append(line.strip().split(": "))
        pass
    obj_list = []
    new_obj = ""
    for item in range(len(file_items)):
        new_obj = obj_type(file_items[item][0], file_items[item][1])
        obj_list.append(new_obj)
        pass
    return obj_list


def new_email(contact, schedule, weather):
    message = "Subject: Today's Weather and Activities\nGood Morning "+contact.name+",\nThe weather today is:\n"+weather+"\nToday's events are:\n"+schedule+"\nHave a great day!\n"
    return message


def server_connect():
    while True:
        try:
            print("Connecting to gmail server...")
            server = smtplib.SMTP_SSL("smtp.gmail.com", "587", local_hostname=None, timeout=5.0)
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


def send_email(from_email, to_email, message, server):    
    server.sendmail(from_email, to_email, message)
    print("Sent email to",to_email)
    pass


def main():
    server, from_email = server_connect()
    weather = get_weather()
    contacts_list = new_file("emails.txt", Contact)
    schedule_list = new_file("schedule.txt", Schedule)
    schedule = ""
    for event in schedule_list:
        schedule += str(event)+"\n"
        pass
    for contact in contacts_list:
        message = new_email(contact, schedule, weather)
        to_email = contact.email
        send_email(from_email, to_email, message, server)
        pass
    print("All emails sent!")
    server_disconnect(server)
    pass


main()
