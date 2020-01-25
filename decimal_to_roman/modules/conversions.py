class ConvertNumbers:

    global arabic
    arabic = [1000, 900, 500, 400,100, 90, 50, 40, 10, 9, 5, 4,1]

    global roman
    roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL","X", "IX", "V", "IV","I"]

    def decimalToRoman(n):
        '''
        This method will transform the decimal number given
        into a roman number.
        It prints an error if the given value is not a number.
        '''
        if type(n) not in [int, float]:
            raise ValueError("\n[ERROR] Not a number...")
        if n < 0:
            n = abs(n)
        r = ""
        i = 0
        while n > 0:
            for _ in range(n // arabic[i]):
                r += roman[i]
                n -= arabic[i]
            i += 1
        return r

    def romanToDecimal(r):
        '''
        This method will transform the roman string given
        into a decimal number.
        If the roman string is not valid, the function will return 0.
        '''
        def isValidRoman(r):
            if r.count('I') > 3 or r.count('X') > 3 or r.count('C') > 3 \
            or r.count('V') > 1 or r.count('L') > 1 or r.count('D') > 1:
                return False
            else:
                return True

        if not isValidRoman(r):
            return 0

        n = 0
        # Manage complex numbers
        for i in range(0, len(r) - 1):
            if i % 2 == 0:
                key = r[:2]
                j = 0
                for elem in roman:
                    if key == elem:
                        n += arabic[j]
                        r = r.replace(key, '')
                    j += 1
 
        # Manage single numbers
        for key in r:
            i = 0
            for elem in roman:
                if key == elem:
                    n += arabic[i]
                    r.replace(key, '')
                i += 1
        return n