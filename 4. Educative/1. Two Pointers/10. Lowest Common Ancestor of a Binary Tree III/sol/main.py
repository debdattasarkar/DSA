from EduBinaryTree import *
from EduTreeNode import *

def lowest_common_ancestor(p, q):
    # Initialize two pointers
    ptr1, ptr2 = p, q

    # Traverse until they meet
    while ptr1 != ptr2:

        # Move ptr1 to parent node or switch to the other node if reached the root
        if ptr1.parent:
            ptr1 = ptr1.parent
        else:
            ptr1 = q

		# Move ptr2 to parent node or switch to the other node if reached the root
        if ptr2.parent:
            ptr2 = ptr2.parent
        else:
            ptr2 = p

    # Return ptr1 or ptr2, since they are the same at this point
    return ptr1
 
# Driver code
def main():
    input_trees = [
        [100, 50, 200, 25, 75, 350],
        [100, 200, 75, 50, 25, 350],
        [350, 100, 75, 50, 200, 25],
        [100, 50, 200, 25, 75, 350],
        [25, 50, 75, 100, 200, 350]
    ]
    input_nodes = [
        [25, 75],
        [50, 350],
        [100, 200],
        [50, 25],
        [350, 200]
    ]

    for i in range(len(input_trees)):
        tree = EduBinaryTree(input_trees[i])
        print((i+1),".\tBinary tree:", sep="")
        display_tree(tree.root)
        print("\n\tp = ",input_nodes[i][0])
        print("\tq = ", input_nodes[i][1])
        
        p = tree.find(tree.root, input_nodes[i][0])
        q = tree.find(tree.root, input_nodes[i][1])
        
        lca = lowest_common_ancestor(p, q)
        print("\n\tLowest common ancestor:", lca.data)
        print("-"*100)

if __name__ == "__main__":
    main()