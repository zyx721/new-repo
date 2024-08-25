class Solution(object):
    def intToRoman(self, num):
        roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        if num in roman_numerals:
            return roman_numerals[num]
        else:
            s = ''
            for value , bod in sorted(roman_numerals.items(),reverse = True):
                while value<=num:
                    s+= roman_numerals[value]
                    num -= value
            return s

s = Solution()
print(s.intToRoman(19))  # Output: 'XCV'
