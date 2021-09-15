import datetime as dt
from datetime import datetime

if __name__ == '__main__':
    current_time = datetime.now()
    print(current_time)
    print(type(current_time))

    current_time_utc = datetime.now(tz=dt.timezone.utc)
    print(current_time_utc)
    print(type(current_time_utc))

    current_time_without_ms = str(datetime.now()).split('.')[0]
    print(current_time_without_ms)
    print(str(datetime.now()).split('.'))

    # Retrieving separate data fields
    year = current_time.year
    month = current_time.month
    day = current_time.day

    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    print(f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}")

    # Working with timestamp
    example_time = "2021-09-10 16:54:23"
    datetime_object = datetime.strptime(example_time, '%Y-%m-%d %H:%M:%S')
    utc_time = datetime_object.replace(tzinfo=dt.timezone.utc)
    current_timestamp = datetime.timestamp(utc_time)
    print(current_timestamp)

    timestamp = 1631292863
    time_and_date_utc = datetime.fromtimestamp(timestamp, tz=dt.timezone.utc)
    print(time_and_date_utc)

    # Timedelta option
    start_time_and_date = "2021-08-10 17:45:00"
    date_time_obj = datetime.strptime(start_time_and_date, '%Y-%m-%d %H:%M:%S')

    # Calculating future date
    future_time_and_date = date_time_obj + dt.timedelta(days=2, hours=3, minutes=22)

    # Calculating past date
    past_time_and_date = date_time_obj + dt.timedelta(days=-4, hours=-2, minutes=-13)

    print(past_time_and_date)
    print(future_time_and_date)

    # get time difference between two dates
    date1 = "2021-08-06 15:32:00"
    date2 = "2021-08-12 21:07:00"

    date_time_obj_1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    date_time_obj_2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    diff = date_time_obj_2 - date_time_obj_1
    print(diff)

    # strptime examples
    date_example_1 = "2021-08-06 16:00:00"
    date_example_2 = "2021/08/06 16/00/00"
    date_example_3 = "06 August 21 - 16:00:00"
    date_example_4 = "06 August 21 - 4 PM"
    date_example_5 = "Aug 2021, 06 / 4 PM"
    date_time_obj_example_1 = datetime.strptime(date_example_1, '%Y-%m-%d %H:%M:%S')
    date_time_obj_example_2 = datetime.strptime(date_example_2, '%Y/%m/%d %H/%M/%S')
    date_time_obj_example_3 = datetime.strptime(date_example_3, '%d %B %y - %H:%M:%S')
    date_time_obj_example_4 = datetime.strptime(date_example_4, '%d %B %y - %I %p')
    date_time_obj_example_5 = datetime.strptime(date_example_5, '%b %Y, %d / %I %p')
    print(date_time_obj_example_1)
    print(date_time_obj_example_2)
    print(date_time_obj_example_3)
    print(date_time_obj_example_4)
    print(date_time_obj_example_5)

    # strftime examples
    example_time = "2021-08-06 16:00:00"
    datetime_object = datetime.strptime(example_time, '%Y-%m-%d %H:%M:%S')
    date_example_1 = datetime_object.strftime('%Y-%m-%d %H:%M:%S')
    date_example_2 = datetime_object.strftime('%Y/%m/%d %H/%M/%S')
    date_example_3 = datetime_object.strftime('%d %B %y - %H:%M:%S')
    date_example_4 = datetime_object.strftime('%d %B %y - %I %p')
    date_example_5 = datetime_object.strftime('%b %Y, %d / %I %p')
    print(date_example_1)
    print(date_example_2)
    print(date_example_3)
    print(date_example_4)
    print(date_example_5)
