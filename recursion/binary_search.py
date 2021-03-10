"""
二分搜索:
    1.用在有序的序列
    2.时间复杂度是O(logn)
递归实现
    查找失败返回None
    取中值
    目标大于中值,则从中值右边开始查找
    目标小于中值,则从中值左边开始查找
    目标定于中值,则返回中值
循环版和递归版比较
    递归的实现一般要设置更多的参数,通过函数参数来存储变化的变量,从而通过递归实现
    不论是递归还是循环,都要设置好终止条件
"""

def binary_search(S,target,low,high):
    
    if low > high:
        return None
    mid = (low+high) // 2
    tmp = S[mid]
    if target < tmp:
        return binary_search(S,target,low,mid-1)
    if target > tmp:
        return binary_search(S,target,mid+1,high)
    return mid

def loop_binary_search(S,target):
    low = 0
    high = len(S) - 1
    
    while (low <= high):
        mid = (low+high) // 2
        tmp = S[mid]
        if target > tmp:
            low = mid + 1
        elif target < tmp:
            high = mid - 1
        else:
            return mid


if __name__=="__main__":
    a = [2,4,7,9,10,18,20]
    binary_search(a,10,0,len(a))
    loop_binary_search(a,10)
    binary_search(a,11,0,len(a))
    loop_binary_search(a,11)
