# Pennies for pay
# Write a program that calculate the amount of money a person would earn over a period of time if his/ her salary
# is one penny day one, two pennies the second day and continues to double each day.
# this program should ask user for the number of days.
# Display a table showing what the salary was for each day and then show the total pay at the end of the period.
# the amount should be display in dollar not pennies.
number_of_days_worked = int(input("please enter how many day you have worked"))
pay_per_day = .01
total_number_of_pennies = 0
print()
print("day\tsalary\n-----\t-----")
for current_day_of_work in range(number_of_days_worked):
    pennies_for_day = 2**current_day_of_work
    total_number_of_pennies += pennies_for_day
    print(current_day_of_work + 1, "\t", pennies_for_day)
total_pay_ = total_number_of_pennies * .01
print("\ntotal pay is ", total_pay_)
