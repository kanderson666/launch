class GoodCat:

    counter = 0                  # class variable

    def __init__(self):
        self.__class__.counter += 1

    @classmethod
    def number_of_cats(cls):
        return cls.counter

class ReallyGoodCat(GoodCat):
    pass

cat1 = GoodCat()
cat2 = GoodCat()
cat3 = ReallyGoodCat()

print(GoodCat.number_of_cats())        # 2
print(GoodCat.counter)                 # 2
print(ReallyGoodCat.number_of_cats())  # 3
print(ReallyGoodCat.counter)           # 3
cat4 = GoodCat()
print(GoodCat.counter)                 # 3
print(ReallyGoodCat.counter)           # 3
