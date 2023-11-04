class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


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
        print(temp.data, end=" ")
        temp = temp.next
    print()


def find_length(head):
    length = 0
    temp = head
    while temp is not None:
        temp = temp.next
        length += 1
    return length


def insert_at_position(data, position, head_tail):
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


def main():
    head, tail = None, None
    head, tail = insert_at_head((head, tail), 20)
    head, tail = insert_at_head((head, tail), 50)
    head, tail = insert_at_head((head, tail), 60)
    head, tail = insert_at_head((head, tail), 90)
    head, tail = insert_at_tail((head, tail), 77)

    print_list(head)


if __name__ == "__main__":
    main()
