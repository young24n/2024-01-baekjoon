T = int(input(""))
results = []

for i in range(T):
    A = list(map(int, input().split()))
    sorted_A = sorted(A, reverse=True)
    results.append(sorted_A[2])

for result in results:
    print(result)