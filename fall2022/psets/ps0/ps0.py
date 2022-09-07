#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None

#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: Up to you
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)
def calculate_sizes(v):

    final_size = 1

    if v.left != None:
        final_size += calculate_sizes(v.left)
    
    if v.right != None: 
        final_size += calculate_sizes(v.right)

    v.size = final_size

    return final_size

#
# Problem 1c
#

# Input: BTvertex r, the root of a size-augmented BinaryTree T
# ... of size n and height h
# Output: A BTvertex that, if removed from the tree, would result
# ... in disjoint trees that all have at most n/2 vertices
# Runtime: O(h)
def find_vertex(r):

    vertex = r

    while vertex.left is not None or vertex.right is not None:
        left = vertex.left
        right = vertex.right

        if (left is None or left.size <= r.size / 2) and (right is None or right.size <= r.size / 2):
            return vertex
        
        if left is not None:
            if right is not None:
                vertex = vertex.left
                continue 

            if left.size > r.size / 2:
                vertex = vertex.left

            else: 
                vertex = vertex.right
                
        else:
            vertex = vertex.right

    return vertex

