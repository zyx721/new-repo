class Hash_map:
    def __init__(self):
        self.max=100
        self.arr=[[] for i in range(self.max)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h % self.max
    def __setitem__(self,key,val):
        h=self.get_hash(key)
        self.arr[h] = val
    def __getitem__(self,key):
        return self.arr[self.get_hash(key)]
    def __delitem__(self, key):
        self.arr[self.get_hash(key)] = None

h = Hash_map()
h['ziad']=13
h['moh']=19
h['iad']=15
print(h.arr)