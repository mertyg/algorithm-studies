class TripleStack:
    def __init__(self,size):
        self.array = [0 for i in range(3*size)]
        self.lengths = [0,0,0]
        self.size = size
    def push(self,item, stack):
        current_pos = self.lengths[stack-1]
        self.array[(stack-1)*self.size+current_pos]=item
        self.lengths[stack-1]+=1
    def pop(self,stack):
        self.lengths[stack-1]-=1
    def peek(self,stack):
        current_pos = self.lengths[stack-1]-1
        return self.array[(stack-1)*self.size+current_pos]
    def isEmpty(self,stack):
        if self.lengths[stack-1]==0:
            return True
        else:
            return False


class MinStack:
    def __init__(self):
        self.array = list()
        self.size = 0
        self.mins = list()
    def push(self,item):
        self.array.append(item)
        self.size+=1
        if self.mins:
            self.mins.append(min(item,self.mins[-1]))
        else:
            self.mins.append(item)
    def pop(self):
        self.size-=1
        self.array.pop()
        self.mins.pop()
    def peek(self):
        return self.array[self.size-1]
    def min(self):
        return self.mins[self.size-1]



class StackWithCapacity:
    def __init__(self, cap):
        self.cap = cap
        self.array = list()
        self.size = 0
    def push(self,item):
        if self.is_full():
            raise Exception("Stack Full")
        self.array.append(item)
        self.size+=1
    def is_full(self):
        return self.size == self.cap
    def peek(self):
        return self.array[self.size-1]
    def pop(self):
        self.size-=1
        self.array.pop()

class SetOfStacks:
    def __init__(self,cap):
        self.cap = cap
        self.stacks = list()
        self.size = 0
    def push(self,item):
        current_stack = self.stacks[self.size-1]
        if current_stack.is_full():
            self.stacks.append(StackWithCapacity(self.cap))
            self.size+=1
            self.stacks[self.size-1].push(item)
        else:
            self.stacks[self.size-1].push(item)
    def peek(self):
        current_stack = self.size-1
        return self.stacks[current_stack].peek()
    def pop(self):
        current_stack = self.size-1
        self.stacks[current_stack].pop()

class QueueWithStacks:
    def __init__(self, cap = 15):
        self.main = StackWithCapacity(cap)
        self.helper = StackWithCapacity(cap)
        self.size = 0
    def add(self,item):
        self.helper.push(item)
        self.size+=1
    def peek(self):
        if self.main.size == 0 :
            while self.helper.size!=0:
                self.main.push(self.helper.peek())
                self.helper.pop()
        return self.main.peek()
    def remove(self):
        if self.main.size == 0 :
            while self.helper.size!=0:
                self.main.push(self.helper.peek())
                self.helper.pop()
        self.main.pop()


class SortedStack:
    def __init__(self,cap=15):
        self.main = StackWithCapacity(cap)
        self.helper = StackWithCapacity(cap)
        self.size = 0
    def push(self,item):
        if self.main.size==0 or item < self.main.peek():
            self.main.push(item)
        else:
            while (self.main.size!=0) and item>self.main.peek():
                self.helper.push(self.main.peek())
                self.main.pop()
            self.main.push(item)
            while self.helper.size!=0:
                self.main.push(self.helper.peek())
                self.helper.pop()
    def pop(self):
        self.main.pop()
    def peek(self):
        return self.main.peek()

