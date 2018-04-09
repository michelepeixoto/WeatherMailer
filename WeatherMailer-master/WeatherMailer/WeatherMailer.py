import weather
import file
import gmail


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


def new_email(contact, schedule, forecast):
    message = "Subject: Today's Weather and Activities\nGood Morning "+contact.name+",\nThe weather today is:\n"+forecast+"\nToday's events are:\n"+schedule+"\nHave a great day!\n"
    return message


def send_email(from_email, to_email, message, server):
    server.sendmail(from_email, to_email, message)
    print("Sent email to",to_email)
    pass


def main():
    server, from_email = gmail.server_connect()
    forecast = weather.get_weather()
    contacts_list = file.new_file("emails.txt", Contact)
    schedule_list = file.new_file("schedule.txt", Schedule)
    schedule = ""
    for event in schedule_list:
        schedule += str(event)+"\n"
        pass
    for contact in contacts_list:
        message = new_email(contact, schedule, forecast)
        to_email = contact.email
        send_email(from_email, to_email, message, server)
        pass
    print("All emails sent!")
    gmail.server_disconnect(server)
    pass


main()
