#!/usr/bin/env python
# coding: utf-8

# <h1>Task 1

# In[2]:


def in_order_run(tree, root):
    arr = []
    if root < 0:
        return []
    arr = in_order_run(tree, tree[root][1])
    arr += [str(tree[root][0])]
    arr += in_order_run(tree, tree[root][2])
    return arr

def pre_order_run(tree, root):
    arr = []
    if root < 0:
        return []
    arr = [str(tree[root][0])]
    arr += pre_order_run(tree, tree[root][1])
    arr += pre_order_run(tree, tree[root][2])
    return arr

def post_order_run(tree, root):
    arr = []
    if root < 0:
        return []
    arr = post_order_run(tree, tree[root][1])
    arr += post_order_run(tree, tree[root][2])
    arr += [str(tree[root][0])]
    return arr

def run_tree(tree):
    print(' '.join(in_order_run(tree, 0)))
    print(' '.join(pre_order_run(tree, 0)))
    print(' '.join(post_order_run(tree, 0)))
    return

def run():
    input_tree = []
    n = int(input())
    for i in range(n):
        input_tree.append([int(c) for c in input().split(' ')])
    run_tree(input_tree)


# In[3]:


run_tree([[4,1,2],[2,3,4],[5,-1,-1],[1,-1,-1],[3,-1,-1]])
#[1,2,3,4,5],[4,2,1,3,5],[1,3,2,5,4]
run_tree([[0,7,2],[10,-1,-1],[20,-1,6],[30,8,9],[40,3,-1],[50,-1,-1],[60,1,-1],[70,5,4],[80,-1,-1],[90,-1,-1]])
#[50,70,80,30,90,40,0,20,10,60],[0,70,50,40,30,80,90,20,60,10],[50,80,90,30,40,70,10,60,20,0]


# <h1>Task 2

# In[3]:


def check_tree(tree, root = 0):
    if len(tree) == 0 or (tree[root][1] < 0 and tree[root][2] < 0) or    ((tree[root][1] < 0 or tree[root][0] > tree[tree[root][1]][0]) and
     (tree[root][2] < 0 or tree[root][0] < tree[tree[root][2]][0]) and\
     (tree[root][1] < 0 or check_tree(tree, tree[root][1]) > 0) and\
     (tree[root][2] < 0 or check_tree(tree, tree[root][2]) > 0)):
        return 1
    else:
        return 0

def run():
    input_tree = []
    n = int(input())
    for i in range(n):
        input_tree.append([int(c) for c in input().split(' ')])
    check_tree(input_tree, 0)


# In[4]:


print(check_tree([[2,1,2],[1,-1,-1],[3,-1,-1]])) #CORRECT
print(check_tree([[1,1,2],[2,-1,-1],[3,-1,-1]])) #INCORRECT
print(check_tree([])) #CORRECT
print(check_tree([[1,-1,1],[2,-1,2],[3,-1,3],[4,-1,4],[5,-1,-1]])) #CORRECT
print(check_tree([[4,1,2],[2,3,4],[6,5,6],[1,-1,-1],[3,-1,-1],[5,-1,-1],[7,-1,-1]])) #CORRECT
print(check_tree([[4,1,-1],[2,2,3],[1,-1,-1],[5,-1,-1]])) #INCORRECT


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




