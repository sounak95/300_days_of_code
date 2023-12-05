
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def create_tree():
    print("Enter the value for Node: ")
    data = int(input())

    if data==-1:
        return None

    # Step1: create Node
    root = Node(data)
    # Step2: Create left subtree
    print(f"Left of Node: {root.data}")
    root.left = create_tree()

    # Step3: Create right subtree
    print(f"Right of Node: {root.data}")
    root.right = create_tree()

    return root


# Main method to call create_tree()
if __name__ == "__main__":
    tree_root = create_tree()