from tkinter import *
from all_classes import *
def button_click():
    try:
        number=int(text1.get())
        root.destroy()
        #call some func
    except:
        label1['text']="input NUMBER"
        label1['font']="papirus 17"
grid=[[3,4],[4,4,6,4,4,6,8]]
pygame.init()
font = pygame.font.SysFont('Calibri', 25, True, False)
text=font.render("Save",True,black)
print(type(text.get_width()))
