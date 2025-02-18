class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solve(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummy.next

def print_ll(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == '__main__':
    # construct list
    head = ListNode(1)
    current = head
    for val in [2, 3, 4, 5]:
        current.next = ListNode(val)
        current = current.next

    n = 2
    print_ll(head)
    head = solve(head, n)
    print_ll(head)