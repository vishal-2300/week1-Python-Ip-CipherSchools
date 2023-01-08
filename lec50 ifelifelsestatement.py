#show ticket pricing
# 1to3(free)
# 4to10(150)
# 11to60(250)
# above 60(200)


age=int(input("enter age"))
if 0<age<=3:
    print("ticket is free")
elif 3<age<=10:
    print("ticket price:150")
elif 11<age<=60:
    print("ticket price:250")
else:
    print("ticket price:200")