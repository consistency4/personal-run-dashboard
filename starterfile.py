###logging your run

from datetime import datetime

def get_time_input():
    time_input= input("please place your the amount of time it took you to complete your run here")
    return datetime.strptime(time_input, "%H:%M:%S").time()

def get_distance():
    return int(input("how many miles did your run"))

def get_date_input():
    date_input= input("what is todays date? (YYYY-MM-DD):")
    return datetime.strptime(date_input, "%Y-%m-%d").date()

def get_intensity():
    return input("what was the lever of intensity: easy, medium, hard?")

def get_notes():
    return input("please add any additional notes that you would like to mention for later")

def main():
    time = get_time_input()
    distance = get_distance()
    date = get_date_input()
    intensity = get_intensity()
    notes = get_notes()
    
    run_data= {"Time:": time, 
               "distance": distance, 
               "date": date, 
               "Intesity": intensity, 
               "Notes": notes}
    
    print("information",run_data)

main()

