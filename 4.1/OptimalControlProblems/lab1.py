#Quest 1

def Caesar_Encr(message, key):      #Caesar Ecryption
    return ''.join([chr((ord(symb) - ord('a') + key) % (ord('z') - ord('a') + 1) + ord('a')) for symb in message])

def Caesar_Dencr(message, key):     #Caesar Decryption
    return ''.join([chr((ord(symb) - ord('a') - key) % (ord('z') - ord('a') + 1) + ord('a')) for symb in message])

def Vigener_Encr(message, key):     #Vigener Ecryption
    return ''.join([chr((ord(message[i]) - 2 * ord('a') + ord(key[i % len(key)])) % (ord('z') - ord('a') + 1) + ord('a')) for i in range(len(message))]).upper()

def Vigener_Dencr(message, key):    #Vigener Decryption
    return ''.join([chr((ord(message[i])  + (ord('z') - ord('a') + 1) - ord(key[i % len(key)])) % (ord('z') - ord('a') + 1) + ord('a')) for i in range(len(message))]).upper()

#Quest 2

