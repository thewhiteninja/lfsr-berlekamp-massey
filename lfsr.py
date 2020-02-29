import collections
import functools


class LFSR:
    def __init__(self, polynomial, seed):
        self._dq = collections.deque(maxlen=len(seed))
        for i in seed:
            self._dq.append(int(i))
        self._polynomial = polynomial
        degree = max(polynomial)
        b = map(lambda x: degree - x - 1, polynomial)
        self._polynomial_bin = [1 if i in b else 0 for i in range(len(seed))][::-1]
        self._clock = 0

    def set_state(self, state):
        self._dq.clear()
        for i in state:
            self._dq.append(i)
        self._clock = 0

    def next_bit(self):
        b = 0
        for i in range(len(self._polynomial_bin)):
            if self._polynomial_bin[i] == 1:
                b = b ^ self._dq[i]
        ret = self._dq.popleft()
        self._dq.append(b)
        self._clock += 1
        return ret

    def next_byte(self):
        return functools.reduce(lambda x, y: x << 1 | y, [self.next_bit() for _ in range(8)])

    def get_clock(self):
        return self._clock

    def _get_polynomial_string(self):
        result = ''
        lis = sorted(self._polynomial, reverse=True)
        for i in lis:
            if i == 0:
                result += '1'
            else:
                result += 'x^%s' % str(i)
            if i != lis[-1]:
                result += ' + '
        return result

    def __str__(self):
        return self._get_polynomial_string()

    def __repr__(self):
        return "<%s polynomial=%s clock=%d>" % (self.__class__.__name__, self._get_polynomial_string(), self._clock)
