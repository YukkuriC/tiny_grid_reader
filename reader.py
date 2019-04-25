from math import floor, ceil


class Mapper:
    def __init__(self, filename, sep=',', flipx=False, flipy=False):
        with open(filename) as f:
            data = f.read().split('\n')
        self.ylab = []
        self.data = []
        for i, line in enumerate(data):
            if i == 0:
                self.xlab = list(map(float, line.split(sep)[1:]))
                if flipx:
                    self.xlab = self.xlab[::-1]
                continue
            if not line:
                continue
            line = list(map(float, line.split(sep)))
            self.ylab.append(line.pop(0))
            if flipx:
                line = linex[::-1]
            self.data.append(line)
        if flipy:
            self.data = self.data[::-1]
            self.ylab = self.ylab[::-1]

    @staticmethod
    def bsearch(lst, val):
        if val <= lst[0]:
            return 0
        if val >= lst[-1]:
            return len(lst) - 1
        l, r = 0, len(lst) - 1
        while l < r:
            m = (l + r) // 2
            if lst[m] == val:
                return m
            elif lst[m] < val:
                l = m + 1
            else:
                r = m - 1
        while lst[l] > val:
            l -= 1
        while lst[r] < val:
            r += 1
        if l == r:
            return l
        return l + (r - l) * (val - lst[l]) / (lst[r] - lst[l])

    @staticmethod
    def get_val(lst, ind):
        if ceil(ind) == floor(ind):
            return lst[floor(ind)]
        les, mor = floor(ind), ceil(ind)
        a, b = lst[les], lst[mor]
        return a + (b - a) * (ind - les) / (mor - les)

    def get_xy(self, x, y):
        x = self.bsearch(self.xlab, x)
        y = self.bsearch(self.ylab, y)
        if floor(y) == ceil(y):
            return self.get_val(self.data[floor(y)], x)
        les, mor = floor(y), ceil(y)
        a = self.get_val(self.data[les], x)
        b = self.get_val(self.data[mor], x)
        return a + (b - a) * (y - les) / (mor - les)


print('Reader'.center(30, '='))
if __name__ == '__main__':
    import sys
    PATH = r"""test.csv"""
    test = Mapper(PATH, ',', flipy=1)
    while 1:
        try:
            row, col = map(float, input('输入坐标，空格分隔: ').split())
            print(test.get_xy(col, row))  # y,x -> x,y
        except EOFError:
            sys.exit()
        except:
            continue