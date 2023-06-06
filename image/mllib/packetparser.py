from scapy.all import *

def packet_get_body(packet_bytes):
    layer = IP(packet_bytes).getlayer(Raw)  # Raw 레이어를 가져옴
    if layer:
        body = layer.load  # 본문 추출
        return body
    else:
        return bytes([])
    
    
def packet_get_port(packet_bytes):
    ip = IP(packet_bytes)  # Raw 레이어를 가져옴
    