#!/usr/bin/env python
# coding: utf-8

# <h1>Task 1

# In[14]:


def phoneWork(workList):
    phoneBook = {}
    for task in workList:
        if task[0] == "add":
            phoneBook[task[1]] = task[2]
            continue
        if task[0] == "find":
            print(phoneBook.get(task[1], "not found"))
            continue
        if task[0] == "del":
            phoneBook.pop(task[1], "")


# In[15]:


phoneWork([["find","3839442"],["add","123456","me"],["add","0","granny"],["find","0"],["find","123456"],["del","0"],["del","0"],["find","0"]])


# In[ ]:


n = int(input())
tasks = []
for i in range(n):
    tasks.append(input().split(" "))
phoneWork(tasks)


# <h1>Task 2

# In[2]:


class task2():
    p = 1000000007
    x = 263
    m = 0
    hTable = []
    
    def hSum(self, word):
        hSum = 0
        for i in range(len(word)):
            l = word[i]
            hSum += ((ord(l) % self.p) * ((self.x**i) % self.p))
            #print(str(i) + ".1" + str(hSum))
            hSum %= self.p
            #print(str(i) + ".2" + str(hSum))
        hSum %= self.m
        return hSum
    
    def findKey(self, key):
        for i in range(len(self.hTable)):
            if self.hTable[i][0] == key:
                #print('key' + str(key) + ' = ' + str(i))
                return i
        return -1
    
    def findValue(self, keyIndex, value):
        values = self.hTable[keyIndex][1]
        for i in range(len(values)):
            if values[i] == value:
                return i
        return -1
    
    def addWord(self, word):
        wKey = self.hSum(word)
        kIndex = self.findKey(wKey)
        if kIndex < 0:
            self.hTable.append([wKey,[word]])
            return False
        wIndex = self.findValue(kIndex, word)
        if wIndex >= 0:
            return False
        self.hTable[kIndex][1] == self.hTable[kIndex][1].insert(0, word)
        return True
        
    def delWord(self, word):
        wKey = self.hSum(word)
        kIndex = self.findKey(wKey)
        if kIndex < 0:
            return False
        wIndex = self.findValue(kIndex, word)
        if wIndex < 0:
            return False
        self.hTable[kIndex][1].pop(wIndex)
        return True
    
    def findWord(self, word):
        wKey = self.hSum(word)
        kIndex = self.findKey(wKey)
        if kIndex < 0:
            return 'No'
        wIndex = self.findValue(kIndex, word)
        if wIndex < 0:
            return 'No'
        return 'Yes'
    
    def check (self, i):
        result = ''
        kIndex = self.findKey(i)
        if kIndex >= 0:
            result = ' '.join(self.hTable[kIndex][1])
        return result
    
    def run(self, m, tasks):
        self.m = m
        for task in tasks:
            if task[0] == 'add':
                self.addWord(task[1])
            if task[0] == 'del':
                self.delWord(task[1])
            if task[0] == 'find':
                print(self.findWord(task[1]))
            if task[0] == 'check':
                print(self.check(int(task[1])))
            #print(self.hTable)
        return


# In[20]:


def hSum(word, m):
    hSum = 0
    x = 263
    p = 1000000007
    i = 0
    for l in word:
        hSum += ord(l) * (x**i)
        hSum %= p
        i += 1
    hSum %= m
    return hSum

def mk_chain(m, tasks):
    keys = []
    values = []
    for task in tasks:
        t0 = task[0]
        t1 = task[1]
        if t0 == 'check':
            t1 = int(t1)
            if t1 in keys:
                print(' '.join(values[keys.index(t1)]))
        else:
            i = -1
            h = hSum(t1, m)
            if h in keys:
                i = keys.index(h)
            if t0 == 'add':
                if i >= 0:
                    if t1 in values[i]:
                        continue
                    values[i].insert(0, t1)
                else:
                    keys.append(h)
                    values.append([t1])
            if t0 == 'del':
                if i >= 0:
                    if t1 in values[i]:
                        values[i].remove(t1)
                        if len(values[i]) == 0:
                            keys.pop(i)
                            values.pop(i)
            if t0 == 'find':
                if i >= 0:
                    if t1 in values[i]:
                        print('yes')
                        continue
                print('no')
                

def mk_chain2(m, tasks):
    values = [[] for i in range(15)]
    for task in tasks:
        t0 = task[0]
        t1 = task[1]
        if t0 == 'check':
            t1 = int(t1)
            if len(values) >= t1:
                print(' '.join(values[t1]))
        else:
            h = hSum(t1, m)
            if t0 == 'add':
                if t1 not in values[h]:
                    values[h].insert(0, t1)
            if t0 == 'del':
                if t1 in values[h]:
                    values[h].remove(t1)
            if t0 == 'find':
                if t1 in values[h]:
                    print('yes')
                else:
                    print('no')


# In[ ]:


m = int(input())
n = int(input())
values = [[] for i in range(m)]
for t in range(n):
    task = input().split(' ')
    t0 = task[0]
    t1 = task[1]
    if t0 == 'check':
        t1 = int(t1)
        if len(values) >= t1:
            print(' '.join(values[t1]))
    else:
        h = 0
        i = 0
        for l in t1:
            h+= ord(l) * (263**i)
            h %= 1000000007
            i += 1
        h %= m
        if t0 == 'add':
            if t1 not in values[h]:
                values[h].insert(0, t1)
        if t0 == 'del':
            if t1 in values[h]:
                values[h].remove(t1)
        if t0 == 'find':
            if t1 in values[h]:
                print('yes')
            else:
                print('no')


# In[21]:


t2 = task2()
t2.run(5, [["add","world"],["add","HellO"],["check","4"],["find","World"],        ["find","world"],["del","world"],["check","4"],["del","HellO"],        ["add","luck"],["add","GooD"],["check","2"],["del","good"]])
print('-----')
mk_chain2(5, [["add","world"],["add","HellO"],["check","4"],["find","World"],        ["find","world"],["del","world"],["check","4"],["del","HellO"],        ["add","luck"],["add","GooD"],["check","2"],["del","good"]])


# In[4]:


m = int(input())
n = int(input())
tasks = []
for i in range(n):
    tasks.append(input().split(' '))
t2 = task2()
t2.run(m, tasks)


# <h1>Task3

# In[24]:


import random

def find_str(pattern, text):
    p = 31
    x = random.randint(0, p - 1)
    print("p = " + str(p))
    print("x = " + str(x))
    i = 1
    h1 = 0
    h2 = 0
    y = x**(len(pattern) - 1)
    for l in pattern:
        h1 += (ord(l) * x**(len(pattern) - i)) % p
        i += 1
    h1 %= p
    i = 1
    print('h (' + pattern + ') = ' + str(h1))
    for l in text[:len(pattern)]:
        h2 += (ord(l) * x**(len(pattern) - i)) % p
        i += 1
    h2 %= p
    print('h0 (' + text[:len(pattern)] + ') = ' + str(h2))
    if h1 == h2:
        print(0)
    s = 0
    for l in text[len(pattern):]: 
        h2 -= (ord(text[s]) * y)
        #h2 %= p
        h2 *= x
        h2 %= p
        h2 += (ord(l) * x**0)
        h2 %= p
        print('del = ' + text[s])
        print('add = ' + l)
        s += 1
        print('h' + str(s) + ' (' + text[s:s + len(pattern)] + ') = ' + str(h2))
        if h1 == h2:
            print(s)


# In[60]:


def find_str(pattern, text):
    result = ''
    p = 31
    x = 1
    n = len(pattern)
    i = 1
    h1 = 0
    h2 = 0
    y = x**(n - 1)
    for l in pattern:
        h1 += (ord(l) * x**(n - i)) % p
        i += 1
    h1 %= p
    i = 1
    s = 0
    for l in text:
        if i <= n:
            h2 += (ord(l) * x**(n - i)) % p
        else:
            h2 = (h2 - ord(text[s]) * y) % p * x % p + ord(l) * x**0
            s += 1
        h2 %= p
        if i >= n and h1 == h2 and pattern == text[s:s + n]:
            result += (' ' + str(s))
        i += 1
    print(result)


# In[61]:


find_str('aba', 'ababacaba')

