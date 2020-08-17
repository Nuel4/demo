has_high_income =True
has_good_credit = False
if has_high_income and has_good_credit :
    print("you are eligible for lone")

elif has_high_income or has_good_credit:
    print("your application is under consideration")
    print("please check back next week")

else:
    print("you are not qualified for lone here")


has_good_record = True
has_criminal_record = False
if has_good_record and not has_criminal_record:
    print("you are qualified")

else:
    print("you are not wanted here")