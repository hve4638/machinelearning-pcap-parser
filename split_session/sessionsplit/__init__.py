from .session import Session, getflags
from .sessions import Sessions

def orderkey(srcip, srcport, dstip, dstport):
    reverse:bool = False
    if srcip == dstip and srcport > dstport:
        reverse = True
    elif srcip > dstip:
        reverse = True
    
    if reverse:
        return (srcip, srcport, dstip, dstport)
    else:
        return (dstip, dstport, srcip, srcport)

def getaddr(data):
    layers = data["_source"]["layers"]
    try:
        srcport = layers["tcp"]["tcp.srcport"]
        dstport = layers["tcp"]["tcp.dstport"]
        srcip = layers["ip"]["ip.src_host"]
        dstip = layers["ip"]["ip.dst_host"]
    except KeyError:
        return None
    
    return (srcip, srcport, dstip, dstport)