#입력 조건
#첫 번째 줄에 N(1<=N<= 100,000)과 K(2<=K<=100,000)가 공백을 기준으로 하여 각각 자연수로 주어진다
#출력 조건
#첫 번째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다
#1번. N에서 1을 뺍니다
#2번. N을 K로 나눕니다


N, K = map(int, input().split())    #input: N, K
cnt = 0     #수행 횟수 값 초기화

while(N!=1):    #N이 1일 경우 종료 (while)
  if (N % K == 0):  #아닐 경우 N-1, count + 1
    N = N // K
    cnt += 1
  else:     #N%K==0이면 N//K, count + 1
    N -= 1
    cnt +=1
    
print(cnt)