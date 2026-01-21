
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        
        if self.arr[h][0] == key:
            return self.arr[h][1]
        
        for index, element in enumerate(self.arr):
            if element[0] == key:
                return element[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)

        
    
        if self.arr[h]:
            
            if self.arr[h + 1] == None and h + 1 < self.MAX:
                self.arr[h + 1] = (key, val) 
                return
            else:
                for i in range(len(self.arr)):
                    if self.arr[i] == None:
                        self.arr[i] = (key, val)
                        return
    
        self.arr[h] = (key, val)    
        
    def __delitem__(self, key):
        h = self.get_hash(key)

        if self.arr[h][0] == key:
           print("caiu aqui 1")
           self.arr[h] = None

        elif self.arr[h + 1][0] == key:
            print(self.arr[h + 1][0])
            self.arr[h + 1] = None  
        else:
            for i in range(len(self.arr)):
                if self.arr[i][0] == key:
                        self.arr[i] = None
                        return

# data = HashTable()
# data['march 7'] = 90
# data['march 18'] = 700
# data['march 8'] = 80
# data['march 17'] = 90
# data['march 22'] = 700
# data['march 24'] = 80
# print(data.arr)
# data['march 24'] = 500

# print(data['march 18'])
# print(data.arr)
# del data['march 8']
# print(data.arr)

#correct solution, da mais uma estudada nela
class HashTable2:  
    def __init__(self):
        self.MAX = 10 # I am keeping size very low to demonstrate linear probing easily but usually the size should be high
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]
           
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key,val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key,val)
        print(self.arr)
        
    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0,index)]
    
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return # item not found so return. You can also throw exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index]=None
        print(self.arr)

data = HashTable2()
data['march 7'] = 90
data['march 18'] = 700
data['march 8'] = 80
data['march 17'] = 90
data['march 22'] = 700
data['march 24'] = 80
print(data.arr)
data['march 24'] = 500

print(data['march 18'])
print(data.arr)
del data['march 8']
print(data.arr)