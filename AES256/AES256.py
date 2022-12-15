import Crypto.Cipher.AES
import base64


class Cipher_AES:
    # Padding calculation for 16 bit block size.
    pad_pkcs5 = lambda x, y: x + (y - len(x) % y) * chr(y - len(x) % y).encode("utf-8")
    unpad_pkcs5 = lambda x: x[:-ord(x[-1])]

    # initialization of key and initial vector.
    def __init__(self, key=""):
        self.__key = key
        print(len(self.__key))
        self.__iv = "fedcba9876543210"

    def Cipher_MODE_CBC(self):
        self.__x = Crypto.Cipher.AES.new(self.__key.encode("utf-8"), Crypto.Cipher.AES.MODE_CBC,
                                         self.__iv.encode("utf-8"))

    def encrypt(self, text):
        self.Cipher_MODE_CBC()
        cipher_text = b"".join([self.__x.encrypt(i) for i in self.text_verify(text.encode("utf-8"))])
        return base64.b64encode(cipher_text).decode("utf-8").rstrip()

    # Decrypt the provided text with the help of padding.
    def decrypt(self, cipher_text):
        self.Cipher_MODE_CBC()
        cipher_text = base64.decodebytes(cipher_text.encode("utf-8"))
        return self.unpad_method(self.__x.decrypt(cipher_text).decode("utf-8"))

    def text_verify(self, text):
        while len(text) > len(self.__key):
            # print(len(text), len(self.__key))
            text_slice = text[:len(self.__key)]
            text = text[len(self.__key):]
            yield text_slice
        else:
            if len(text) == len(self.__key):
                yield text
            else:
                yield self.pad_method(text)

    def pad_method(self, text):
        return Cipher_AES.pad_pkcs5(text, 16)

    def unpad_method(self, text):
        return Cipher_AES.unpad_pkcs5(text)


key = "w9z$C&E)H@McQfTjWnZr4u7x!A%D*G-J"
# file containing json
f = open('777.json')
text = f.read()
f.close()
cipher_text = Cipher_AES(key).encrypt(text)
print(len(cipher_text))
print(cipher_text)
text = Cipher_AES(key).decrypt(cipher_text)
print(text)