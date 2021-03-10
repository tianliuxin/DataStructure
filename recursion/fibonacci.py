"""
斐波拉契数列
    表达式
        f(n) = 0,n=0
        f(n) = 1,n=1
        f(n) = f(n-1) + f(n-2) n>1
    有趣的斐波拉契数列
        该数列的应用是十分丰富的,这里不探究其数学方法,只从表达式本身出发来用计算机求解
        1.递归法
        2.循环法
        3.递归缓存
"""

def fib1(n):
    if n<2:
        return n
    return fib1(n-1)+fib1(n-2)

def fib2(n):
    return n if n<2 else fib2(n-1)+fib2(n-2)

"""
循环版计算逻辑:
    保存最后一个值
    更新最后一个值
    将保存的值赋值给前一个值
"""
def fib3(n):
    a,b = 0,1
    while n>0:
        a,b = b,a+b # 保存最后一个值,计算下个值作为最后一个值
        n-=1
    return a

def fib4(n):
    a,b = 0,1
    while n>0:
        a,b = b,a+b
        n-=1
        yield a

if __name__=="__main__":
    for i in fib4(7):
        print(i)
    fib3(7)