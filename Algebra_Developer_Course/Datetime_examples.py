import datetime
import locale

today = datetime.datetime.today()
print(f"Today's date is {today}")

now = datetime.datetime.now()
print(f"Sadasnji trenutak je {now}")

day_in_week = datetime.date.weekday(today)
print(f"Today's day is {day_in_week + 1}")


if day_in_week == 0:
	print(f'Today is Monday, {day_in_week + 1}. day in the week.\n')
elif day_in_week == 1:
	print(f'Today is Tuesday, {day_in_week + 1}. day in the week.\n')
elif day_in_week == 2:
	print(f'Today is Wednesday, {day_in_week + 1}. day in the week.\n')
elif day_in_week == 3:
	print(f'Today is Thursday, {day_in_week + 1}. day in the week.\n')
elif day_in_week == 4:
	print(f'Today is Friday, {day_in_week + 1}. day in the week.\n')
elif day_in_week == 5:
	print(f'Today is Saturday, {day_in_week + 1}. day in the week.\n')
else:
	print(f'Today is Sunday, {day_in_week + 1}. day in the week.\n')



print("FORMATTING DATE AND TIME OUTPUT")

print("DAY OF THE WEEK '%A' -> full name, '%a' -> short name\n")
print(f"Full name of today's day is {today.strftime('%A')}")
# Full name of today's day is Thursday
print(f"Short name of today's day {today.strftime('%a')}\n")
# Short name of today's day Thu

locale.setlocale(locale.LC_TIME, "hr_HR")
print(f"HR - Full name of Today's day of the week is {today.strftime('%A')}")
# HR - Full name of Today's day of the week is èetvrtak
print(f"HR - Short name of today's day of the week is {today.strftime('%a')}")
# HR - Short name of today's day of the week is èet

print(f"Full name of today's day of the week is {today.strftime('%A')[:3]}\n")
# Full name of today's day of the week is èet

locale.setlocale(locale.LC_ALL, '')

print("YEAR '%Y' -> full name i '%y' -> short name\n")

print(f"4 characters - Year is {today.strftime('%Y')}. year")
# 4 characters - Year is 2023. year
print(f"2 characters - Year is {today.strftime('%y')}. year")
# 2 characters - Year is 23. year


print(f"Today's day is {today.strftime('%j')}. day in {today.strftime('%Y')}. year")
# Today's day is 061. day in 2023. year

print(f"This week is {today.strftime('%W')}. week in {today.strftime('%Y')}. year")
# This week is 09. week in 2023. year


print("MONTH '%B' -> full name, '&b' -> short name\n")

print(f"Full name of the month is {today.strftime('%B')}")
# Full name of the month is March

print(f"Short name of the month is {today.strftime('%b')}")
# Short name of the month is Mar

print(f"Current month of the year is {today.strftime('%m')}\n")
# Current month of the year is 03


# Calculating time difference
christmas = datetime.datetime.strptime("25.12.2023 18:50:00", "%d.%m.%Y %H:%M:%S")
time_till_christmas = christmas - now
print(f"Time left until Christmas: {time_till_christmas}") 
# Time left until Christmas: 297 days, 23:58:09.746472

today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(f"Yesterday's date: {yesterday.strftime('%d-%m-%Y %H:%M:%S')}")
# Yesterday's date: 01-03-2023 18:58:08
print(f"Tomorrow's date: {tomorrow.strftime('%d-%m-%Y %H:%M:%S')}")
# Tomorrow's date: 03-03-2023 18:58:08
