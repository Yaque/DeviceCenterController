import struct


def byte2data(bytes_data):
    return struct.unpack('i', bytes_data)[0]

def data2byte(data):
    return struct.pack('i', data)


def package_data_2_security(bytes_data):
    new_data = bytes()
    for i in range(1, len(bytes_data)):
        new_data += bytes_data[i:i+1]
    new_data += bytes_data[0:1]
    return new_data


def unpackage_data_2_security(bytes_data):
    l = len(bytes_data)
    new_data = bytes_data[l-1:l]
    for i in range(0, l-1):
        new_data += bytes_data[i : i+1]
    return new_data