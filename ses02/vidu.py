
age = int(input("Moi ban nhap nam sinh"))
tuoi = 2018 - age
gioitinh = input("Gioi tinh cua ban la")
if tuoi > 20:
    if gioitinh == "nam":
        print("Ban la nam thanh nien")
    else:
        print("Ban la nu thanh nien")
elif tuoi > 35:
    if gioitinh == "nam":
        print("Ban dang do tuoi trung nien, han che ruou bia")
    else:
        print("Chao quy ba :D")
else:
    print("Ban dang tre, hay lo hoc hanh")

