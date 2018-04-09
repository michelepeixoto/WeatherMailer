from time import strftime, sleep
from datetime import datetime, timedelta
import re

# A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.


class Clock:

    def __init__(self):
        pass

    def time():
        return strftime("%H:%M:%S")


def display(clock):
    print(clock.time())
    pass


def alarm(clock, alert_time):
    print("Alarm set for " + alert_time)
    while True:
        sleep(1)
        if clock.time() == alert_time:
            print("WAKE UP\n")
            break
        else:
            continue
    pass


def timer(clock, in_time):
    curr_date = datetime.now()
    alert_time = curr_date + timedelta(seconds=in_time)
    alert_time = alert_time.strftime("%H:%M:%S")
    while True:
        sleep(1)
        if clock.time() == alert_time:
            print("TIME'S UP\n")
            break
        else:
            curr_date = datetime.now()
            curr_time = curr_date.strftime("%H:%M:%S")
            print(curr_time)
            continue
    pass


def main():
    clock = Clock
    display(clock)
    while True:
        choice = input("Enter 1 to set an alarm, 2 to set a timer or 3 to quit:\n")
        if choice == "1":
            alert_time = input("Set alarm time as HH:MM:SS\n")
            if re.match("^\d\d:\d\d:\d\d$", alert_time):
                alarm(clock, alert_time)
                pass
            else:
                print("Invalid input.")
                main()
                pass
            break
        elif choice == "2":
            in_time = input("Set timer to go off in how many seconds (999 max)?\n")
            if re.match("^\d{1,3}$", in_time):
                timer(clock, int(in_time))
                pass
            else:
                print("Invalid input.")
                main()
                pass
            break
        elif choice == "3":
            print("Goodbye.")
            quit()
        else:
            print("Invalid input, try again.")
            continue
    main()
    pass


main()
