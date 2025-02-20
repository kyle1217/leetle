from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(input, index=0):
   if index >= len(input) or input[index] is None:
      return None
   
   node = TreeNode(input[index])
   node.left = createTree(input, 2 * index + 1)
   node.right = createTree(input, 2 * index + 2)

   return node

def printTree(root):
    queue = deque([root])

    while queue:
       node = queue.popleft()
       print(node.val, end=" ")

       if node:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    print()
      

def solve(node):
  if not node:
     return None
  
  temp = node.left
  node.left = node.right
  node.right = temp

  solve(node.left)
  solve(node.right)
  
  return node

if __name__ == '__main__':
   input = [4, 2, 7, 1, 3, 6, 9]
   root = createTree(input)
   printTree(solve(root))