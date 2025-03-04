class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def solve(head):
  if not head or not head.next:
    return head
  
  # find n/2
  slow, fast = head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

  # reverse second half
  prev, curr = None, slow
  while curr:
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

  # merge two lists
  first, second = head, prev
  while second.next:
    temp1, temp2 = first.next, second.next
    first.next = second
    second.next = temp1
    first, second = temp1, temp2
  
  return head

def create_list(arr):
  if not arr:
    return None
  head = ListNode(arr[0])
  current = head
  for val in arr[1:]:
    current.next = ListNode(val)
    current = current.next
  return head
  
def print_list(head):
  current = head
  while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next

if __name__ == '__main__':
  input = [1, 2, 3, 4, 5]
  head = create_list(input)
  print_list(head)
  solve(head)
  print_list(head)