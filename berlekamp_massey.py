class BerlekampMassey:
    def __init__(self, sequence):
        n = len(sequence)
        s = map(int, sequence)

        k = 0
        for k in range(n):
            if s[k] == 1:
                break
        self._f = {k + 1, 0}
        self._l = k + 1

        g = {0}
        a = k
        b = 0

        for n in range(k + 1, n):
            d = 0
            for item in self._f:
                d ^= s[item + n - self._l]

            if d == 0:
                b += 1
            else:
                if 2 * self._l > n:
                    self._f ^= set([a - b + item for item in g])
                    b += 1
                else:
                    temp = self._f.copy()
                    self._f = set([b - a + item for item in self._f]) ^ g
                    self._l = n + 1 - self._l
                    g = temp
                    a = b
                    b = n - self._l + 1

    def _get_polynomial_string(self):
        result = ''
        lis = sorted(self._f, reverse=True)
        for i in lis:
            if i == 0:
                result += '1'
            else:
                result += 'x^%s' % str(i)

            if i != lis[-1]:
                result += ' + '
        return result

    def get_polynomial(self):
        return list(self._f)

    def get_polynomial_degree(self):
        return self._l

    def __str__(self):
        return self._get_polynomial_string()

    def __repr__(self):
        return "<%s polynomial=%s>" % (self.__class__.__name__, self._get_polynomial_string())
