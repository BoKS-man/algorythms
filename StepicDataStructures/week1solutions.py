#!/usr/bin/env python
# coding: utf-8

# <h1>Task 1

# In[ ]:


def check_brackets(s):
    stack = []
    indexes = []
    brackets = ['[',']','(',')','{','}']
    for i in range(len(s)):
        if brackets.count(s[i]) > 0:
            if brackets.index(s[i]) % 2 == 0:
                stack.append(s[i])
                indexes.append(i + 1)
            else:
                if len(stack) > 0 and                stack[len(stack)-1] == brackets[brackets.index(s[i]) - 1]:
                    stack.pop()
                    indexes.pop()
                else:
                    return i + 1
    if len(indexes) > 0:
        return(indexes[0])
    return ('Success')


# In[42]:


check_brackets('[]'),check_brackets('{}[]'),check_brackets('[()]'),check_brackets('(())'),check_brackets('{[]}()'),check_brackets('{'),check_brackets('{[}'),check_brackets('foo(bar);'),check_brackets('foo(bar[i);'),


# <h1>Task 2

# In[44]:


def find_tree_depth(num, dots_parents):
    total_depth = 0
    for i in range(num):
        dot_depth = find_dot_depth(i, dots_parents)
        if dot_depth > total_depth:
            total_depth = dot_depth
    return total_depth


# In[45]:


def find_dot_depth(index, tree):
    if tree[index] < 0:
        return 1
    return find_dot_depth(tree[index], tree) + 1


# In[46]:


find_tree_depth(5,[4,-1,4,1,1]),find_tree_depth(5,[-1,0,4,0,3])


# <h1>Task 3

# In[43]:


def pkg_process(size, n, pkgs):
    process = []
    log = {}
    for pkg in pkgs:
        work_result = pkg[0]
        for l in range(pkg[0], pkg[1] + pkg[0]):
            if log.get(l, 0) < size:
                log[l] = log.get(l, 0) + 1
            else:
                work_result = -1
        process.append(work_result)
    return process
        


# In[44]:


pkg_process(1,2,[]),pkg_process(1,1,[[0,0]]),pkg_process(1,2,[[0,1],[0,1]]),pkg_process(1,2,[[0,1],[1,1]])


# <h1>Task 4

# In[54]:


def process_max_stack(incoming):
    cmd_count = -1
    stack = []
    s_max = []
    result = []
    for task in incoming:
        if cmd_count < 0:
            cmd_count = int(task)
            continue
        cmd = task.split(' ')
        l_max = s_max[len(s_max) - 1] if len(s_max) > 0 else 0
        if cmd[0] == 'max':
            result.append(l_max)
        elif cmd[0] == 'pop':
            stack.pop()
            s_max.pop()
        elif cmd[0] == 'push':
            stack.append(cmd[1])
            if len(s_max) == 0 or l_max < cmd[1]:
                s_max.append(cmd[1])
            else:
                s_max.append(l_max)
    return result


# In[55]:


process_max_stack(["3","push 1","push 7","pop"]),process_max_stack(["5","push 2","push 1","max","pop","max"]),process_max_stack(["6","push 7","push 1","push 7","max","pop","max"]),process_max_stack(["5","push 1","push 2","max","pop","max"]),process_max_stack(["10","push 2","push 3","push 9","push 7",                   "push 2","max","max","max","pop","max"])
#([],[2,2],[7,7],[2,1],[9,9,9,9])


# <h1>Task 5

# In[67]:


def find_shift_max(n, array, f_size):
    result = []
    l_max = 0
    for i in range(n):
        if array[i] > l_max:
            l_max = array[i]
        if i >= f_size-1:
            result.append(l_max)
    return result


# In[68]:


find_shift_max(8,[2,7,3,1,5,2,6,2],4)
#[7,7,5,6,6]


# In[ ]:


1 2 3 4 5 6 7 8
2 7 3 1 5 2 6 2
2 7 7 7 7 5 6 6


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




