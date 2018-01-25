# -*-coding:utf8 -*-
__author__ = "陈子昂"
__datetime__ = "2018/1/21 19:55"

#已知一段二进制数据为TCP协议头部信息，写程序解析包含的各字段内容。
# TCP Header格式如下 http://www.rfc-editor.org/rfc/rfc793.txt （3.1 Header Format）

datagrams = b'010101010110101111011111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001101111111110000000000000110101010101111'

def parse_datagrams(datagrams):
    SourcePort = datagrams[0:16]
    DestinationPort = datagrams[16:32]
    SequenceNumber = datagrams[32:64]
    AcknowledgmentNumber =  datagrams[64:96]
    DataOffse = datagrams[96:100]
    Reserved = datagrams[100:106]
    ControlBits = datagrams[106:112]
    Window = datagrams[112:128]
    Checksum = datagrams[128:144]
    UrgentPointer = datagrams[144:160]
    Kind = datagrams[160:164]
    Options = None

    if Kind == b'00000010':
        Option = datagrams[164:168]

    if Options:
        MaximumSegmentSizeOptionData = datagrams[168:184]

    # 时间关系，没做完

    print(SourcePort,DestinationPort,SequenceNumber,AcknowledgmentNumber)

parse_datagrams(datagrams)


