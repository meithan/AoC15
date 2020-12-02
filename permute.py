def permutations(alist):
    result = []
    if len(alist) == 1: return [alist]
    for i in range(len(alist)):
        sublist = alist[:i] + alist[i+1:]
        subperms = permutations(sublist)
        for subperm in subperms:
            result.append([alist[i]]+subperm)
    return result

def circular_permutations(alist):
    if len(alist) <= 3: return [alist]
    result = [alist[:3]]
    remain = alist[3:]
    while len(remain) > 0:
        elem = remain.pop()
        buff = []
        for sub in result:
            for i in range(len(sub)):
                buff.append(sub[:i]+[elem]+sub[i:])
        result = buff
    return result
        

res = circular_permutations([1,2,3,4,5,6,7])
print res
print len(res)
