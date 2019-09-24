# coding: utf-8
'''
# 05.15 滴滴一面
'''

def hasLoop(linkNode):
    slow = linkNode
    fast = linkNode
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def findLoopStart(linkNode):
    slow = linkNode
    fast = linkNode
    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return None
    fast = linkNode
    meetNode = slow
    while fast != meetNode:
        fast = fast.next
        slow = slow.next
    return fast