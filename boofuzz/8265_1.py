#!/usr/bin/env python3
"""Demo FTP fuzzer as a standalone script."""

from boofuzz import *


def main():
    """
    This example is a very simple FTP fuzzer. It uses no process monitory
    (procmon) and assumes that the FTP server is already running.
    """
    session = Session(target=Target(connection=UDPSocketConnection("127.0.0.1", 320)))
    #session = Session(target=Target(connection=RawL3SocketConnection("127.0.0.1", 320)))

    define_proto(session=session)

    session.fuzz()

        # UDP
'''
        Word(name="Source_Port", default_value=320),
        Word(name="Destination _Port", default_value=320),
        Word(name="Length", default_value=320),
        Checksum(name="UDP_Checksum", length=2),
        Word(name="Source_Port", default_value=320),
'''

def define_proto(session):
    signaling = Request("signaling", children=(
        BitField(name="Fixed", width=1),
        BitField(name="TransportSpecific", width=3, default_value=0b100, fuzzable=False),
        BitField(name="MessageType", width=4, default_value=12, fuzzable=False),
        BitField(name="Reserved_1", width=4, fuzzable=False),
        BitField(name="VersionPTP", width=4, default_value=2, fuzzable=False),

        Word(name="Message_Length", default_value=19),
        Byte(name="SubdomainNumber", default_value=0),
        Byte(name="Reserved_2"),

        BitField(name="PTP_ALTERNATE_MASTER", width=1),
        BitField(name="PTP_TWO_STEP", width=1, fuzzable=False),
        BitField(name="PTP_UNICAST", width=1, default_value=1, fuzzable=False),
        BitField(name="VOID_2", width=2, fuzzable=False),
        BitField(name="PTP_profile_Specific_1", width=1),
        BitField(name="PTP_profile_Specific_2", width=1),
        BitField(name="PTP_SECURITY", width=1, default_value=0),

        BitField(name="PTP_LI_61", width=1),
        BitField(name="PTP_LI_59", width=1),
        BitField(name="PTP_UTC_REASONABLE", width=1),
        BitField(name="PTP_TIMESCALE", width=1),
        BitField(name="TIME_TRACEABLE", width=1),
        BitField(name="FREQUENCY_TRACEABLE", width=1),
        BitField(name="VOID_1", width=2),

        Bytes(name="Correction", size=6),
        Bytes(name="CorrectionSubNs", size=2),
        Bytes(name="Reserved_3", size=4),
        Bytes(name="ClockIdentity", default_value=b"\x00\x25\x9e\x98\x00\x00\x00\x02", size=8),
        Bytes(name="SourcePortID", default_value=b"\x00\x01", size=2),
        Bytes(name="SequenceID", default_value=b"\x00", size=2),
        Bytes(name="Control", default_value=b"\x01", size=1),
        Bytes(name="LogMessagePeriod", default_value=b"\x7F", size=1),

        Byte(name="Reserved_4"),
        Bytes(name="Message Interval", default_value=b"\xff\xff\xff\xff", size=4),
        Bytes(name="Organization ID", default_value=b"\x00\x00\x01", size=3),
        Byte(name="Reserved_5"),
        Bytes(name="Target Port Identity", default_value=b"\x00\x00\x02", size=10),
    ))
    session.connect(signaling)


if __name__ == "__main__":
    main()
