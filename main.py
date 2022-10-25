
days_of_week = {
    'Sunday': 1,
    'Monday': 2,
    'Tuesday': 3,
    'Wednesday': 4,
    'Thursday': 5,
    'Friday': 6,
    'Saturday': 7
}


def add_time(start, duration, z=''):
    new_time = ''
    day_test = False
    if z:
        day_test = True
    z_list1 = start.split(':')                       # sets up ['3', '00 PM']
    hour_x = int(z_list1[0])
    z_list2 = z_list1[1].split()                 # sets up ['00', 'PM']
    min_x = int(z_list2[0])
    if z_list2[1] == 'PM':
        hour_x += 12

    z_list3 = duration.split(':')                      # sets up ['3', '10']
    hour_y = int(z_list3[0])
    min_y = int(z_list3[1])

    sum_hours = hour_x + hour_y
    sum_mins = min_x + min_y

    if sum_mins > 59:
        sum_mins -= 60
        sum_hours += 1

    next_day_test = sum_hours // 24
    blurb = ''
    if next_day_test >= 2:
        blurb = '(' + str(next_day_test) + ' days later)'
    elif next_day_test >= 1:
        blurb = '(next day)'

    new_day = ''

    # Day of Week test
    if day_test:
        value_of_day = days_of_week[z.title()]
        if next_day_test < 1:
            new_day = ', ' + z.title()
        else:
            new_day_sum = (value_of_day + next_day_test) % 7
            if new_day_sum == 0:                # special case for saturday 7 % 7 = 0
                new_day = ', Saturday'
            else:
                new_day = [k for k, v in days_of_week.items() if v == new_day_sum][0]
                new_day = ', ' + new_day

    ampm = 'Z'
    result_list = []

    if sum_hours % 24 == 0:
        sum_hours = 12
        ampm = 'AM'
    elif sum_hours % 24 < 12:
        sum_hours = sum_hours % 24
        ampm = 'AM'
    elif sum_hours % 24 == 12:
        ampm = 'PM'
    else:
        sum_hours = sum_hours % 24 - 12
        ampm = 'PM'

    # clean up the mess
    if len(str(sum_mins)) < 2:
        sum_mins_str = '0' + str(sum_mins)
    else:
        sum_mins_str = str(sum_mins)
    new_time = str(sum_hours) + ':' + sum_mins_str + ' ' + str(ampm) + new_day + ' ' + blurb
    return new_time


print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
print(add_time("3:30 PM", "2:12"))
print(add_time("11:55 AM", "3:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:40 AM", "0:25"))
print(add_time("2:59 AM", "24:00"))
print( add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("5:01 AM", "0:00"))
print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("11:59 PM", "24:05", "Wednesday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
