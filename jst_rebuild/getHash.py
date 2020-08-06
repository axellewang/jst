


class getHash:

    def convert_n_bytes(self, n, b):
        bits = b * 8
        return (n + 2 ** (bits - 1)) % 2 ** bits - 2 ** (bits - 1)

    def convert_4_bytes(self, n):
        return self.convert_n_bytes(n, 4)

    @classmethod
    def getHashCode(cls, value):
        h = 0
        n = len(value)
        for i, c in enumerate(value):
            h = h + ord(c) * 31 ** (n - 1 - i)
        hashcode = cls().convert_4_bytes(h)
      #  print(hashcode)
        return hashcode




if __name__ == '__main__':
    test = getHash()
    test.getHashCode('JJ1090')
   # test.T_BILL_GP_RESERVATION_Modulus(number=1000000)
