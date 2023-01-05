import random
print('For Hasy press e')
print('For Mediam press m')
print('For Hard press h')
b=input('level->')
if b=='e':
    randNo = random.randint(1, 10)
elif b=='m':
    randNo = random.randint(1, 25)
elif b=='h':
    randNo = random.randint(1, 50)
count=0
while (True):
    print('Press Q to quit')
    if b=='e':
        a = input("Enter a number(1 to 10):")
    elif b=='m':
        a = input("Enter a number(1 to 25):")
    elif b=='h':
        a = input("Enter a number(1 to 50):")
    if a=='Q':
        break
    
    while (True):
        try:
            a=int(a)
            if randNo<a:
                print('NOPE!!  Gusse smaller')
                count+=1
                a=int(input())
            elif randNo>a:
                print('NOPE!!  Gusse higher')
                count+=1
                a=int(input())
            elif randNo==a:
                print('WOW!! You Win \nscore:',count)
                if b=='e':
                    randNo = random.randint(1, 10)
                elif b=='m':
                    randNo = random.randint(1, 25)
                elif b=='h':
                    randNo = random.randint(1, 50)
                count=0
                break
        except Exception as e:
            print("Wrong Try")
            break
print('Timepass Done')