def class_duration(acad_hours):
    acad_class_duration = 40
    break_duration = 15
    acad_hours_per_break = 3
    
    acad_duration = acad_hours*acad_class_duration + acad_hours//acad_hours_per_break*break_duration
    hours = acad_duration // 60
    minutes = acad_duration % 60

    return print(f"The total duration of the course is {hours:1} hours and {minutes:02} minutes.")

acad_hours = 64

class_duration(acad_hours)