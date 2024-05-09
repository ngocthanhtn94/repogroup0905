# Bài 5: Viết chương trình nhập vào một số bất kỳ và in ra giá trị tuyệt đối của số đó
Value = float(input("Nhập vào 1 số bất kỳ: "))
Tri_tuyet_doi = abs(Value)
print(f"Giá trị tuyệt đối của {Value} là {Tri_tuyet_doi}")

# Bài 8: Viết chương trình nhập vào số năm và cho biết năm đó là năm nhuận hay năm không nhuận.
year = int(input("Nhập vào một năm: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "là năm nhuận.")
else:
    print(year, "không phải là năm nhuận.")

# Bài 11: Nhập vào chiều cao (cm) và cân nặng (kg), tính số BMI và xét kết quả theo dữ liệu
height_cm = float(input("Nhập chiều cao (cm): "))
weight_kg = float(input("Nhập cân nặng (kg): "))

# Chuyển đổi chiều cao từ cm sang m
height_m = height_cm / 100

# Tính chỉ số BMI
bmi = weight_kg / (height_m ** 2)

# Xét chỉ số BMI và in kết quả
if bmi < 16:
    print("BMI =", bmi, "- Gầy cấp độ III")
elif 16 <= bmi < 17:
    print("BMI =", bmi, "- Gầy cấp độ II")
elif 17 <= bmi < 18.5:
    print("BMI =", bmi, "- Gầy cấp độ I")
elif 18.5 <= bmi < 25:
    print("BMI =", bmi, "- Bình thường")
elif 25 <= bmi < 30:
    print("BMI =", bmi, "- Thừa cân")
elif 30 <= bmi < 35:
    print("BMI =", bmi, "- Béo phì cấp độ I")
elif 35 <= bmi < 40:
    print("BMI =", bmi, "- Béo phì cấp độ II")
else:
    print("BMI =", bmi, "- Béo phì cấp độ III")
