T=int(input("請輸入任教班級數量:"))
student=[]
for i in range(T):
    student.append(int(input("請輸入班級學生數量:")))
print("需購買電腦數量為:",max(student))
