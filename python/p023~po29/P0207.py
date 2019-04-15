import turtle

t = turtle.Turtle()
t.shape("turtle")

house_size = int(input("집의 크기는 얼마로 할까요?"))

t.fd(house_size)
t.right(90)
t.fd(house_size)
t.right(90)
t.fd(house_size)
t.right(90)
t.fd(house_size)

t.right(90)

t.fd(house_size)
t.left(120)
t.fd(house_size)
t.left(120)
t.fd(house_size)
t.left(120)
