
def parsePackets_recursive(binStr):
    thisPacket = {'bit_length': 0}

    # Determine type of 1st packet in string
    thisPacket['packetVersion'] = int(binStr[0:3], 2)
    binStr = binStr[3:]
    thisPacket['bit_length'] += 3

    thisPacket['type_ID'] = int(binStr[0:3], 2)
    binStr = binStr[3:]
    thisPacket['bit_length'] += 3
    
    if thisPacket['type_ID'] != 4:  # If operator packet
        thisPacket['lenght_ID'] = int(binStr[0], 2)
        binStr = binStr[1:]
        thisPacket['bit_length'] += 1

        thisPacket['sub_packets'] = []

        if thisPacket['lenght_ID'] == 0:
            thisPacket['sub_length'] = int(binStr[0:15], 2)
            binStr = binStr[15:]
            thisPacket['bit_length'] += 15

            subPktBitSum = []

            while sum(subPktBitSum) < thisPacket['sub_length']:
                subPack = parsePackets_recursive(binStr)
                thisPacket['sub_packets'].append(subPack)

                binStr = binStr[subPack['bit_length']:]
                thisPacket['bit_length'] += subPack['bit_length']
                subPktBitSum.append(subPack['bit_length'])

        else:   # If length_ID == 1
            thisPacket['sub_length'] = int(binStr[0:11], 2)
            binStr = binStr[11:]
            thisPacket['bit_length'] += 11

            while len(thisPacket['sub_packets']) < thisPacket['sub_length']:
                subPack = parsePackets_recursive(binStr)
                thisPacket['sub_packets'].append(subPack)
                binStr = binStr[subPack['bit_length']:]
                thisPacket['bit_length'] += subPack['bit_length']
    
    else:   # If literal value
        valueBits = ''
        while True:
            groupBit = int(binStr[0], 2)
            valueBits += binStr[1:5]
            binStr = binStr[5:]
            thisPacket['bit_length'] += 5

            if groupBit == 0:
                thisPacket['literalValue'] = int(valueBits, 2)
                break

    return thisPacket


def findVersionSum_recursive(packetDict):
    versionSum = packetDict['packetVersion']
    if 'sub_packets' in packetDict.keys():
        for packet in packetDict['sub_packets']:
            versionSum += findVersionSum_recursive(packet)
    
    return versionSum


def findPacketValue_recursive(thisPacket):
    if 'sub_packets' in thisPacket.keys():
        for packet in thisPacket['sub_packets']:
            if 'literalValue' not in packet.keys():
                findPacketValue_recursive(packet)
    
    if thisPacket['type_ID'] == 0:
        thisPacket['literalValue'] = 0
        for packet in thisPacket['sub_packets']:
            thisPacket['literalValue'] += packet['literalValue']
    if thisPacket['type_ID'] == 1:
        thisPacket['literalValue'] = 1
        for packet in thisPacket['sub_packets']:
            thisPacket['literalValue'] *= packet['literalValue']
    if thisPacket['type_ID'] == 2:
        thisPacket['literalValue'] = thisPacket['sub_packets'][0]['literalValue']
        for packet in thisPacket['sub_packets']:
            if packet['literalValue'] < thisPacket['literalValue']:
                thisPacket['literalValue'] = packet['literalValue']
    if thisPacket['type_ID'] == 3:
        thisPacket['literalValue'] = thisPacket['sub_packets'][0]['literalValue']
        for packet in thisPacket['sub_packets']:
            if packet['literalValue'] > thisPacket['literalValue']:
                thisPacket['literalValue'] = packet['literalValue']
    if thisPacket['type_ID'] == 5:
        if thisPacket['sub_packets'][0]['literalValue'] > thisPacket['sub_packets'][1]['literalValue']:
            thisPacket['literalValue'] = 1
        else:
            thisPacket['literalValue'] = 0
    if thisPacket['type_ID'] == 6:
        if thisPacket['sub_packets'][0]['literalValue'] < thisPacket['sub_packets'][1]['literalValue']:
            thisPacket['literalValue'] = 1
        else:
            thisPacket['literalValue'] = 0
    if thisPacket['type_ID'] == 7:
        if thisPacket['sub_packets'][0]['literalValue'] == thisPacket['sub_packets'][1]['literalValue']:
            thisPacket['literalValue'] = 1
        else:
            thisPacket['literalValue'] = 0


# --- Start Here ---
with open('input.txt') as inputFile:
    hexStr = inputFile.read()

b_size = len(hexStr) * 4
binStr = (bin(int(hexStr, 16))[2:]).zfill(b_size)

# --- Part One ---
packetDict = parsePackets_recursive(binStr)
versionSum = findVersionSum_recursive(packetDict)
print('Version sum = ', versionSum)

# --- Part Two ---
findPacketValue_recursive(packetDict)
print('Packet value = ', packetDict['literalValue'])


# Examples

# D2FE28
# 110 100 101111111000101000
# VVV TTT AAAAABBBBBCCCCC
#   6   4  0111 1110 0101 = 2021


# 38006F45291200
# 001 110 0 000000000011011 110 100 01010       010 100 1000100100 0000000
# VVV TTT I LLLLLLLLLLLLLLL VVV TTT AAAAA       VVV TTT AAAAABBBBB
#   1   6                27   6   4  1010 = 10    2   4  0001 0100 = 20


# EE00D40C823060
# 111 011 1 00000000011 010 100 00001       100 100 00010       001 100 00011 00000
# VVV TTT I LLLLLLLLLLL VVV TTT AAAAA       VVV TTT AAAAA       VVV TTT AAAAA
#   7   3             3   2   4  0001 = 1     4   4  0010 = 2     1   4  0011 = 3
# AAAAAAAAAAAAAAAAAAAAA BBBBBBBBBBBBB       CCCCCCCCCCCCC       DDDDDDDDDDDDD


# 8A004A801A8002F478
# 100 010 1 00000000001 001 010 1 00000000001 101 010 0 000000000001011 110 100 01111 000
# VVV TTT I LLLLLLLLLLL VVV TTT I LLLLLLLLLLL VVV TTT I LLLLLLLLLLLLLLL VVV TTT AAAAA
#   4   2             1   1   2             1   5   2                11   6   4  1111 = 15
# AAAAAAAAAAAAAAAAAAAAA BBBBBBBBBBBBBBBBBBBBB CCCCCCCCCCCCCCCCCCCCCCCCC DDDDDDDDDDDDD
# represents an operator packet (version 4)
# which contains an operator packet (version 1)
# which contains an operator packet (version 5)
# which contains a literal value (version 6); this packet has a version sum of 16.


# 620080001611562C8802118E34
# 011 000 1 00000000010 000 000 0 000000000010110 000 100 01010       101 100 01011       001 000 1 00000000010 000 100 01100       011 100 01101 00
# VVV TTT I LLLLLLLLLLL VVV TTT I LLLLLLLLLLLLLLL VVV TTT AAAAA       VVV TTT AAAAA       VVV TTT I LLLLLLLLLLL VVV TTT AAAAA       VVV TTT AAAAA
#   3   0             2   0   0                22   0   4  1010 = 10    5   4  1011 = 11    1   0             2   0   4  1100 = 12    3   4  1101 = 13
# AAAAAAAAAAAAAAAAAAAAA BBBBBBBBBBBBBBBBBBBBBBBBB CCCCCCCCCCCCC       DDDDDDDDDDDDD       EEEEEEEEEEEEEEEEEEEEE FFFFFFFFFFFFF       GGGGGGGGGGGGG
# represents an operator packet (version 3) which contains two sub-packets;
# each sub-packet is an operator packet that contains two literal values. This packet has a version sum of 12


# C0015000016115A2E0802F182340
# 110 000 0 000000001010100 000 000 0 000000000010110 000 100 01010       110 100 01011       100 000 1 00000000010 111 100 01100       000 100 01101       000000
# VVV TTT I LLLLLLLLLLLLLLL VVV TTT I LLLLLLLLLLLLLLL VVV TTT AAAAA       VVV TTT AAAAA       VVV TTT I LLLLLLLLLLL VVV TTT AAAAA       VVV TTT AAAAA
#   6   0                84   0   0                22   0   4  1010 = 10    6   4  1011 = 11    4   0             2   7   4  1100 = 12    0   4  1101 = 13
# AAAAAAAAAAAAAAAAAAAAAAAAA BBBBBBBBBBBBBBBBBBBBBBBBB CCCCCCCCCCCCC       DDDDDDDDDDDDD       EEEEEEEEEEEEEEEEEEEEE FFFFFFFFFFFFF       GGGGGGGGGGGGG
# same structure as the previous example, but the outermost packet uses a different length type ID.
# This packet has a version sum of 23.


# A0016C880162017C3686B18A3D4780
# 101 000 0 000000001011011 001 000 1 00000000001 011 000 1 00000000101 111 100 00110       110 100 00110       101 100 01100       010 100 01111       010 100 01111       0000000
# VVV TTT I LLLLLLLLLLLLLLL VVV TTT I LLLLLLLLLLL VVV TTT I LLLLLLLLLLL VVV TTT AAAAA       VVV TTT AAAAA       VVV TTT AAAAA       VVV TTT AAAAA       VVV TTT AAAAA       
#   5   0                91   1   0             1   3   0             5   7   4  0110 = 6     6   4  0110 = 6     5   4  1100 = 12    2   4  1111 = 15    2   4  1111 = 15
# AAAAAAAAAAAAAAAAAAAAAAAAA BBBBBBBBBBBBBBBBBBBBB CCCCCCCCCCCCCCCCCCCCC DDDDDDDDDDDDD       EEEEEEEEEEEEE       FFFFFFFFFFFFF       GGGGGGGGGGGGG       GGGGGGGGGGGGG
# an operator packet that contains an operator packet that contains an operator packet
# that contains five literal values; it has a version sum of 31





# C200B40A82 finds the sum of 1 and 2, resulting in the value 3.
# 04005AC33890 finds the product of 6 and 9, resulting in the value 54.
# 880086C3E88112 finds the minimum of 7, 8, and 9, resulting in the value 7.
# CE00C43D881120 finds the maximum of 7, 8, and 9, resulting in the value 9.
# D8005AC2A8F0 produces 1, because 5 is less than 15.
# F600BC2D8F produces 0, because 5 is not greater than 15.
# 9C005AC2F8F0 produces 0, because 5 is not equal to 15.
# 9C0141080250320F1802104A08 produces 1, because 1 + 3 = 2 * 2.