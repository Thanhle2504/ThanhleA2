#9.2
can=["Canh","Tân", "Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỳ"]
chi=["Dậu","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]
nam = int(input("Nhap vao nam: "))
a= nam % 10
b= nam % 12
print("Nam" ,nam,"là năm:",can[a] + " " + chi[b])
