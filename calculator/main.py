
def main():
    print(" This is a monthly payment loan calculator ")
    print("")

    principal = float(input("Enter loan amount"))
    apr = float(input("Enter Annual Interest rate:"))
    years = int(input("Enter amount of years: "))

    monthly_interest_rate = apr / 1200
    number_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))

    print("Monthly payment for this loan is : %.2f" % monthly_payment)


main()
