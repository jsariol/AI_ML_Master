try:
    current_time = int(input("\nWhat is the current time? (0-23): "))
    if current_time < 0 or current_time > 23:
        print('Invalid value entered. Please enter a value between 0 and 23 for the current time.')
    else:
        wait_hours = int(input("How many hours to wait for the alarm?: "))
        if wait_hours < 0:
            print('Invalid value entered. Please enter a positive value for the amount of hours.')
        else:
            alarm_time = (current_time + wait_hours) % 24
            print("The alarm will go off at", alarm_time, "hours.")
except ValueError:
    print('Invalid value entered. Please enter whole numbers only.')
