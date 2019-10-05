import random

# ~~~ Variables ~~~
ch = ['Rock', 'Paper', 'Scissors']
ai = ''

# ~~~ AI ~~~

ai = random.choice(ch)

# ~~~ Player ~~~

player = input('Move: ')

# ~~~ Determing wins/losses ~~~

# Tie
if ai == player:
    print('Tie!')
    
# AI got rock    
elif ai == 'Rock':
    if player == 'Paper':
        print('Win!')
    elif player == 'Scissors':
        print('Lose!')
        
# AI got paper       
elif ai == 'Paper':
    if player == 'Rock':
        print('Lose!')
    elif player == 'Scissors':
        print('Win!')
        
# AI got scissors   
elif ai == 'Scissors':
    if player == 'Rock':
        print('Win!')
    elif player == 'Paper':
        print('Lose!')

# ~~~ Debugging ~~~
print('AI chose: ' + ai)
print('Player chose: ' + player)
