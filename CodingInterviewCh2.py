from random import randint


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:

    def __init__(self,values = None):
        self.head = None
        self.tail = None
        if values:
            for i in range(len(values)):
                self.add(values[i])

    def add(self,value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            temp = Node(value)
            self.tail.next = temp
            self.tail = temp

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

    def __str__(self):
        current = self.head
        l = list()
        while current is not None:
            l.append(str(current.value))
            current = current.next
        return " ".join(l)

#with extra space
def remove_dups(llist : LinkedList):
    if llist.head is None:
        return llist

    current = llist.head.next
    prev = llist.head
    val_dict = set()
    val_dict.add(prev.value)
    while current is not None:
        if current.value in val_dict:
            prev.next = current.next
            current=current.next
        else:
            val_dict.add(current.value)
            prev = current
            current = current.next
    return llist

#without space
def remove_dups2(llist : LinkedList):
    current = llist.head
    if current is None:
        return llist
    while current is not None:
        runner = current
        check = current.value
        while runner.next is not None:
            if runner.next.value == check:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return llist


def kth_to_last(llist : LinkedList, k: int):
    kth = llist.head
    last = kth
    for i in range(k):
        last = last.next
    while last.next is not None:
        kth = kth.next
        last = last.next
    return kth.value

def delete_middle_node(middle : Node):
    middle.value = middle.next
    middle.next = middle.next.next

def partition(llist: LinkedList, num : int):
    current = llist.head
    fast = current.next
    if current is None:
        return llist
    while fast is not None:
        if fast.value < num:
            current.next = fast.next
            fast.next = llist.head
            llist.head = fast
            fast = current.next
        else:
            current = fast
            fast = current.next

#tek loopta yap
def sum_lists(llist1 : LinkedList ,llist2: LinkedList):
    current1 = llist1.head
    current2 = llist2.head
    sumlist = LinkedList()
    remainder = 0
    while current1 is not None or current2 is not None:
        subsum = 0
        if current1 is not None:
            subsum+=current1.value
            current1 = current1.next
        if current2 is not None:
            subsum+=current2.value
            current2 = current2.next
        subsum+=remainder
        remainder = 0
        subsum = str(subsum)
        if len(subsum)>1:
            remainder = 1
        sumlist.add(subsum[-1])
    if remainder==1:
        sumlist.add(remainder)
    return sumlist

def is_palindrome(llist: LinkedList):
    current = llist.head
    length = 0
    if not current:
        return False
    while current:
        length+=1
        current = current.next
    if length%2 == 0:
        odd=False
    else:
        odd = True
    current = llist.head
    numlist = list()
    while len(numlist)<length//2:
        numlist.append(current.value)
        current = current.next
    if odd:
        current = current.next
    while current:
        if numlist.pop()!=current.value:
            return False
        current = current.next
    return True

# naive approach, O(N*M)
def intersection(llist1: LinkedList, llist2: LinkedList):
    current1 = llist1.head
    while current1:
        current2 = llist2.head
        while current2:
            if current1==current2:
                return True
            else:
                current2 = current2.next
    return False

#faster approach, O(N+M)
def intersection_faster(llist1: LinkedList,llist2: LinkedList):
    if llist1.tail != llist2.tail:
        return False
    length1, length2 = (0,0)
    current = llist1.head
    while current:
        length1+=1
        current = current.next
    current = llist2.head
    while current:
        length2+=1
    if length1 < length2:
        short,long = (llist1.head,llist2.head)
        diff = llist2-llist1
    else:
        short,long = (llist2.head,llist1.head)
        diff = length2-length1
    for i in range(diff):
        long = long.next
    while short and long:
        if short==long:
            return True
        short,long = (short.next,long.next)
    return False

#using additional space
def loop_detection(llist1: LinkedList):
    node_set = set()
    current = llist1.head
    while current:
        if current in node_set:
            return current
        else:
            node_set.add(current)

#faster algorithm with runner approach
def loop_detection2(llist1: LinkedList):
    ptr1 = llist1.head
    ptr2 = llist1.head
    while ptr2 and ptr2.next:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
        if ptr1 == ptr2:
            break
    if ptr2 is None or ptr2.next is None:
        return None
    ptr1 = llist1.head
    while ptr1!=ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1
