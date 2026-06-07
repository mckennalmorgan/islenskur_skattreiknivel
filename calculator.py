# TODO:
# [x] Finish calculator
# [ ] Turn tax values into yaml config file
# [ ] Add in union fees, etc.

def calculate_monthly_tax(
    monthly_income,
    pension_credit=0.04,
    personal_credit=72492
):
    tax_brackets = [
        {"limit": 498122, "rate": 0.3149},
        {"limit": 1398450, "rate": 0.3799},
        {"limit": float('inf'), "rate": 0.4599}
    ]
    taxable_income = monthly_income * (1 - pension_credit)
    print("\n========================================== \n")
    print(f"Your taxable monthly income is {taxable_income:.2f}\n")
    print(f"Your personal tax credit is {personal_credit}")
    print("\n========================================== \n")


    tax = 0
    previous_bracket = 0 # since there is no limit below 31.49%
    for bracket in tax_brackets:
        taxable_amount = max(0, min(taxable_income, bracket["limit"]) - previous_bracket)
        tax += taxable_amount * bracket["rate"]
        print(f"Tax from {bracket['rate']*100:.2f}% bracket = {taxable_amount * bracket['rate']:.2f}\n")
        previous_bracket = bracket["limit"]
    tax = tax - personal_credit

    print("========================================== \n")
    print(f"Your total monthly tax is {tax:.2f}\n")
    print(f"Your net salary after taxes is {taxable_income - tax:.2f}\n")
    print(f"Your tax rate is {tax / taxable_income*100:.2f}%")
    print("\n========================================== \n")

if __name__ == "__main__":
    print("\n========================================== \n")
    monthly_income = float(input("What is your monthly income? "))
    
    calculate_monthly_tax(monthly_income)
