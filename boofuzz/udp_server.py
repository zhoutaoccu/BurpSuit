import socket
from time import strftime, localtime

HOST = '127.0.0.1'
PORT = 320
BUFSIZE = 1024
ADDR = (HOST, PORT)

udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_s.bind(ADDR)

while True:
    #print("Wait for messages.....")
    data, addr = udp_s.recvfrom(BUFSIZE)

    print("...received from and returned to: ", addr)

upd_s.close()

'''
    udp_s.sendto(
        str(
            '[%s] %s\n' % (strftime("%Y-%m-%d %H:%M:%S", localtime()), str(data))
        ).encode('gbk'), addr)
'''