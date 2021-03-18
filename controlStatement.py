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


#continue문 - continue 만나면 그 아래 코드 실행하지 않고 바로 while의 조건문으로 점프한다.
i = 0
while i < 15: #i가 홀수면 이 부분으로 온다.
    i = i + 1
    # i가 홀수면 print(i) 안 하고 바로 조건 부분으로 돌아감
    if i % 2 == 1:
        continue #i가 홀수가 맞으면 실행하는 부분
    print(i)


print(" ============= ")
n = 1
i = 1

# while n < 10:
#     while i < 10:
#         print("{} * {} = {}".format(n, i, n*i))



# 예제
print(" == 예제 1 ==")
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")

# 테스트
print_grade(40, 45)
print_grade(20, 35)
print_grade(30, 32)
print_grade(50, 45)


print()
print(" == 예제 2 == ")
# 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.
while i <= 100:
    if ((i % 8) == 0) & ((i % 12) != 0):
        print(i)
    i += 1


print()
print(" == 예제 3 == ")
# 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써 보세요.
i = 2
sum = 0
while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        sum += i
        # sum = i + sum
    i += 1
print(sum)


print()
print(" == 예제 4 == ")
# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써 보세요
sum = 0
i = 1

while i <= 120:
    if 120 % i == 0: #약수가 맞다면!!
        print(i) #약수 출력
        sum += 1 # sum = sum + 1
    i += 1
print("120의 약수는 총 {}개입니다.".format(sum))



print()
print(" == 예제 5 == ")
money = 50000000 #5천만원 - 1988
apartment1988 = 50000000
aprtment2016 = 1100000000

#2016 은행돈 = money
#print(2016 - 1988)=28
n = 1
while n < 29:
    money *= 1.12 #money = money * 1.12
    n += 1

moneywin = money - aprtment2016
eunmiwin = aprtment2016 - money
if money > aprtment2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(moneywin)))
elif aprtment2016 > money:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(eunmiwin)))


