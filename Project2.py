import datetime, random


def getbirtthday(numberofbirthdays):
    birthdays = []

    for i in range(numberofbirthdays):
        startyear = datetime.date(2001, 1, 1)
        randomnumberofdays = datetime.timedelta(random.randint(0, 364))
        birthday = startyear + randomnumberofdays
        birthdays.append(birthday)
