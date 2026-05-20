def solution(arr, k):
    answer = []
    mylist = list(dict.fromkeys(arr))
    
    if len(mylist) > k :
        answer = mylist[:k]
    elif len(mylist) < k :
        answer = mylist
        answer.extend([-1] * (k-len(mylist)))
    else : answer = mylist
        
    return answer