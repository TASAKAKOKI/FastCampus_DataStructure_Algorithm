# 코딩테스트에 주로 쓰이는수학이론은 대개 정수론, 기하학이 있다.
import math
import time
# 방법1: 단순 반복문 사용
# 시간복잡도 O(N)


# GCD와 LCM은 수학문제가 나오는 경우 50%확률로 해당하는 개념이므로 숙지!
# GCD(최대공약수,greatest common divider), LCM(최소공배수,least common multiple)
# 해법은 3가지 방법이 있다.
# 1. 단순 반복문을 통한 풀이: 시간 복잡도 최악
# 2. 유클리드 호제법을 이용한 풀이: 가장 추천
# 유클리드 호제법이란, GCD(a,b) = GCD(b,a%b) 임을 사용하는 것.
# 3. math 라이브러리를 사용: 가장 최적화 되어 있지만, 시험에서는 사용하지 못할 수 있음


def gcd_naive(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# 방법2: 유클리드호제법 사용
# 2-1 재귀 사용


def gcd1(a, b):
    return gcd1(b, a % b) if a % b != 0 else b
# 2-2 반복문으로 사용


def gcd2(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


# 방법3: math패키지의 gcd 사용
math.gcd(1, 2)

start1 = time.time()*1000000000
print(gcd_naive(10**10, 2**20))
print(f'gcd_naive는 {time.time()*1000000000-start1}시간 소요')

start2 = time.time()*1000000000
print(gcd1(10**10, 2**20))
print(f'gcd1은 {time.time()*1000000000-start2}시간 소요')

start3 = time.time()*1000000000
print(gcd2(10**10, 2**20))
print(f'gcd2는 {time.time()*1000000000-start3}시간 소요')

start4 = time.time()*1000000000
print(math.gcd(10**10, 2**20))
print(f'math.gcd는 {time.time()*1000000000-start4}시간 소요')


# lcm(Lesss common multipli)
# lcm은 gcd를 활용하여 계산
# 만약 python이 아닌 다른 언어의 경우 int overflow가 발생할 수 있으므로,
# a / gcd(a,b) * b 의 순서로 하는 것이 보다 정석이라고 할 수 있다.
def lcm(a, b):
    return a*b/math.gcd(a, b)


print(lcm(10*2, 2*2))
