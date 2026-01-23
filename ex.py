def test():
    def test1():
        def test2(num=[1]):
            num[0] += 1
            print(num[0])
        test2()
    test1()
    test1()
test()
# ==> 2     # 2, 3
# ==> 3
# ==> 2
# ==> 3
