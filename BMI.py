def bmi_index(weight, height):
    index = round(weight/(height*height), 2)

    print(f"The body mass index is {index}.")

weight = 90 #in kilograms
height = 1.80 #in meters

bmi_index(weight, height)