import random
class Solution:
    def test(self, s):
        if s[0] != 'a' or s[-1] != 'b':
            print('No, it is not in the language')
            return False
        num_a = self.number_of_char(s, 'a')
        num_b = self.number_of_char(s, 'b')
        valid_string = ''
        for _ in range(num_a):
            valid_string += 'a'
        for _ in range(num_b):
            valid_string += 'b'
        if valid_string == s:
            print('Yes, it is in the language')
            return True
        else:
            print('No, it is not in the language')
            return False
    def number_of_char(self, s, c):
        nb = 0
        for i in s:
            if i == c:
                nb += 1
        return nb
    def generate_strings(self, n):
        l = []
        for _ in range(n+1):
            s = ''
            while s in l:
                length = random.choices(range(2, n+2))[0]
                a_count = random.choices(range(1, length), k=1)[0]
                b_count = length - a_count
                for _ in range(a_count):
                    s += 'a'
                for _ in range(b_count):
                    s += 'b'
                if s in l :
                    s=''

            l.append(s)
        l.pop(0)
        return l
s = Solution()
m = int(input('Enter number of words: '))
print(s.generate_strings(m))
n = input('Enter a word: ')
print(s.test(n))
