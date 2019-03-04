SBOX = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)


def byte2array(bytes):
    """Converts bytes to 4 x 4 array
    :param bytes: bytes
    :return: 4 x 4 array
    """
    array = []
    for i, byte in enumerate(bytes):
        if i % 4 == 0:
            array.append([byte])
        else:
            array[i // 4].append(byte)
    return array


def array2hex(array):
    """Converts 4 x 4 array to hex string
    :param array: array
    :return: hex string
    """
    hexstr = ""
    for i in range(4):
        hexstr += ''.join('{:02x}'.format(x) for x in array[i])
    return hexstr


def getKeySchedule(key):
    """Returns key schedule of 44 words
    :param key: 128 bit master key
    :return: key schedule
    """
    key_schedule = byte2array(key)

    # Code here
    sss = "7750f228896eb4561b9cd67497aad0b1"
    hello = sss[0:8]
    w0 = sss[0:8]
    w1 = sss[8:16]
    w2 = sss[16:24]
    w3 = sss[24:32]
    xor_result = int(sss, 16) ^ int(sss, 16)
    #FIRST ROUNDKEY
    #DIVIDE KEY INTO SUBKEYS
    #2.g(w3)
    #3.w4,w5,w6 and w7...
    #BEGIN g(W3)
    w3 = w3[2::] + w3[:2:]
    bin_w3 = str(bin(int(w3,16)))
    # print(bin_w3[2:6])
    print(w3)
    SUBSTITUTE_BYTES(w3)
    arr_first_4 = int(bin_w3[2:6],2)
    arr_last_4 = int(bin_w3[30:],2)
    # print(arr_first_4*arr_last_4)
    # print(SBOX[0])
    #SBOX SHIT NOW
    # print(byte2array((array2hex(w3))))
    # w1 = int(sss,16) ^ int(sss,16)
    # sss = int(key,16)
    # print ('%x' % xor_result)
    # for key in key_schedule:
    # print(w0)
    return key_schedule

def encrypt(plaintext, key_schedule):
    """Encrypts plaintext using key schedule
    :param plaintext: plaintext in hex
    :param key_schedule: key schedule
    :return: ciphertext in hex
    """
    state_array = byte2array(plaintext)

    # Code here


    return array2hex(state_array)


def ADD_ROUND_KEY(state_array, key_array):
    """Performs ADD ROUND KEY
    :param state_array: state array
    :param key_array: key array
    :return: none
    """
    # Code here


def SUBSTITUTE_BYTES(state_array):
    """Performs SUBSTITUTE_BYTES
    :param state_array: state array
    :param key_array: key array
    :return: none
    """
    # Code here
    # sss = "7750f228896eb4561b9cd67497aad0b1"
    # hello = sss[2:4]
    # print(bin(int(hello,16)))
    # print(hex(SBOX[0x20]))
    # intArr = int(state_array,16)
    state_array = "72aad0b1"
    p0 = str(hex(SBOX[int(state_array[0:2],16)]))
    # print("aaa: ", state_array[4:6])
    w = 32
    print("THIS IS OGING IN: ",state_array[0:2])
    pw = SBOX[int(state_array[0:2],16)]
    print(hex((pw)))
    print("SBOX: ",hex(SBOX[w]))
    # print(p0)
    # print(hex(int(state_array[2:4],16)))
    # p1 = str(SBOX[hex(int(state_array[2:4],16))])
    # p1 = str(SBOX[hex()])
    # print(hex(int(state_array[2:4],16)))
    # print(p1)
    p2 = str(hex(SBOX[int(state_array[4:6],16)]))
    p3 = str(hex(SBOX[int(state_array[6:8],16)]))
    # state_array = p0[2:] + p1[2:] + p2[2:] + p3[2:]
    print(state_array)
    # print("This is the state array: ",state_array)
    # print(type(state_array))
    # return state_array


def SHIFT_ROWS(state_array):
    """Performs SHIFT_ROWS
    :param state_array: state array
    :param key_array: key array
    :return: none
    """
    # Code here


key = "7750f228896eb4561b9cd67497aad0b1"
key_schedule = getKeySchedule(bytes.fromhex(key))

plaintext = ["27153a16906ef425d078796f71569cbe",
             "b6f2d9b55d607b9a3e23cb4b9e133a18",
             "1a9d31f65a985ae9dfb6344cc90ec75b",
             "4e90a7cd0d8bce7285161377f0fd6fca"]

ciphertext = []

for msg in plaintext:
    ciphertext.append(encrypt(bytes.fromhex(msg), key_schedule))

# print(ciphertext)
print(key_schedule)
# SUBSTITUTE_BYTES(key_schedule)