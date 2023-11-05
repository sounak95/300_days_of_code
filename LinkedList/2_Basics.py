class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

    def __del__(self):
        print("Destructor called for:", self.data)


# I want to insert a node right at the head of Linked List
def insert_at_head(head_tail, data):
    head, tail = head_tail
    # check for Empty LL
    if head is None:
        new_node = Node(data)
        head = new_node
        tail = new_node
    else:
        # step1:
        new_node = Node(data)
        # step2:
        new_node.next = head
        # step3:
        head = new_node
    return head, tail


# I want to insert a node right at the end of LINKED LIST
def insert_at_tail(head_tail, data):
    head, tail = head_tail
    if head is None:
        new_node = Node(data)
        head = new_node
        tail = new_node
    else:
        # step1: create a node
        new_node = Node(data)
        # step2: connect with tail node
        tail.next = new_node
        # step3: update tail
        tail = new_node
    return head, tail


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, "->", end="")
        temp = temp.next
    print()


def find_length(head):
    length = 0
    temp = head
    while temp is not None:
        temp = temp.next
        length += 1
    return length


def insert_at_position(head_tail, data, position):
    head, tail = head_tail
    length = find_length(head)

    if position == 1:
        head, tail = insert_at_head((head, tail), data)
    elif position > length:
        head, tail = insert_at_tail((head, tail), data)
    else:
        new_node = Node(data)
        prev = None
        curr = head
        while position != 1:
            position -= 1
            prev = curr
            curr = curr.next
        # step3:
        new_node.next = curr
        # step4:
        prev.next = new_node

    return head, tail


def delete_node(head_tail, position):
    head, tail = head_tail
    # empty list
    if head is None:
        print("Cannot delete, coz LL is empty")
        return head, tail

    if head == tail:
        # single element
        del head  # Python handles memory management automatically
        head = None
        tail = None
        return head, tail

    length = find_length(head)

    # delete from head
    if position == 1:
        # first node ko delete kardo
        temp = head
        head = head.next
        temp.next = None
        del temp  # Python handles memory management automatically
    elif position == length:
        # last node ko delete krdo

        # find prev
        prev = head
        while prev.next != tail:
            prev = prev.next

        # prev node ka link null karo
        prev.next = None

        # node delete kro
        del tail  # Python handles memory management automatically

        # update tail
        tail = prev
    else:
        # middle me koi node ko delete krna h

        # step1: set prev/curr pointers
        prev = None
        curr = head
        while position != 1:
            position -= 1
            prev = curr
            curr = curr.next

        # step2: prev -> next me curr ka next node add kro
        prev.next = curr.next

        # step3: node isolate krdo
        curr.next = None
        # step4: delete node
        del curr  # Python handles memory management automatically

    return head, tail


# Example usage:
head, tail = None, None
head, tail = insert_at_head((head, tail), 50)
print_list(head)
print("Before -> Length of LL is:", find_length(head))
if tail:
    print("Before tail ->", tail.data)
head, tail = delete_node((head, tail), 1)
print("After Length of LL is:", find_length(head))
if tail:
    print("After tail ->", tail.data)
