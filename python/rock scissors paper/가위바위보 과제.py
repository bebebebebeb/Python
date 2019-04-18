import turtle          #터틀 그래픽 모듈을 불러온다
import random    #난수 모듈을 불러온다


screen = turtle.Screen()
image1 = "rock.gif"     #이미지들을 불러온다
image2 = "scissors.gif"
image3 = "paper.gif"
screen.addshape(image1)
screen.addshape(image2)
screen.addshape(image3)


t1 = turtle.Turtle() #첫 번째 거북이를 생성한다
t1.speed(0) #t1의 속도를 최대로 하여 빠르게 결과가 나타나게 한다
t1.penup() #거북이가 지나가는 자리에 펜이 그어지지 않는다
user = turtle.textinput("","무엇을 내시겠습니까:")  #사용자에게서 변수를 받는다.
if user == "가위":
    t1.shape(image2) #사용자가 변수를 "가위"라 하면 image2가 선택된다.

elif user == "바위":
    t1.shape(image1) #사용자가 변수를 "바위"라 하면 image1이 선택된다.
   
elif user == "보" : 
    t1.shape(image3) #사용자가 변수를 "보"라 하면 image3이 선택된다.
    
t1.stamp() #거북이의 위치에 선택한 이미지가  띄어진다. 
t1.write("당신의 선택",False,"left", ("",15))   #사용자가 선택한 이미지 위에 "당신의 선택" 이라는 글씨가 써진다.


t2 = turtle.Turtle()   #두 번째 거북이를 생성한다.
t2.penup()  #거북이가 지나가는 자리에 펜이 그어지지 않는다
t2.speed(0) #t2의 속도를 최대로 하여 빠르게 결과가 나타나게 한다
computer = random.choice([image1, image2, image3]) #컴퓨터는 랜덤으로 이미지를 선택한다
computer = image2

if computer == image1 :
    t2.shape(image1)  #컴퓨터가 랜덤으로 뽑은 image1이 선택된다
    
elif computer == image2 :
    t2.shape(image2)   #컴퓨터가 랜덤으로 뽑은 image2가 선택된다
    
else :
    t2.shape(image3) #컴퓨터가 랜덤으로 뽑은 image3이 선택된다

t2.setpos(300,0)  #t2는 (300,0)의 위치로 간다.
t2.stamp() #컴퓨터가 랜덤으로 선택한 이미지가  (300,0)의 자리에 띄어진다
t2.write("컴퓨터의 선택",False,"left", ("",15)) #컴퓨터가 랜덤으로 선택한 이미지 위에 "컴퓨터의 선택" 이라는 글씨가 써진다. 


t3 =turtle.Turtle()  #세 번째 거북이를 생성한다.
t3.speed(0) #t3의 속도를 최대로 하여 빠르게 결과가 나타나게 한다
t3.penup()   #거북이가 지나가는 자리에 펜이 그어지지 않는다
t3.setpos(300,200)     #(300,200)의 위치에서 승부의 결과가 써진다.

if user == "가위" and computer == image1 or user == "바위" and computer == image3 or user == "보" and computer == image2:
    t3.write("컴퓨터가 이겼습니다.",False,"left", ("",15)) #컴퓨터가 이길시 "컴퓨터가 이겼습니다."라는 글이 써진다.
    
elif user == "가위" and computer == image3 or user == "바위" and computer == image2 or user == "보" and computer == image1:
    t3.write("당신이 이겼습니다.",False,"left", ("",15)) #사용자가 이길시 "당신이 이겼습니다."라는 글이 써진다.

    
else:
    t3.write("비겼습니다.",False,"left", ("",15)) #사용자와 컴퓨터가 비길시 "비겼습니다."라는 글이 써진다.
