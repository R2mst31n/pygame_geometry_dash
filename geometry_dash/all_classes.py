import pygame,random
from tkinter import *
from all_values import *
class Character(pygame.sprite.Sprite):
    width=0
    height=0
    mask=pygame.mask.Mask((0,0))
    def __init__(self,width,height,x,y,filename,color_key=black):
        super().__init__()
        self.image=pygame.image.load(filename).convert()
        self.image.set_colorkey(color_key)
        self.image=pygame.transform.scale(self.image,[width,height])
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.mask=pygame.mask.from_surface(self.image)
        print("bottom of figure",self.rect.bottom)
        print("top of figure",self.rect.top)
        print("x coordin is: ",self.rect.x)
        print("y coordin is: ",self.rect.y)
    def move(self,direction,par2,v):
        if direction=="x":
            if par2=="fd":
                self.rect.x +=v
            else: self.rect.x -=v
        else:
            if par2=="fd": self.rect.y +=v
            else: self.rect.y -=v
class Figure(pygame.sprite.Sprite):
    width=0
    height=0
    typ=""
    mask=pygame.mask.Mask((0,0))
    def __init__(self,width,height,x,y):
        super().__init__()
        typ="rect"
        #create surface rect and fill it black color
        self.image=pygame.Surface([width,height])
        self.image.fill(black)
        self.image.set_colorkey(white)
        #set coordinates of rect
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.mask=pygame.mask.from_surface(self.image)
    def convert_to_triangle(self,mode):
        typ=""
        self.image.fill(white)
        pygame.draw.polygon(self.image,black,mode)
        self.image.set_colorkey(white)
        self.mask=pygame.mask.from_surface(self.image)
    def move(self,direction,par2,v):
        if direction=="x":
            if par2=="fd":
                self.rect.x +=v
            else: self.rect.x -=v
        else:
            if par2=="fd": self.rect.y +=v
            else: self.rect.y -=v

    def reset_figure(self):
        self.rect.x=size[0]+100
class Level():
    columns=[]
    def get_level(self,level):
        file=open("level.1.txt",'r')
        line=file.read().split('\n')[level-1]
        columns=line.split('@')
        for i in range(len(columns)):
            columns[i]=list(columns[i])
        file.close()
        return columns
    def add_level(self,column):
        file=open("level.1.txt",'a')
        file.write("\n")
        for i in range (len(column)):
            for x in range(len(column[i])):
                column[i][x]=str(column[i][x])
        for i in range(len(column)):
            column[i]="".join(column[i])
        file.write("@".join(column))
    def get_number(self):
        return len(open("level.1.txt",'r').readlines())
class Tkin():
    rect=False
    def button_click(self,event=None):
        try:
            self.some=int(self.text.get())
            self.ret=True
            self.root.destroy()
        except:
            self.label["text"]="input NUMBER"
            self.label["font"]="papirus 17"

    def __init__(self):
        self.root=Tk()
        self.root.geometry("300x100")
        self.root.title("input lenght of you track")
        self.label=Label(self.root,text="please, input lenght(number)",
                     font="arial 14")
        self.root.bind("<Return>",lambda event: self.button_click())
        self.label.pack()
        self.text=Entry(self.root,font="arial 14")
        self.text.pack()
        button1=Button(self.root,text="ok",font="arial 15",
                       command=lambda: Tkin.button_click(self))
        button1.pack()
        self.root.mainloop()
        
class Some_windows():
    def menu(self,screen,pos,pressed):
        """create main menu (screen-environment;pos-list of mouses x and y;pressed-True if user pressed"""
        mx,my=pos
        screen.fill(white)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text1=font.render("Select level",True,black)
        text2=font.render("Create Level",True,black)
        text3=font.render("Exit",True,black)
        width1,width2,width3=text1.get_width(),text2.get_width(),text3.get_width()
        x_rect1,x_rect2,x_rect3=(size[0]-width1-30)//2,(size[0]-width2-30)//2,(size[0]-width3-30)//2
        pygame.draw.rect(screen,green,[x_rect1,150,width1+30,30])
        pygame.draw.rect(screen,green,[x_rect2,250,width2+30,30])
        pygame.draw.rect(screen,green,[x_rect3,350,width3+30,30])
        screen.blit(text1,[x_rect1+15,155])
        screen.blit(text2,[x_rect2+15,255])
        screen.blit(text3,[x_rect3+15,355])
        if mx>x_rect1 and mx<x_rect1+width1+30 and my>150 and my<180:
            pygame.draw.rect(screen,black,[x_rect1-3,148,width1+34,32],4)
            if pressed:
                #pressed in "Select Level" button
                return 4
        if mx>x_rect2 and mx<x_rect2+width2+30 and my>250 and my<280:
            pygame.draw.rect(screen,black,[x_rect2-3,248,width2+34,32],4)
            if pressed:
                #pressed in "Create Level" button
                return 2
        if mx>x_rect3 and mx<x_rect3+width3+30 and my>350 and my<380:
            pygame.draw.rect(screen,black,[x_rect3-3,348,width3+34,32],4)
            if pressed:
                #Exit
                return 10
        return 0
    def chose_lvl_menu(self,screen,pos,pressed):
        """create levels chosig menu(screen-env;pos-mouse x and y positions;pressed=True if user pressed in screen"""
        mx,my=pos
        screen.fill(white)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text=font.render("Select level",True,black)
        textpos=text.get_rect()
        textpos.centerx=size[0]//2
        screen.blit(text,textpos)
        for line in range(Level().get_number()):
            text1=font.render("{} Level".format(line+1),True,red)
            text1=pygame.transform.scale(text1,[100,text1.get_height()])
            textpos1=text.get_rect()
            textpos1.centerx=size[0]//2
            textpos1.centery=60+40*line
            screen.blit(text1,textpos1)
        if pressed:
            if my>47:
                return 1,(my-47)//(14+26)
        return 4,0
class widgets():
    """add some widgets in active screen"""
    def __init__(self,x,y,width,height,color=green):
        self.x,self.y,self.width,self.height,self.color=x,y,width,height,color
    def button(self,screen):
        """simple button(only rect)"""
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.width,self.height])
    def check(self,screen,pos,pressed,weight=4,color=black):
        """check if mouse location inside button and if clicked return True"""
        mx,my=pos
        if mx>self.x and mx<self.x+self.width and my>self.y and my<self.y+self.height:
            pygame.draw.rect(screen,color,[self.x-weight//2,self.y-weight//2,
                                           self.width+weight,self.height+weight],weight)
            if pressed:
                return True
        return False
    def add_txt(self,screen,text,margin=8,color=black):
        """add text into button"""
        font=pygame.font.SysFont("Calibri",25,True,False)
        txt=font.render(text,True,color)
        txtpos=txt.get_rect()
        txtpos.center=(self.x+self.width//2,self.y+self.height//2)
        txt=pygame.transform.scale(txt,(self.width-margin,self.height-margin))
        screen.blit(txt,txtpos)
    def delet(self):
        """delete widget(don't work)"""
        self.x,self.y=-3456765430,-4567890






