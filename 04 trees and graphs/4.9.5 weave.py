# Given two arrays, return all possible ways to merge them 
# while preserving relative order between elements from the same array.

def weave(list1, list2, prefix = [], results = []):
    if not list1 or not list2:
        result = prefix + list1 + list2
        results.append(result)
        return results
    prefix1 = prefix + [list1[0]]
    weave(list1[1:], list2, prefix1, results)
    prefix2 = prefix + [list2[0]]
    weave(list1, list2[1:], prefix2, results)
    return results

if __name__ == '__main__':
    list1 = [1,2]
    list2 = [3,4]
    print(weave(list1, list2))