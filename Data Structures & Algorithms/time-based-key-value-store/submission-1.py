class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        data = self.data[key]
        n = len(data)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if data[m][0] <= timestamp:
                if m == n - 1 or data[m + 1][0] > timestamp:
                    return data[m][1]
                else:
                    l = m + 1
            else:
                r = m - 1

        return ""
