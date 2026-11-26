class TimeMap:

    def __init__(self):
        # hashmap of lists, to make more efficient to BS on get
        # if times are put in order should work
        self.kvstore = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvstore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # timestamp_prev <= timestamp so want closest <=
        # timestamps are stricly increasing according to description
        res = ""
        values = self.kvstore.get(key, []) # empty list if not there
        l = 0 
        r = len(values) - 1
        while l <= r:
            mid = (l + r) // 2 # integer division
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        