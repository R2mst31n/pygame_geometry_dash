import pygame,random
from all_classes import *
from jumper import *
#definitions
def create_lvl(screen,leng,pos,typ):
    screen.fill(white)
    if(ite):
        for row in range(leng):
            grid.append([])
            for column in range(10):
                grid[row].append(0)
    for i in range (leng):
        for y in range(10):
            colour=green
            if(grid[i][y]==1):
                colour=black
            pygame.draw.rect(screen,colour,
                                 [size[0]//leng*i,(size[1]-40)//10*y+40,size[0]//leng,
                                  (size[1]-40)//10],2)
    pygame.draw.rect(screen,black,[0,0,30,30],2)
    pygame.draw.rect(screen,black,[50,0,50,30],2)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text=font.render("Save",True,black)
    screen.blit(text,[50,0])
    if(pos[0]>10 and pos[0]<30 and pos[1]>0 and pos[1]<30):
        #i choose black square
        figure=0
    elif(pos[0]>50 and pos[0]<100 and pos[1]>0 and pos[1]<30):
        save_lvl(grid)
        #grid=[]
        return 0
    elif(pos[1]>30):
        grid[pos[0]//(size[0]//leng)][pos[1]//((size[1]-40)//leng)-1]=1
    return 3
def save_lvl(grd):
    for column in range (len(grd)):
        for row in range (len(grd[column])):
            if grd[column][0]==0:
                del grd[column][0]
            else: break
    print(grd)
    lvl=Level()
    lvl.add_level(grd)
def draw_lvl(screen,num):
    grd=Level().get_level(num)
    count_x=len(grd)
    width=size[0]//count_x
    height=(size[1]-40)//10
    now_x=0
    for column in range(count_x):
        grd[column].reverse()
        for row in range(len(grd[column])):
            colour=black
            if grd[column][row]=='0':
                colour=white
            pygame.draw.rect(screen,colour,[now_x,size[1]-height*(row+1),
                                            width,height],2)
        now_x +=width
grid = []
ite = True
execu=0
pygame.init()
screen=pygame.display.set_mode(size)
pygame.display.set_caption("game's title")
screen.fill(white)
down_button=False
done=True
clock=pygame.time.Clock()
while done:
    down_button=False
    pos=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            down_button=True
    if(execu==0):
        #start main menu
        execu=Some_windows().menu(screen,pygame.mouse.get_pos(),down_button)
        pygame.mouse.get_pos()
    elif(execu==1):
        screen.fill(white)
        if (not res):
            res=0
        execu=play_game(screen,1)
        pygame.mouse.get_pos()
        #start game_levels
    elif(execu==2):
        #start Tkin_create_levels option
        some=Tkin()
        if(some.ret):
            execu=3
    elif(execu==3):
        #start create_levels option
        if(not down_button):
            pos=[0,0]
        execu=create_lvl(screen,some.some,pos,0)
        ite=False
    elif (execu==4):
        #start choose lvl menu
        execu,res=Some_windows().chose_lvl_menu(screen,pos,down_button)
    else:
        done=False
        #something go wrong
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
