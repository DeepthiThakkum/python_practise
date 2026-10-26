high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")

high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")

high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")

high_income = False
good_credit = True
student = True

if not student:
    print("Eligible")
else:
    print("Not Eligible")

high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
