import random
board=[
      ['','',''],
      ['','',''],
      ['','','']
    ]
game_on=True
count=0
num=random.randint(0,1)
def check():
  if game_on==False:
    exit()
def draw():
 print( '_______________________________________')
 for i in range(3):
 
  print( '|         |            |              |')
  print( '|         |            |              |')
  print(f'|     {board[i][0]}    |        {board[i][1]}    |       {board[i][2]}       |')
  print( '|_________|____________|______________|')
def rules():
  print('          Rules            ')
  print('. You are x')
  print('   Computer is y')
def player(count,board):
 square=int(input('What number square do you want to put you piece in? ')) 
 
 if square==1 and board[0][0]=='':
   board[0][0]='x'
   count+=1
 elif square=='exit':
   print('Goodbye')
   exit()
 elif square==2 and board[0][1]=='':
   board[0][1]='x'
   count+=1
 elif square==3 and board[0][2]=='':
   board[0][2]='x'
   count+=1
 elif square==4 and board[1][0]=='':
   board[1][0]='x'
   count+=1
 elif square==5 and board[1][1]=='':
   board[1][1]='x'
   count+=1
 elif square==6 and board[1][2]=='':
   board[1][2]='x'
   count+=1
 elif square==7 and board[2][0]=='':
   board[2][0]='x'
   count+=1
 elif square==8 and board[2][1]=='':
   board[2][1]='x'
   count+=1
 elif square==9 and board[2][2]=='':
   board[2][2]='x'
   count+=1
 else:
   print('sorry you cannot put it there')
   player()
 return count,board

def check_if_put_piece(put_piece,square,count):
  if square==1 and board[0][0]=='':
    board[0][1]='0'
    count+=1
    put_piece=True
  elif square==2 and board[0][1]=='':
    board[0][1]='0'
    count+=1
    put_piece=True
  elif square==3 and board[0][2]=='':
    board[0][2]='0'
    count+=1
    put_piece=True
  elif square==4 and board[1][0]=='':
    board[1][0]='0'
    count+=1
    put_piece=True
  elif square==5 and board[1][1]=='':
    board[1][1]='0'
    count+=1
    put_piece=True
  elif square==6 and board[1][2]=='':
    board[1][2]='0'
    count+=1
    put_piece=True
  elif square==7 and board[2][0]=='':
    board[2][0]='0'
    count+=1
    put_piece=True
  elif square==8 and board[2][1]=='':
    board[2][1]='0'
    count+=1
    put_piece=True
  elif square==9 and board[2][2]=='':
    board[2][2]='0'
    count+=1
    put_piece=True
  else:
   square=random.randint(0,9)  
  return put_piece,board,square

# This function is Computer playing
def computer(count,board):
 square=random.randint(0,9) #defining square
 put_piece=False
 while put_piece!=True:
   put_piece,board,square=check_if_put_piece(put_piece,square,count)
 print(board)
 return count,board

def check_if_board_is_filled():
  if count==9:
    print('Tie')
    print('Hope you like this game')
    exit()
def check_if_Win(game_on):
 #computer matches
 
 if board[0][0] == board[0][1] == board[0][2]=='0':
     print('Computer won by matching a row')
     print('Hope you like this game!')
     game_on=False
 if board[1][0] == board[1][1] == board[1][2]=='0':
     print('Computer won by matching a row')
     print('Hope you like this game!')
     game_on=False
 if board[2][0] == board[2][1] == board[2][2]=='0':
     print('Computer won by matching a row')
     print('Hope you like this game!') 
     game_on=False
 if board[0][0] == board[1][0] == board[2][0]=='0':
     print('Computer won by matching a row')
     print('Hope you like this game!') 
     game_on=False
 if board[0][1] == board[1][1] == board[2][1]=='0':
     print('Computer won by matching a row')
     print('Hope you like this game!') 
     game_on=False
 if board[0][2] == board[1][2] == board[2][2]=='0':
     print('Computer won by matching a row')
     print('Hope you like this game!') 
     game_on=False
 if board[0][0] == board[1][1] == board[2][2]=='0':
     print('Computer won by matching a row')
     print('Hope you like this game!')
     game_on=False
 if board[0][2] == board[1][1] == board[2][0]=='0':
     print('Computer won by matching a row')
     print('Hope you like this game!')
     game_on=False
 if board[0][0] == board[0][2] == board[2][0] == board[2][2]=='0':
     print('Computer won by matching 4 corners')
     print('Hope you like this game')
     game_on=False
  
  #x matches

 if board[0][0] == board[0][1] == board[0][2]=='x':
     print('Player won by matching a row')
     print('Hope you like this game!')
     game_on=False
 if board[1][0] == board[1][1] == board[1][2]=='x':
     print('Player won by matching a row')
     print('Hope you like this game!')
     game_on=False
 if board[2][0] == board[2][1] == board[2][2]=='x':
     print('Player won by matching a row')
     print('Hope you like this game!') 
     game_on=False
 if board[0][0] == board[1][0] == board[2][0]=='x':
     print('Player won by matching a row')
     print('Hope you like this game!') 
     game_on=False
 if board[0][1] == board[1][1] == board[2][1]=='x':
     print('Player won by matching a row')
     print('Hope you like this game!') 
     game_on=False
 if board[0][2] == board[1][2] == board[2][2]=='x':
     print('Player won by matching a row')
     print('Hope you like this game!') 
     game_on=False
 if board[0][0] == board[1][1] == board[2][2]=='x':
     print('Player won by matching a row')
     print('Hope you like this game!')
     game_on=False
 if board[0][2] == board[1][1] == board[2][0]=='x':
     print('Player won by matching a row')
     print('Hope you like this game!')
     game_on=False
 if board[0][0] == board[0][2] == board[2][0] == board[2][2]=='x':
     print('Player won by matching 4 corners')
     print('Hope you like this game')
     game_on=False
 return game_on
def mainloop(game_on):
 if num==0:
  move='o'
  print('The turn goes to computer.')
  draw()
  while game_on==True:
    
    computer(count,board)
    draw()
    player(count,board)
    game_on=check_if_Win(game_on)
    check()
    draw()
    check_if_board_is_filled()
 if num==1:
  move='x'
  print('The turn goes to the player.')
  draw()
  while game_on==True:
    
    player(count,board)
    draw()
    computer(count,board)
    draw()
    game_on=check_if_Win(game_on)
    check()
    draw()
    check_if_board_is_filled()
mainloop(game_on)