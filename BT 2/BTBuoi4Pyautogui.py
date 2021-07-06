import pyautogui

x,y,x1,y1=[636, 212,1012, 547]
x2=x1-x
y2=y1-y

def ve(start_x,start_y,moveto_x,moveto_y):
    pyautogui.mouseDown(start_x,start_y) #Bắt đầu di chuyển chuột tại start_x,start_y
    pyautogui.moveTo(moveto_x,moveto_y) #Di chuyển đến vị trí moveto_x,moveto_y
    pyautogui.mouseUp()

if __name__ == "__main__":
    ve(685, 235,685, 509)
    ve(685, 235, 802, 239)
    ve(802, 239, 802, 342)
    ve(802, 342, 802, 342)
    ve(802, 342, 685, 342)
    ve(837, 235, 923, 342)
    ve(986, 235, 844, 514)

    pyautogui.screenshot('someButton.png', region=(x, y, x2, y2)) #x,y góc trên cùng bên trái, x2,y2 góc dưới cùng bên phải (region nội dung cần chụp, bên trong x,y,x1,y1)





