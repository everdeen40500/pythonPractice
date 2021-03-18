# while문
i = 1
while i <= 5:
    print('hi mark!')
    i += 1


# 예 : while문을 사용하여, 100 이상의 자연수 중 가장 작은 23의 배수를 출력해 보세요.
# 풀이 1
print()
i = 100
n = 1
answer = 23 * n

while answer < i:
    answer = 23 * n
    n += 1
print((n-1) * 23)


# 풀이 2 - "n의 배수면 n으로 나누었을 때 나머지가 0이란 것!" 이 포인트!!!! (n의 배수 % n = 0)
i = 100

while (i % 23) != 0:
    i += 1
print(i)




# if - 만약 / else - 그렇지 않으면
# if 조건부분:  -> 불린값으로 나온다.
#   수행부분
# else:
#   수행부분
print()
temperature = 8
if temperature <= 10:
    print("자켓을 입는다.")
else:
    print("자켓을 입지 않는다")

# elif = else if  -> 맞는 조건 1개가 실행된다!



# break문
i = 100
while True:
    # i가 23의 배수면 반복문을 끝냄(break 자리에서 바로 중단하고 break 전 명령 수행하고 끝낸다.)
    if i % 23 == 0:
        break
    i = i + 1
print(i)


#continue문
i = 0
while i < 15: #i가 홀수면 이 부분으로 온다.
    i = i + 1
    # i가 홀수면 print(i) 안 하고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue #i가 홀수가 맞으면 실행하는 부분
    print(i)