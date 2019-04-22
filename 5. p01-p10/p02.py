from datetime import datetime

d =datetime.now()
t = int(input("출생년도는?"))
age = int(d.year) - int(t)

if age >= 15 :
    print("올해", age ,"살이군요. 영화관람이 가능합니다.")
else:
    print("올해", age ,"살이군요. 영화를 관람할 수 없습니다.")
