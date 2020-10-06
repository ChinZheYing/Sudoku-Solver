original = [
  [5,3,0,0,7,0,0,0,0],
  [6,0,0,1,9,5,0,0,0],
  [0,9,8,0,0,0,0,6,0],
  [8,0,0,0,6,0,0,0,3],
  [4,0,0,8,0,3,0,0,1],
  [7,0,0,0,2,0,0,0,6],
  [0,6,0,0,0,0,2,8,0],
  [0,0,0,4,1,9,0,0,5],
  [0,0,0,0,8,0,0,7,9]
  ]

solution = original
empty = []
for i in range(9):
  for j in range(9):
    if(original[i][j] == 0):
      empty.append([0,i,j])

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


printsud(original)
print("")

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
printsud(solution)