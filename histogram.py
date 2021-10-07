class Histogram:
    def __init__(self, beg, end, bars):
        beg, end, bars = float(beg), float(end), int(bars)
        self.beg = beg
        self.end = end
        self.heights = [0.0 for _ in range(bars)]
        self.find_bar_coef = bars / (end - beg)

    def bar_idx(self, val):
        i = int((val - self.beg) * self.find_bar_coef)
        if i == len(self.heights):
            return i - 1
        else:
            return i

    def add(self, val):
        idx = self.bar_idx(val)
        self.heights[idx] += 1.0

    def add_from_list(self, vals):
        for v in vals:
            self.add(v)

    def bar_len(self):
        return (self.end - self.beg) / len(self.heights)

    def area(self):
        return sum(self.heights) * self.bar_len()

    def normalize(self):
        inv_area = 1.0 / self.area()
        for i, _ in enumerate(self.heights):
            self.heights[i] *= inv_area

    def pairs(self):
        d = self.bar_len()
        first = self.beg + d * 0.5
        return map(lambda i_h: (first + i_h[0] * d, i_h[1]), enumerate(self.heights))
