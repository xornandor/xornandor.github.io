pesan = input("Masukkan pesan (hanya teks): ")
geser = int(input("Masukkan pergeseran, (-) ke kiri dan (+) ke kanan: "))
type = input("encrypt (ketik 'enc') atau dec (ketik 'dec'): ")

def caesar_cipher(pesan, geser, type="enc"):

    pesan = pesan.lower()
    result = []

    if type == "enc":
        for a in range(len(pesan)):
            result.append(chr((((ord(pesan[a]) - 97) + geser) % 26) + 97))
    
    if type == "dec":
        for a in range(len(pesan)):
            result.append(chr((((ord(pesan[a]) - 97) - geser) % 26) + 97))
    
    return ''.join(result)

print(caesar_cipher(pesan, geser, type))