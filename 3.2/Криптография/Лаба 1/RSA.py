
def RSA(p, q, message):
    n = p * q                  # Generated free and secret keys
    phi = (p - 1) * (q - 1)
    e = 65537
    d = extended_gcd(e, phi)[1]
    if d < 0: d += phi

    Fkey = {e, n}            # Free key
    Skey = {d, n}              # Secret key
    print(Fkey, Skey)

    m = [(ord(elem)**e % n) for elem in message]  # Encryption of the message
    print(m)

    return [(chr(Exponentiation(elem, d, n))) for elem in m]   # Decrypting a message

def extended_gcd(a, b):
    if a == 0: return b, 0, 1

    rezult, q1, q2 = extended_gcd(b % a, a)
    t = q2 - (b // a) * q1
    s = q1
    return rezult, t, s

def Exponentiation(elem, degree, modulus):
    c = 1
    for _ in range(degree):
        c = (c * elem) % modulus
    return c

p, q = 3347, 2777

message = "hello world 123 !"

m = RSA(p, q, message)

print(m)
