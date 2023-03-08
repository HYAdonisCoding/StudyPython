# 外部函数
def test1():
    k = 10
    n = 20
    
    # 内部函数
    def test2():
        nonlocal k, n
        k = 100
        n = 200
        print('test2')
        
    print(f'k = {k}, n = {n}')
    test2()
    print(f'k = {k}, n = {n}')
    
test1()

