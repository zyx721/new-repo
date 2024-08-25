a = ["a","b","c","d","e"]
itr = iter(a)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
itr = reversed(a)
print("\n rev \n")
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","CNN","ABC","ESPN","BN_SPORT"]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index +=1
        if self.index == len(self.channels):
            print("hey")
            raise StopIteration
        return self.channels[self.index]
r = RemoteControl()
itr = iter(r)
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))


