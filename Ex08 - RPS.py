from pyfiglet import Figlet
import random

# custom_fig = Figlet(font='cybermedium')
# custom_fig = Figlet(font='doom')
custom_fig = Figlet(font='shadow')
# custom_fig = Figlet(font='gothic')
def printword (val):
    if val=='r':
        print ('You chose rock')
    elif val=='p':
        print ('You chose paper')
    else:
        print ('You chose scissors')
    
print(custom_fig.renderText('Rock - Paper - Scissors'))

print ('How to play')
print ('Rock beats Scissors, Scissors beats Paper and Paper beats Rock.')
print ('Enter to quit')
gameon = True
rpsl = ['r','p','s']
wins = 0
losses = 0
draws = 0
aprev=''
hprev=''
won=False
while gameon:
    rps = input ('Enter r for rock, p for paper and s for scissors ')
    if rps == '':
        print ('Here are your draws: ',draws)
        print ('Here are your wins: ',wins)
        print ('Here are your losses: ',losses)
        break
    printword (rps)

    if hprev=='':
        index = random.randint(0,2)
    elif hprev=='r':
        index=1
    elif hprev=='p':
        index=2
    elif hprev=='s':
        index=0
      
    print ("A.I. chose "+ rpsl[index])
    comchoice=rpsl[index]
    if rps == comchoice:
        print('Draw, try again')
        draws = draws + 1
    elif rps == 'r'and comchoice == 's':
        print ('You win, congrats')
        wins = wins + 1
        won=False
    elif rps == 'p'and comchoice =='r':
        print ('You win, congrats')
        wins = wins + 1
        won=False
    elif rps == 's'and comchoice =='p':
        print ('You win, congrats')
        wins = wins + 1
        won=False
    else:
        print ("You lose")
        losses = losses + 1
        won=True
        aprev=comchoice

    hprev=rps

