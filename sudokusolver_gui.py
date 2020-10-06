import pygame as pg 
import time 

width = 400
height = 400

pg.init() 
fps = 30
CLOCK = pg.time.Clock() 
screen = pg.display.set_mode((width,height), 0, 32) 

pg.font.init()
myfont = pg.font.SysFont('Comic Sans MS', 40)
one = myfont.render('1', False, (0, 0, 0))
two = myfont.render('2', False, (0, 0, 0))
three = myfont.render('3', False, (0, 0, 0))
four = myfont.render('4', False, (0, 0, 0))
five = myfont.render('5', False, (0, 0, 0))
six = myfont.render('6', False, (0, 0, 0))
seven = myfont.render('7', False, (0, 0, 0))
eight = myfont.render('8', False, (0, 0, 0))
nine = myfont.render('9', False, (0, 0, 0))
r_one = myfont.render('1', False, (255, 0, 0))
r_two = myfont.render('2', False, (255, 0, 0))
r_three = myfont.render('3', False, (255, 0, 0))
r_four = myfont.render('4', False, (255, 0, 0))
r_five = myfont.render('5', False, (255, 0, 0))
r_six = myfont.render('6', False, (255, 0, 0))
r_seven = myfont.render('7', False, (255, 0, 0))
r_eight = myfont.render('8', False, (255, 0, 0))
r_nine = myfont.render('9', False, (255, 0, 0))

col = 0
row = 0

original=[[0,0,0,0,0,0,0,0,0,],
          [0,0,0,0,0,0,0,0,0,],
          [0,0,0,0,0,0,0,0,0,],
          [0,0,0,0,0,0,0,0,0,],
          [0,0,0,0,0,0,0,0,0,],
          [0,0,0,0,0,0,0,0,0,],
          [0,0,0,0,0,0,0,0,0,],
          [0,0,0,0,0,0,0,0,0,],
          [0,0,0,0,0,0,0,0,0,]]

solution = original
empty = []


def printsud(sud):
  for i in range(9):
    print(sud[i][0], sud[i][1], sud[i][2],'|',
          sud[i][3], sud[i][4], sud[i][5],'|',
          sud[i][6], sud[i][7], sud[i][8],)
    if(i == 2 or i == 5): print('---------------------')

def checkrow(sud, row, num): #True is correct
  occurance = 0
  for i in range(9):
    if(sud[row][i] == num): occurance = occurance + 1
  return occurance == 0

def checkcolumn(sud, col, num): #True is correct
  occurance = 0
  for i in range(9):
    if(sud[i][col] == num): occurance = occurance + 1
  return occurance == 0

def checksquare(sud, row, col, num): #True is correct
  occurance = 0
  rowstart = 0
  if(row <= 2): rowstart = 0
  if(row >=3 and row <= 5): rowstart = 3
  if(row >= 6): rowstart = 6
  colstart = 0
  if(col <= 2): colstart = 0
  if(col >=3 and col <= 5): colstart = 3
  if(col >= 6): colstart = 6

  for i in range(rowstart, rowstart+3,1):
    for j in range(colstart, colstart+3,1):
      if(sud[i][j] == num): occurance = occurance + 1
  return occurance == 0

def solvesquare(row, col, num):
  run = True
  while (run == True and (num != None and num < 9)):
    num += 1
    
    cr = checkrow(solution, row, num)
    cc = checkcolumn(solution, col, num)
    cs = checksquare(solution, row, col, num)
    if(cr == True and cc == True and cs == True): 
      return num
      run = False
    if(cr == False and cc == False and cs == False and num == 9):
      num = 10
      return num
      run = False

def resetafter(j):
  for k in range(j+1, len(empty), 1):
    empty[k][0] = 0

def solve():
    for i in range(9):
            for j in range(9):
                if(original[i][j] == 0): empty.append([0,i,j])
    i = 0
    while i < len(empty):
        resetafter(i)
        wrong = 0
        for x in range(len(empty)): 
            if(empty[x][0] == 0): wrong = wrong + 1
            solution[empty[x][1]][empty[x][2]] = empty[x][0]
        if wrong == 0: i = 100
        empty[i][0] = solvesquare(empty[i][1], empty[i][2],empty[i][0])
        if empty[i][0] == 10 or empty[i][0] == None:
            i = i - 2
        i = i + 1
    for x in range(len(empty)): solution[empty[x][1]][empty[x][2]] = empty[x][0]

def show_ans():
    for i in range(9):
        for j in range(9):
            posx = 40*(j+1) - 10
            posy = 40*(i+1) - 30

            if solution[i][j] == 1: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_one, (posx,posy)) 
            elif solution[i][j] == 2: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_two, (posx,posy)) 
            elif solution[i][j] == 3: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_three, (posx,posy)) 
            elif solution[i][j] == 4: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_four, (posx,posy)) 
            elif solution[i][j] == 5: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_five, (posx,posy)) 
            elif solution[i][j] == 6: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_six, (posx,posy)) 
            elif solution[i][j] == 7: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_seven, (posx,posy)) 
            elif solution[i][j] == 8: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_eight, (posx,posy)) 
            elif solution[i][j] == 9: 
                pg.draw.rect(screen, (255,255,255), (40*(j+1)-18,40*(i+1)-18,36,36))
                screen.blit(r_nine, (posx,posy)) 

def game_initiating_window(): 
    # updating the display 
    pg.display.update() 
    time.sleep(3)                    
    screen.fill((255,255,255))

    # drawing lines 
    for i in range(10):
        if i == 0 or i == 9 or i == 3 or i == 6: pg.draw.line(screen, 0, (20+i*40,20),(20+i*40,height-20), 3) 
        else: pg.draw.line(screen, 0, (20+i*40,20),(20+i*40,height-20), 1) 
    for i in range(10):
        if i == 0 or i == 9 or i == 3 or i == 6: pg.draw.line(screen, 0, (20,20+i*40),(width-20,20+i*40), 3) 
        else: pg.draw.line(screen, 0, (20,20+i*40),(width-20,20+i*40), 1) 

game_initiating_window() 

def user_click(): 
    x, y = pg.mouse.get_pos() 
    global row
    global col
    global original
    if original[row-1][col-1] == 0: pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))

    if(x <((width-40)/9+20)): 
        col = 1
    elif(x <((width-40)/9*2+20)): 
        col = 2
    elif(x <((width-40)/9*3+20)): 
        col = 3
    elif(x <((width-40)/9*4+20)): 
        col = 4
    elif(x <((width-40)/9*5+20)): 
        col = 5
    elif(x <((width-40)/9*6+20)): 
        col = 6
    elif(x <((width-40)/9*7+20)): 
        col = 7
    elif(x <((width-40)/9*8+20)): 
        col = 8
    elif(x <((width-40)/9*9+20)): 
        col = 9

    if(y <((height-40)/9+20)): 
        row = 1
    elif(y <((height-40)/9*2+20)): 
        row = 2
    elif(y <((height-40)/9*3+20)): 
        row = 3
    elif(y <((height-40)/9*4+20)): 
        row = 4
    elif(y <((height-40)/9*5+20)): 
        row = 5
    elif(y <((height-40)/9*6+20)): 
        row = 6
    elif(y <((height-40)/9*7+20)): 
        row = 7
    elif(y <((height-40)/9*8+20)): 
        row = 8
    elif(y <((height-40)/9*9+20)): 
        row = 9

    pg.draw.rect(screen, (0,255,0), (40*col-18,40*row-18,36,36))
    
def key_pressed():
    posx = 40*col - 10
    posy = 40*row - 30
    global original
    global empty
    if event.key == pg.K_1: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(one, (posx,posy)) 
        original[row-1][col-1] = 1
    if event.key == pg.K_2: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(two, (posx,posy)) 
        original[row-1][col-1] = 2
    if event.key == pg.K_3: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(three, (posx,posy)) 
        original[row-1][col-1] = 3
    if event.key == pg.K_4: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(four, (posx,posy)) 
        original[row-1][col-1] = 4
    if event.key == pg.K_5: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(five, (posx,posy)) 
        original[row-1][col-1] = 5
    if event.key == pg.K_6: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(six, (posx,posy)) 
        original[row-1][col-1] = 6
    if event.key == pg.K_7: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(seven, (posx,posy)) 
        original[row-1][col-1] = 7
    if event.key == pg.K_8: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(eight, (posx,posy)) 
        original[row-1][col-1] = 8
    if event.key == pg.K_9: 
        pg.draw.rect(screen, (255,255,255), (40*col-18,40*row-18,36,36))
        screen.blit(nine, (posx,posy)) 
        original[row-1][col-1] = 9

    if event.key == pg.K_SPACE: 
        solve()
        show_ans()

while(True): 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            pg.quit() 
        elif event.type is pg.MOUSEBUTTONDOWN: 
            user_click()
        if event.type == pg.KEYDOWN:
            key_pressed()
    pg.display.update() 
    CLOCK.tick(fps) 