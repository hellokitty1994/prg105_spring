# average rain fall
# write a program that uses nested loops
# to calculate the average rainfall over a period of years
# the program should fist ask the number of years
# the outer loop will iterate once for each year
# the inner loop will iterate 12 time once for each month
# each intention of the inner loop will ask the user for inches of rain fall for that month
# After all iteration, the program should display the number of months, the total of inches of rainfall
# and the average rainfall per month for the entire period.
the_total_number_of_months = 0
the_total_inches_of_rainfall = 0
number_of_years = int(input("Please enter the number of years: "))
for the_current_year in range(1, number_of_years + 1):
    for the_current_month in range(1, 13):
        the_montly_rainfall_in_inches = float(input("How many inches of rain fall for month "
                                                    + format(the_current_month, "d") + " year " + format(the_current_year, "d") + "; "))
        the_total_inches_of_rainfall = the_total_inches_of_rainfall + the_montly_rainfall_in_inches
        the_total_number_of_months += 1
average_rainfall = the_total_inches_of_rainfall / the_total_number_of_months
print("Number of months" + format(the_total_number_of_months, "d"), "total" + "inches of rainfall" +
      format(the_total_inches_of_rainfall, ".2f"), "average rainfall" + format(average_rainfall, ".2f"), sep="/n")
