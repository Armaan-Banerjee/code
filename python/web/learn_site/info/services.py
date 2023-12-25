# from .models import Comment

class ComentNode:
    def __init__(self, comment):
        self.comment = comment
        self.children = []
        self.parent = None

class ComentTree:
    def __init__(self, root_comment):
        self.root = ComentNode(root_comment)
    
    def add_child(self, parent, child_comment) -> ComentNode:
        child = ComentNode(child_comment)
        child.parent = parent
        parent.children.append(child)

        return child
    
    def depth_first_search(self, root, value, level=0, matches = []) -> [(ComentNode, int)]:
        if root.comment == value:
            #print(level)
            matches.append((self, level))
        #print(root.comment)
        for child in root.children:
            self.depth_first_search(child, value, level + 1)
        
        return matches

    def breadth_first_search(self, root: ComentNode, value) -> [ComentNode]:
        matches = []
        queue = [root]
        while queue:
            current_node = queue.pop(0)
            if current_node.comment == value:
                matches.append(current_node)
            print(current_node.comment)
            queue.extend(current_node.children)
    
        return matches
    
    def print_tree(self, root, level=0):
        print(" " * level + root.comment)
        for child in root.children:
            self.print_tree(child, level + 1)


class ListNode:
    def __init__(self, tree):
        self.tree = tree
        self.next = None
        self.prev = None
    

class ComentList:
    def __init__(self):
        self.head = None

    def append(self, tree):
        new_node = ListNode(tree)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    def display_forward(self):
        current = self.head
        while current:
            print(current.tree, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(current.tree, end=" <-> ")
            current = current.prev
        print("None")

    

tree = ComentTree("comment")

child1 = tree.add_child(tree.root, "1st reply")
child2 = tree.add_child(tree.root, "2nd reply")
child3 = tree.add_child(tree.root, "3rd reply")

grandchild1_1 = tree.add_child(child1, "1st reply to 1st reply")
grandchild1_2 = tree.add_child(child1, "2nd reply to 1st reply")

grandchild2_1 = tree.add_child(child2, "1st reply to 2nd reply")
grandchild2_2 = tree.add_child(child2, "2nd reply to 3rd reply")

grandchild3_1 = tree.add_child(child3, "1st reply to 3rd reply")
grandchild3_2 = tree.add_child(child3, "2nd reply to 3rd reply")


comentlist = ComentList()
comentlist.append(1)
comentlist.append(2)
comentlist.append(3)

comentlist.display_forward()
comentlist.display_backward()