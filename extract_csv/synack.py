import re
from queue import Queue
RE_TIMERELATIVE = re.compile(r"(\d+)[.](\d{9})")

def rtime_make(time_relative):
    matched = RE_TIMERELATIVE.match(time_relative)
    if matched is None:
        raise Exception(f"No TimeRelative Format : {time_relative}")
    
    return int(matched.group(1)), int(matched.group(2))

def rtime_sub(time1, time2):
    a = time1[0] - time2[0]
    b = time1[1] - time2[1]
    if b < 0:
        b += 1000000000
        a -= 1
    return (a, b)

def rtime_export(rtime):
    return f"{rtime[0]}.{rtime[1]:0>9}"

class SynAck:
    def __init__(self):
        self.synqueues = {}

    def syn(self, src, dst, time_relative):
        time = rtime_make(time_relative)
        key = (src, dst)
        if key not in self.synqueues:
            self.synqueues[key] = Queue()
        self.synqueues[key].put(time)

    def ack(self, src, dst, time_relative):
        time = rtime_make(time_relative)
        key = (dst, src)
        if key not in self.synqueues:
            return rtime_export((0,0))
        q = self.synqueues[key]
        while q.qsize():
            syntime = q.get()
            rtime = rtime_sub(time, syntime)
            if rtime[0] >= 10: #timeout 10s?
                continue
            return rtime_export(rtime)
        else:
            return rtime_export((0,0))


if __name__ == "__main__":
    sa = SynAck()
    sa.syn("1", "2", "0.000001234")
    sa.syn("1", "2", "0.000010000")
    print(sa.ack("2", "1", "0.000011234"))
    print(sa.ack("2", "1", "0.000011235"))