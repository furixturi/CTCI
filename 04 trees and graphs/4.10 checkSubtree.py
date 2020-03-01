# Check Subtree: 
# T1 and T2 are two very large binary trees, with T1 much bigger than T2. 
# Create an algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of Tl if there exists a node n in T1 such that 
# the subtree of n is identical to T2. That is, if you cut off the tree at 
# node n, the two trees would be identical.
def generateStringFromTree(t, nodeChars=[]):
    if t is None:
        nodeChars.append('X')
    else:
        nodeChars.append(t.data)
        generateStringFromTree(t.left, nodeChars)
        generateStringFromTree(t.right, nodeChars)
    return ' '.join(nodeChars)    

def checkSubtree_solution1(t1, t2):
    t1String = generateStringFromTree(t1)
    t2String = generateStringFromTree(t2)
    return t2String in t1String

######################################################
def matchTree(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data != t2.data:
        return False
    return matchTree(t1.left, t2.left) and matchTree(t1.right, t2.right)

def checkSubtree_solution2(t1, t2):
    if t2 is None:
        return True # empty tree is a subtree of any tree
    if t1 is None:
        return False # empty tree cannot contain an non-empty tree
    if t1.data == t2.data:
        return matchTree(t1, t2)
    return checkSubtree_solution2(t1.left, t2) or checkSubtree_solution2(t1.right, t2)