def runner_up(n,score_arr):
    arr = list(set(score_arr))
    arr.sort(reverse=True)
    
    if len(arr) > 1:
        return arr[1]
    else:
        return "No runner-up."
    
    
    
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(runner_up(n,arr))
