class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def print_list(head):
    # Function to print the doubly linked list
    temp = head
    while temp is not None:
        print(temp.data, end="->")
        temp = temp.next
    print("NULL")

def find_length(head):
    # Function to find the length of the doubly linked list
    temp = head
    len = 0
    while temp is not None:
        len += 1
        temp = temp.next
    return len

def insert_at_head(head_tail, data):
    # Function to insert a node at the head of the doubly linked list
    head, tail = head_tail
    if head is None:  # LL is empty
        newNode = Node(data)
        head = newNode
        tail = newNode
    else:  # LL is not empty
        newNode = Node(data)
        newNode.next = head
        head.prev = newNode
        head = newNode
    return head, tail

def insert_at_tail(head_tail, data):
    # Function to insert a node at the tail of the doubly linked list
    head, tail = head_tail
    if head is None:  # LL is empty
        newNode = Node(data)
        head = newNode
        tail = newNode
    else:  # LL is non-empty
        newNode = Node(data)
        tail.next = newNode
        newNode.prev = tail
        tail = newNode
    return head, tail

def insert_at_position(head_tail, data, position):
    # Function to insert a node at a given position in the doubly linked list
    head, tail = head_tail
    if head is None or position == 1:  # Insert at head
        head, tail = insert_at_head(head_tail, data)
    else:
        len = find_length(head)
        if position > len + 1:  # Position is out of bounds
            return head, tail
        if position == len + 1:  # Insert at tail
            head, tail = insert_at_tail(head_tail, data)
        else:  # Insert in the middle
            # Step 1: Create node
            newNode = Node(data)
            # Step 2: Set prev and curr pointers
            prevNode = None
            currNode = head
            for _ in range(position - 1):
                prevNode = currNode
                currNode = currNode.next
            # Step 3: Update pointers
            prevNode.next = newNode
            newNode.prev = prevNode
            newNode.next = currNode
            currNode.prev = newNode
    return head, tail

def delete_node(head_tail, position):
    # Function to delete a node from the doubly linked list
    head, tail = head_tail
    if head is None:  # LL is empty
        print("Cannot delete, because LL is empty")
        return head, tail

    if head == tail:  # LL has only one node
        del head  # Python handles memory deallocation
        return None, None

    len = find_length(head)
    if position == 1:  # Delete from head
        next_node = head.next
        del head
        next_node.prev = None
        head = next_node
    elif position == len:  # Delete from tail
        prev_node = tail.prev
        del tail
        prev_node.next = None
        tail = prev_node
    else:  # Delete from middle
        # Step 1: Set prevNode/currNode/nextNode
        prevNode = None
        currNode = head
        for _ in range(position - 1):
            prevNode = currNode
            currNode = currNode.next
        nextNode = currNode.next
        # Step 2: Update pointers
        prevNode.next = nextNode
        nextNode.prev = prevNode
        del currNode  # Python handles memory deallocation

    return head, tail

# Main program
head, tail = None, None
head, tail = insert_at_head((head, tail), 40)
head, tail = insert_at_head((head, tail), 30)
head, tail = insert_at_head((head, tail), 20)
head, tail = insert_at_head((head, tail), 10)
print_list(head)

# Perform deletions
head, tail = delete_node((head, tail), 4)
print_list(head)
