# BST Sequences: 
# A binary search tree was created by traversing through an array from left 
# to right and inserting each element. Given a binary search tree with distinct 
# elements, print all possible arrays that could have led to this tree.
# EXAMPLE
# Input:
# Output: {2, 1, 3}, {2, 3, 1}

def allSequences(tree):
    result = []
    if tree is None:
        result.append([])
        return result
    prefix = [tree.data]
    leftSequences = allSequences(tree.left)
    rightSequences = allSequences(tree.right)
    for seqL in leftSequences:
        for seqR in rightSequences:
            weaved = []
            weave(seqL, seqR, weaved, prefix)
            result = result + weaved
    return result

def weave(first, second, results, prefix):
    if not first or not second:
        result = prefix[:]
        result = result + first
        result = result + second
        results.append(result)
    prefix.append(first.pop(0))
    weave(first, second, results, prefix)
    first.insert(0, prefix.pop())
    prefix.append(second.pop(0))
    weave(first, second, results, prefix)
    second.insert(0, prefix.pop())