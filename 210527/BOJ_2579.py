# No.2579 계단 오르기
# 계단 오르기 게임은 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 가는 게임이다. <그림 1>과 같이 각각의 계단에는 일정한 점수가 쓰여 있는데 계단을 밟으면 그 계단에 쓰여 있는 점수를 얻게 된다.

# 계단 오르는 데는 다음과 같은 규칙이 있다.

# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.

# 따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.
# 각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 입력의 첫째 줄에 계단의 개수가 주어진다.
# 둘째 줄부터 한 줄에 하나씩 제일 아래에 놓인 계단부터 순서대로 각 계단에 쓰여 있는 점수가 주어진다. 계단의 개수는 300이하의 자연수이고, 계단에 쓰여 있는 점수는 10,000이하의 자연수이다.

# 출력 : 첫째 줄에 계단 오르기 게임에서 얻을 수 있는 총 점수의 최댓값을 출력한다.

N = int(input())
arr = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N)]
for i in reversed(range(N)):
  if i == N-1:
    dp[i] = arr[i]
  elif i == N-2:
    dp[i] = arr[i] + arr[i+1]
  elif i == N-3:
    dp[i] = arr[i] + arr[i+2]
  else:
    dp[i] = max(dp[i+2] + arr[i], dp[i+3] + arr[i+1] + arr[i])

print(max(dp))

# 2156의 포도주 시식 문제와 같다!
# 다른 점은 무조건 마지막 계단은 밟아야 한다는 점이다.
# 그래서 포도주 시식과 달리 마지막 입력값부터 계산해서 최대값을 출력했다.