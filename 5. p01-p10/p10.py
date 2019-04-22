import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","도형을 입력하시오:")
if s == "사각형":
    s = turtle.textinput("","가로:")
    w = int(s)
    s = turtle.textinput("","세로:")
    h = int(s)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)

if s == "원":
    s = turtle.textinput("","반지름의 길이를 입력하시오:")
    w = int(s)
    t.circle(w)
    
if s == "삼각형":      #이 알고리즘은 정삼각형만 만들 수 있다.
    s = turtle.textinput("","한변의 길이를 입력하시오:")
    w = int(s)
for i in range(3):
    t.forward(w)
    t.left(180//1.5)
