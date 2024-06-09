def game():
    return 44677123

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScor<score:
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
'''
elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))
        '''