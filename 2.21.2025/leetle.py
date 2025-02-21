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

def solve(root, hi=10**4, lo=-10**4):
  if root == None:
    return True

  if not lo < root.val < hi:
    return False
  
  return solve(root.left, root.val, lo) and solve(root.right, hi, root.val)

if __name__ == '__main__':
    input = [2, 1, 3]
    root = createTree(input)
    print(solve(root))