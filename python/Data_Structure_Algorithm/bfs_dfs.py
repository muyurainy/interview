# -*- coding: utf-8 -*-
from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def BFS(g):
    '''BFS

    Parameter
    ---------
    g: 二叉树
    Return
    ------
    BFS遍历序列
    '''
    queue = deque()
    queue.append(g)
    while(len(queue)):
        treenode = queue.popleft()
        print (treenode.val)
        if treenode.left:
            queue.append(treenode.left)
        if treenode.right:
            queue.append(treenode.right)

def DFS(g):
    '''DFS

    Parameter
    ---------
    g: 二叉树
    n: 当前访问的节点
    Return
    ------
    DFS遍历序列
    '''
    if(g.left == None and g.right == None):
        print (g.val)
        return
    print (g.val)
    if g.left:
        DFS(g.left)
    if g.right:
        DFS(g.right)

'''

'''
treenode = TreeNode(0)
treenode1 = TreeNode(1)
treenode2 = TreeNode(3)
treenode.left = treenode1
treenode.right = treenode2
treenode3 = TreeNode(2)
treenode1.right = treenode3
DFS(treenode)