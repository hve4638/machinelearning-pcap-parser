
class Session:
    def __init__(self):
        self.pkts = []
        self.endstep = False
        self.end = False
    
    def add(self, pkt):
        flags = getflags(pkt)
        self.pkts.append(pkt)

        if self.isendpkt(flags):
            if self.endstep:
                self.end = True
            else:
                self.endstep = True
    
    @classmethod
    def isendpkt(cls, flags):
        if flags["fin"] or flags["rst"]:
            return True
        else:
            return False

def getflags(data):
    layers = data["_source"]["layers"]
    ack = layers["tcp"]["tcp.flags_tree"]["tcp.flags.ack"]
    psh = layers["tcp"]["tcp.flags_tree"]["tcp.flags.push"]
    syn = layers["tcp"]["tcp.flags_tree"]["tcp.flags.syn"]
    fin = layers["tcp"]["tcp.flags_tree"]["tcp.flags.fin"]
    rst = layers["tcp"]["tcp.flags_tree"]["tcp.flags.reset"]
    return {
        "ack" : ack == '1',
        "psh" : psh == '1',
        "syn" : syn == '1',
        "fin" : fin == '1',
        "rst" : rst == '1',
    }

