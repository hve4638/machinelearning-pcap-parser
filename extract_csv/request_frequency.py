import re

"""

"""
class RequestFrequency:
    RE_TIMERELATIVE = re.compile(r"(\d+)[.](\d{9})")
    def __init__(self, time_interval=1):
        self.time_latest = (0, 0)
        self.interval = time_interval
        self.request_count = {}

    def add(self, time_relative:str, addr):
        matched = self.RE_TIMERELATIVE.match(time_relative)
        if matched is None:
            raise Exception(f"No TimeRelative Format : {time_relative}")
        
        num = int(matched.group(1)), int(matched.group(2))
        if self.__compare(self.time_latest, num) < 0:
            raise Exception(f"TimeSequence Error : {time_relative} < {num}")
        else:
            self.time_latest = num

        index = num[0]
        if index not in self.request_count:
            self.request_count[index] = {}
        if addr not in self.request_count[index]:
            self.request_count[index][addr] = 0
        
        self.request_count[index][addr] += 1
        return self.get(addr)

    def get(self, addr):
        sum = 0
        for index in range(self.time_latest[0], self.time_latest[0]-self.interval-1, -1):
            if index not in self.request_count:
                continue
            if addr not in self.request_count[index]:
                continue
            sum += self.request_count[index][addr]

        return sum

    def __compare(self, num1, num2):
        if num1[0] > num2[0]:
            return -1
        elif num1[0] < num2[0]:
            return 1
        elif num1[1] > num2[1]:
            return -1
        elif num1[1] < num2[1]:
            return 1
        else:
            return 0

if __name__ == "__main__":
    rf = RequestFrequency(time_interval=2)
    print(rf.add(time_relative="0.000201234", addr="1"))
    print(rf.add(time_relative="0.000201235", addr="1"))
    print(rf.add(time_relative="1.100201235", addr="1"))
    print(rf.add(time_relative="2.100201235", addr="1"))
    print(rf.add(time_relative="2.100201235", addr="1"))
    print(rf.add(time_relative="4.100201235", addr="1"))
