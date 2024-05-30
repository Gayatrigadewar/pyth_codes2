import datetime

def display_current_date_time():

    now = datetime.datetime.now()

    current_dat_time =  now.strftime("%Y-%m-%d %H:%M:%S")

    print("current date and time :")
    print(current_dat_time)

    display_current_date_time