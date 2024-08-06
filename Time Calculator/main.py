days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
periods = ['AM', 'PM']


def add_time(start, duration, day=''):
    #extract hours, minutes and period from initial date
    start_hours = int(start.split(':')[0])
    start_minutes = int(start.partition(' ')[0].partition(':')[2])
    start_period = start.split(' ')[1]
    start_day = day
    #extract hours, minutes and period from duration
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.partition(' ')[0].partition(':')[2])
    #assign values to the new time's hour, minutes, period and weekday
    new_time_hours = start_hours + duration_hours
    new_time_minutes = start_minutes + duration_minutes
    new_time_period = start_period
    new_time_day = start_day

    #check if the sum of minutes is >= 60, if so, add an hour and reduce minutes to the 0-60 range
    if new_time_minutes >= 60:
        new_time_minutes %= 60
        new_time_hours += 1
    #check if the sum of minutes is a digit, if so, concatenate a zero
    if new_time_minutes < 10:
        new_time_minutes = '0' + str(new_time_minutes)

    #calculate passed days
    days_passed = new_time_hours // 24

    #if the starting period is PM and the sum of hours is greater than 12, increment days passed by one
    if start_period == periods[1] and new_time_hours > 12:
        days_passed += 1

    #calculate passed periods
    periods_passed = new_time_hours // 12

    #correctly reassign new period based on periods passed
    if periods_passed % 2 != 0:
        new_time_period = periods[0] if start_period == periods[1] else periods[1]

    #reduce new time hours to the range of 0-12
    new_time_hours = new_time_hours % 12
    if new_time_hours == 0:
        new_time_hours = 12

    #build the new time string
    new_time = str(new_time_hours) + ":" + str(new_time_minutes) + ' ' + new_time_period

    #check if the optional parameter is present, calculate the new time day based on days passed
    if new_time_day.lower() in days:
        new_time_day = days[(days.index(start_day.lower()) + days_passed) % 7].lower().capitalize()
        new_time += ', ' + new_time_day

    #build a proper string
    if days_passed == 1:
        new_time += ' (next day)'
    elif days_passed > 1:
        new_time += f' ({days_passed} days later)'
    return new_time


#some tests
print(add_time('3:30 PM', '2:12'))
print(add_time('8:16 PM', '466:02'))
print(add_time('11:30 PM', '2:12'))
print(add_time('2:59 AM', '24:00'))
