class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, message):
        cryptogram = ''
        for i in range(len(message)):
            if self.alphabet.find(message[i]) != -1:
                sum = self.alphabet.index(message[i]) + (self.alphabet.index(self.key[i % len(self.key)]))
                cryptogram += self.alphabet[sum] if sum < len(self.alphabet) else self.alphabet[sum-len(self.alphabet)]
            else:
                cryptogram += message[i]
        return cryptogram

    def decode(self, cryptogram):
        message = ''
        for i in range(len(cryptogram)):
            if self.alphabet.find(cryptogram[i]) != -1:
                dif = self.alphabet.index(cryptogram[i]) - (self.alphabet.index(self.key[i%len(self.key)]))
                message += self.alphabet[dif] if dif >= 0 else self.alphabet[dif+len(self.alphabet)]
            else:
                message += cryptogram[i]
        return message