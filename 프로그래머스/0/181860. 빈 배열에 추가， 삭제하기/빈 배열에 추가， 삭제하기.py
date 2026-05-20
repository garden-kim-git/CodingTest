# def solution(arr, flag):
#     answer = []
#     for i in range(len(arr)) :
#         if flag[i] : answer.extend([arr[i]]*2*arr[i])
#         else : answer = answer[:-(arr[i])]
#     return answer

def solution(arr, flag):
    answer = []
    for index, item in enumerate(flag) :
        if item : answer.extend([arr[index]] * arr[index] * 2)
        else : answer = answer[:-arr[index]]

    return answer