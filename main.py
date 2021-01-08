from random import randint

print('choese one of them: "rock" "paper" "rock"')

computerMove = randint(0, 2)

if computerMove == 0:
    computerMove = 'rock'
elif computerMove == 1:
    computerMove = 'paper'
elif computerMove == 2:
    computerMove = 'sizors'

playerMove = input(f'player move= ').lower()
print(f'computer move= {computerMove}')

if playerMove == computerMove:
    print('draw')
elif playerMove == 'rock':
    if computerMove == 'papaer':
        print('computer wins!')
    elif computerMove == 'sizors':
        print('player wins!')
elif playerMove == 'paper':
    if computerMove == 'rock':
        print('player wins!')
    elif computerMove == 'sizors':
        print('computer wins!')
elif playerMove == 'sizors':
    if computerMove == 'rock':
        print('computer wins!')
    elif computerMove == 'paper':
        print('player wins!')
else:
    print('something went wrong')
