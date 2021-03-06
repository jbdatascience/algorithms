# Given two binary trees, write a function to check if they are identical.
# (For simplicity, we will not consider the rotations of the tree to be
# identical.) We are given the roots for both binary trees.
# We need to simply traverse both trees at the same time and compare the
# node values. We can traverse in a breadth first or a depth first manner.
# We will show the depth first search here.

def isSameTree(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False

# Time Complexity O(min(N,M))
# where N and M are the number of nodes for the trees.

# Space Complexity O(min(height1, height2))
# levels of recursion is the mininum height between the two trees.


