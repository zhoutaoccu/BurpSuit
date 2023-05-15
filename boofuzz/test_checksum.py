#!/usr/bin/env python3
"""Demo FTP fuzzer as a standalone script."""

from boofuzz import *
from boofuzz import helpers
import socket

def ipv4_length(s):
    return len(s) + 20

def recordlength(s):
    return len(s)

def ip_str_to_bytes(ip):
    """Convert an IP string to a four-byte bytes.

    :param ip: IP address string, e.g. '127.0.0.1'

    :return 4-byte representation of ip, e.g. b'\x7F\x00\x00\x01'
    :rtype bytes

    :raises ValueError if ip is not a legal IP address.
    """
    try:
        return socket.inet_aton(ip)
    except socket.error:
        raise ValueError("Illegal IP address passed to socket.inet_aton: {0}".format(ip))

IP_SRC = '192.168.43.123'
IP_DST = '192.168.43.131'

def main():
    """
    This example is a very simple FTP fuzzer. It uses no process monitory
    (procmon) and assumes that the FTP server is already running.
    """
    #session = Session(target=Target(connection=UDPSocketConnection("127.0.0.1", 320)))
    

    

    s_initialize("udp_with_checksum")
    if s_block_start("ipv4_head"):
        s_dword(0x4500, name="IPv4")
        if s_block_start("ipv4_len"):
            s_size("udp_data", length=2, fuzzable=False)
        s_block_end()

        s_dword(0x02d0, name="id")
        s_dword(0x4000, name="flag")
        s_byte(0x40, name="time_live")
        s_byte(0x11, name="Protocol")

        s_checksum(
                block_name="ipv4_head",
                algorithm="crc32",
                length=2,
                fuzzable=False,
            )

        s_dword(ip_str_to_bytes(IP_SRC), name="IPv4 Src Block")
        s_dword(ip_str_to_bytes(IP_DST), name="IPv4 Dst Block")
    s_block_end()
    

    if s_block_start("elements"):
        s_word(320, name="Source_Port")
        s_word(320, name="Dest_Port")
        if s_block_start("udp_len"):
            s_size("udp_data", length=2, fuzzable=False)
        s_block_end()
        #s_word(0, name="UDP_Checksum")
        s_checksum(
            block_name="elements",
            algorithm="udp",
            length=2,
            fuzzable=False,
            ipv4_src_block_name="IPv4 Src Block",
            ipv4_dst_block_name="IPv4 Dst Block",
        )
        if s_block_start("udp_data"):
            s_string("aaaaaaaaaaaaaaaaaaaaff")
        s_block_end()
        
    s_block_end()

    session = Session(target=Target(connection=RawL3SocketConnection("127.0.0.1", 320)))
    session.connect(s_get("udp_with_checksum"))

    session.fuzz()

if __name__ == "__main__":
    main()
