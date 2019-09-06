# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:40:56 2019

@author: Lori
"""

from binarytree import Node

root= Node(5)
root.left=Node(15)
root.right=Node(30)
root.right.right=Node(35)
root.left.left=Node(20)
root.left.right=Node(50)
root.left.left.left=Node(10)
root.left.right.right=Node(25)
root.left.right.left=Node(70)
print(root)
