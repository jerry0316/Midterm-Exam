x = int(input("請輸入x軸座標為:"))
y = int(input("請輸入y軸座標為:"))
if x == 0 and y ==0:
    print("該點位於原點")
elif x > 0 and y >0 :
    print ("該點位於第一象限，離原點距離為根號",x**2 + y**2)
elif x<0 and y > 0:
    print("該點位於第二象限，離原點距離為根號",x**2 + y**2)
elif x<0 and y <0 :
    print("該點位於第三象限，離原點距離為根號",x**2 + y**2)
elif x>0 and y<0 :
    print("該點位於第四象限，離原點距離為根號",x**2 + y**2)
elif x==0 and y>0:
    print("該點位於上半平面x軸上，離原點距離為根號",x**2 + y**2)
elif x==0 and y<0:
    print("該點位於下半平面x軸上，離原點距離為根號",x**2 + y**2)
elif y==0 and x>0:
    print("該點位於右半平面Y軸上，離原點距離為根號",x**2 + y**2)
elif y==0 and x<0:
    print("該點位於左半平面Y軸上，離原點距離為根號",x**2 + y**2)
