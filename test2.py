import sys
input = sys.stdin.readline
T = int(input().strip())
count = 0
for i in range(T):
    word = input().strip()
    group = []
    check=True
    for i in range(0,len(word)):
        #한 글자일 때는 무조건 그룹 단어
        if len(word) == 1:
            count+=1
        if word[i] not in group:
            group.append(word[i])
            continue
        if word[i] != word[i-1]:
            check = False
            if check == False:
                break
        if check == True:
            count+=1
print(count)