# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(juice, capacity):
    # write your code in Python 3.6
    remain = [capacity[i]-juice[i] for i in range(len(juice))]
    max_cap = max(remain)
    ans = 0
    cap = 0
    while cap <= max_cap:
        cap += min(juice)
        juice.remove(min(juice))
        ans += 1
    return ans
