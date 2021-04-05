x = 3
won = 0
loss = 0
draw = 0
while x != 0:
    comp_C = 'Scissors'
    user_C = input('Do you want: Rock, Paper or Scissors ?\n ')
    if comp_C == user_C:
        draw = draw + 1
        print('draw' + ' You have won ' + str(won) + ' and lost ' + str(loss) + ' we have ' + str(draw) + ' draw games')
    elif user_C == 'Rock':
        won = won + 1
        print('you won' + ' You have won ' + str(won) + ' and lost ' + str(loss) + ' we have ' + str(draw) + ' draw games')
    else :
        loss = loss +1
        print('you lost' + ' You have won '+ str(won) + ' and lost ' + str(loss) + ' we have ' + str(draw) + ' draw games')
    x = x-1

