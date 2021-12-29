x=int(0)
y=int(0)
z=int(0)
score=list((x,y,z))
for i in range(0,15):
    bett1=int(input('mari_bett: '))
    bett2=int(input('cr_bett: '))
    bett3=int(input('elhadi_bett: '))
    score1=int(input('mari_score: '))
    score2=int(input('cr_score: '))
    score3=int(input('elhadi_score: '))
    if bett1==score1!=0:
        x= bett1 + score1 + 1 + x
        score[0]=x
    elif bett1==score1==0:
        x= x + 2
        score[0]=x
    elif bett1<score1:
        x= bett1 - score1 + x
        score[0]=x
    elif bett1>score1:
        x= score1 - bett1 +x
        score[0]=x
    if bett2==score2!=0:
        y= bett2 + score2 + 1 + y
        score[1]=y
    elif bett2==score2==0:
        y= y + 2
        score[1]=y
    elif bett2<score2:
        y= bett2 - score2 + y
        score[1]=y
    elif bett2>score2:
        y= score2 - bett2 + y
        score[1]=y
    if bett3==score3!=0:
        z= bett3 + score3 + 1 + z
        score[2]=z
    elif bett3==score3==0:
        z= z + 2
        score[2]=z
    elif bett3<score3:
        z= bett3 - score3 + z
        score[2]=z
    elif bett3>score3:
        z= score3 - bett3 + z
        score[2]=z
    print(score)
        
