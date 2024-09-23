import datetime

now = datetime.datetime.now()
print(type(now))
now_string = str(now)
print(now_string)
print(type(now.hour))
print(now.hour)

print(type(now.second))
print(now.second)

print(type(now))
print(now.second)
print(now.microsecond)

now_again = datetime.datetime.now()

print(f"{now == now_again=}")
print(now)
print(now_again)

print(f"{now.hour == now_again.hour=}")
print(now.date)
print(now.date())
print(f"{now.date == now_again.date=}")

print(now.now())

print(now.toordinal())

date = datetime.date(2024, 9, 23)
print(date)
print(f"{now.date() == date=}")

time = datetime.time(11, 8, 30)
print(time)
print(now.time() > time)

dt = datetime.datetime(2024,9,23,11,11,30)
print(now > dt)

formatering = now.strftime("%d/%m/%Y, %H:%M:%S")

print(type(formatering))
print(formatering)

print(f"{now - dt}")
print(f"{now - dt}")
print(f"{now + datetime.timedelta(days=1)}")

date_from_string = datetime.datetime.strptime(formatering, "%d/%m/%Y, %H:%M:%S")
print(type(date_from_string))
print(date_from_string)
print(date_from_string.microsecond)
print(date_from_string + datetime.timedelta(microseconds=100))
date_from_string = date_from_string + datetime.timedelta(microseconds=100)
print(date_from_string.microsecond)
