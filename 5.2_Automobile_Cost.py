# Auto Costs
# Write a program that ask the users to enter the montly cost for:
# loan payment, insurance, gas, and maintains.
def ask_for_car_expenses():
    loan_payment_monthly = float(input("How much is your monthly loan payment"))
    gas_payment_monthly = float(input("How much do you pay in gas every month"))
    insurance_payment_monthly = float(input("How much is your monthly insurance payment"))
    maintenance_payment_monthly = float(input("How much do you spend in maintenance a month"))
    return loan_payment_monthly, gas_payment_monthly, insurance_payment_monthly, maintenance_payment_monthly
def calculate_total_monthly_expenses ( payment1, payment2, payment3, payemnt4):
    total_monthly_expenses = payment1, payment2, payment3, payemnt4
    return total_monthly_expenses
def calculate_total_annual_cost( total_monthly_expenses ):
    total_annual_cost = total_monthly_expenses * 12
    return total_annual_cost
def print_details( total_monthly_cost, total_annual_cost ):
    print( "Your total monthly cost is" + format( total_monthly_cost ), ",.2f" + "/nYour total annual cost is" + format(total_annual_cost))

def main():
    loan_payment, insurance_payment, gas_payment, maintance_payment = ask_for_car_expenses()
    total_montly_Cost = calculate_total_monthly_expenses( loan_payment, insurance_payment, gas_payment, maintance_payment)
    total_annual_cost = calculate_total_annual_cost( total_montly_Cost )
main()
