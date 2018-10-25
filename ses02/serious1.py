ccao = float(input("Moi ban nhap vao chieu cao :"))
cnang = float(input("Moi ban nhap vao can nang :"))
bmi = cnang / (ccao*ccao)
if bmi < 16 :
    print("chi so bmi: ", bmi, "Severely underweight")
elif bmi <= 18.5:
    print("chi so bmi: ", bmi,"Underweight")
elif bmi <= 25:
    print("chi so bmi: ", bmi,"Normal")
elif bmi <= 30:
    print("chi so bmi: ", bmi,"Overweight")
else:
    print("chi so bmi: ", bmi,"Obese")