# """
# #피보나치
# n=int(input('n_th pivo: '))
# list=[1,1]
# sum=1

# for i in range(2,n,1):
#     sum = list[i-1] + 2*list[i-2]
#     list.append(sum)

# print(list[n-1])
# print(list)
# """
# rosalind_fib
# dataset: a b
# a == n == num
# b == k == K


def Fibo(num, K):
    l_result = [1, 1]
    for i in range(1, num - 1):  # k번째 항까지만 알면되니까!
        l_result.append(l_result[-1] + (K * l_result[-2]))
    print(l_result)
    return l_result[-1]  # 마지막 항


n = int(input("fibo: "))
k = int(input("k: "))
print(Fibo(n, k))
