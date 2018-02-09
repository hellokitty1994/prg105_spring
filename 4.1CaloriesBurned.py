# calories burned
# how many calories are going to be burned in 10, 15, 20, 25 and 30 minutes if 1 minute = 4.2 calories
calories_burned_per_minute = 4.2
for number_of_minutes in range(10, 31, 5):
    number_of_calories_burned = (number_of_minutes / 1) * calories_burned_per_minute
    print(" You will burn", number_of_calories_burned, "calories in", number_of_minutes, "minutes")
