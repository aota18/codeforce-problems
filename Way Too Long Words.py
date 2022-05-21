n=input()
word_list=[]
for i in range(int(n)):
    word_list.append(input())

for word in word_list:
    # if len(word) > 10
    if len(word)<=10:
        print(word)
    else:
        print(word[0]+str(len(word)-2)+word[len(word)-1])