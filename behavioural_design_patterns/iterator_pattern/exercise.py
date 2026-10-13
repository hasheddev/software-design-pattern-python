from __future__ import annotations

class Node:
  def __init__(self, value, left: Node | None = None, right: Node | None = None):
    self.right = right
    self.left = left
    self.value = value

    self.parent = None

    if self.left:
      self.left.parent = self
    if self.right:
      self.right.parent = self

  def traverse_preorder(self):
    array = []
    return Node.preorder(self, array)
    # todo - return inorder values (not Nodes)
  @staticmethod
  def preorder(root: Node | None, array: list):
    #Preorder Traversal (Root -> Left -> Right)
    if root is None:
      return array
    array.append(root.value)
    Node.preorder(root.left, array)
    Node.preorder(root.right, array)
    return array
    
