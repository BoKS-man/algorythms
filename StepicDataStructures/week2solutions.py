#!/usr/bin/env python
# coding: utf-8

# <h1>Task 1

# In[24]:


class forest:
    swap_log = []
    tree = []
    
    def parent(self, i):
        return int((i-1)/2)

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def swap(self, i1, i2):
        #print('swap ' + str(i1) + ' and ' + str(i2))
        self.swap_log.append([i1, i2])
        i = self.tree[i1]
        self.tree[i1] = self.tree[i2]
        self.tree[i2] = i

    def min_sift_down(self, i):
        #print('sift_down: ' + str(i))
        min_index = i
        l = self.left_child(i)
        if l < len(self.tree) and self.tree[l] < self.tree[min_index]:
            min_index = l
        z = self.right_child(i)
        if z < len(self.tree) and self.tree[z] < self.tree[min_index]:
            min_index = z
        if i != min_index:
            self.swap(i, min_index)
            self.min_sift_down(min_index)

    def log_make_heap(self, n, tree):
        self.swap_log = []
        self.tree = tree
        i = int(n/2)-1
        while i >= 0:
            #print(i)
            self.min_sift_down(i)
            i -= 1
        print(len(self.swap_log))
        for l in self.swap_log:
            print(str(l[0]) + ' ' + str(l[1]))


# In[27]:


a = forest()
a.log_make_heap(5, [5,4,3,2,1])
#3,[[1,4],[0,1],[1,3]]
a.log_make_heap(5, [1,2,3,4,5])
#0
a.log_make_heap(6, [0,1,2,3,4,5])
#0
a.log_make_heap(6, [7,6,5,4,3,2])
#4,[[2,5],[1,4],[0,2],[2,5]]


# In[9]:


n = int(input())
heap = [int(i) for i in input().split(' ')]
a = forest()
a.log_make_heap(n, heap)


# <h1>Task 2

# In[25]:


class forest2(forest):
    
    def min_sift_down(self, i):
        #print('sift_down: ' + str(i))
        min_index = i
        l = self.left_child(i)
        if l < len(self.tree) and        self.tree[l][1] <= self.tree[min_index][1]:
            min_index = l
        r = self.right_child(i)
        if r < len(self.tree) and        ((self.tree[r][1] <= self.tree[min_index][1] and         self.tree[r][0] < self.tree[min_index][0]) or        self.tree[r][1] < self.tree[min_index][1]):
            min_index = r
        if i != min_index:
            self.swap(i, min_index)
            self.min_sift_down(min_index)
    
    def tasks2treads(self,r1,r2):
        result = []
        n = r1[0]
        m = r1[1]
        self.tree = []
        for i in range(n):
            self.tree.append([i, 0])
        for i in r2:
            #result.append([self.tree[0][0], self.tree[0][1]])
            print(str(self.tree[0][0]) + ' ' + str(self.tree[0][1]))
            #print(self.tree)
            self.tree[0][1] += i
            self.min_sift_down(0)
        #return result


# In[26]:


f2 = forest2()
f2.tasks2treads([2,5],[1,2,3,4,5])
#[[0,0],[1,0],[0,1],[1,2],[0,4]]
f2.tasks2treads([4,20],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
#[[0,0],[1,0],[2,0],[3,0],[0,1],[1,1],[2,1],[3,1],[0,2],[1,2],
#[2,2],[3,2],[0,3],[1,3],[2,3],[3,3],[0,4],[1,4],[2,4],[3,4]]


# In[ ]:


arr1 = [int(i) for i in input().split(' ')]
arr2 = [int(i) for i in input().split(' ')]
f2 = forest2()
f2.tasks2treads(arr1, arr2)


# <h1>Task 3

# In[9]:


def tab_merge_task(m, n, t_size, m_query):
    max_size = max(t_size)
    t_parents = [i for i in range(m)]
    for o in m_query:
        o = [parent(i-1, t_parents) for i in o]
        if o[0] != o[1]:
            min_i = o[0] if t_size[o[0]] <= t_size[o[1]] else o[1]
            max_i = o[0] if t_size[o[0]] > t_size[o[1]] else o[1]
            t_size[min_i] += t_size[max_i]
            t_size[max_i] = 0
            t_parents[max_i] = t_parents[min_i]
            if t_size[min_i] > max_size:
                max_size = t_size[min_i]
        print(max_size)

def parent(i, tree):
    if tree[i] != i:
        tree[i] = parent(tree[i], tree)
    return tree[i]


# In[10]:


tab_merge_task(5, 5, [1,1,1,1,1], [[3,5],[2,4],[1,4],[5,4],[5,3]])
#[2,2,3,5,5]
tab_merge_task(6, 4, [10,0,5,0,3,3], [[6,6],[6,5],[5,4],[4,3]])
#[10,10,10,11]


# In[6]:


str1 = input()
arr1 = [int(i) for i in str1.split(' ')]
m = arr1[0]
n = arr1[1]
str1 = input()
t_size = [int(i) for i in str1.split(' ')]
m_query = []
for l in range(n):
    str1 = input()
    m_query.append([int(i) for i in str1.split(' ')])
tab_merge_task(m, n, t_size, m_query)


# <h1>Task 4

# In[22]:


def check_equal_system(n, e, d, v_pairs):
    var = [i for i in range(n)]
    i = 1
    for pair in v_pairs:
        if i <= e:
            var[pair[1]-1] = var[pair[0]-1]
        if i > e and i <= e + d:
            if var[pair[0]-1] == var[pair[1]-1]:
                print(0)
                return
        i += 1
    print(1)


# In[23]:


check_equal_system(4,6,0,[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]])
#1
check_equal_system(6,5,3,[[2,3],[1,5],[2,5],[3,4],[4,2],[6,1],[4,6],[4,5]])
#0


# In[18]:


str1 = input()
arr1 = [int(i) for i in str1.split(' ')]
n = arr1[0]
e = arr1[1]
d = arr1[2]
v_pairs = []
for i in range(e + d):
    str1 = input()
    arr1 = [int(i) for i in str1.split(' ')]
    v_pairs.append(arr1)
check_equal_system(n, e, d, v_pairs)

