# team wins reaches 25points and leads the other team by 2 or more teams

# each line of input two integers 
# opt = 1 -> Qingcheng scores
# opt = 2 -> Wuye scores 
# x is points that player get consecutively


# rule is best-of-three
# first 2 or 3 lines pirnt score (N:M)
# last line print who won (1 = Qingcheng, 2=Wuye)

game_scores=[]
win_Q=0
win_W=0

cur_scores=[0, 0]
while win_Q <2 and win_W<2:
    input_str = input()
    # 0 - Qing, 1-Wuye
    
    opt=int(input_str.split()[0])
    x=int(input_str.split()[1])

    cur_scores[opt-1]+=x

    # game set
    if cur_scores[0]>=25 and cur_scores[0] > cur_scores[1]+1:
        win_Q+=1
        game_scores.append(f"{cur_scores[0]}:{cur_scores[1]}")
        cur_scores=[0, 0]
    elif cur_scores[1]>=25 and cur_scores[1]>cur_scores[0]+1:
        win_W+=1
        game_scores.append(f"{cur_scores[0]}:{cur_scores[1]}")
        cur_scores=[0, 0]

for score in game_scores:
    print(score)
print(1 if win_==2 else 2)
