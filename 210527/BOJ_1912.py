# No.1912 연속합
# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.
# 예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

# 입력: 첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.
# 출력: 첫째 줄에 답을 출력한다.

N = int(input())
arr = list(map(int, input().split()))

dp = []
for i in range(N):
  if i == 0:
    dp.append(arr[i])
  else:
    dp.append(max(dp[i-1] + arr[i], arr[i]))

print(max(dp))


# 풀이 (인덱스라고 생각하지 말고 그냥 순서 1, 2, 3이라고 생각하고 풀어놓음)
# 세 번째 수까지의 최대값은 max(arr[1] + arr[2] + arr[3], arr[2] + arr[3], arr[3]) 중 하나인데, arr[1] + arr[2]와 arr[2] 중에 누가 큰 지는 두 번째 수의 최대값을 구할 때 이미 정해졌다.
# 그러므로 그 전의 최대값인 dp[2]와 arr[3]을 더한 값과 arr[3] 중에 어떤 값이 가장 큰 지만 판단하면 된다!