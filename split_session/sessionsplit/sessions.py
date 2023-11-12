from .session import getflags, Session

class Sessions:
    def __init__(self):
        self.ordered = []
        self.sessions = {}

    def addpkt(self, key, pkt):
        flags = getflags(pkt)
        if self.isbeginpkt(flags):
            if key in self.sessions:
                del self.sessions[key]

        if key not in self.sessions:
            newsession = Session()
            self.sessions[key] = newsession
            self.ordered.append(newsession)

        self.sessions[key].add(pkt)
        
        if self.sessions[key].end:
            del self.sessions[key]
            print("END")
    
    @classmethod
    def isbeginpkt(cls, flags):
        if flags["syn"] and not flags["ack"]:
            return True 
        else:
            return False
        
    @classmethod
    def isendpkt(cls, flags):
        if flags["fin"] or flags["rst"]:
            return True
        else:
            return False
    
    def getsessions(self):
        return self.ordered
