import sys
sys.setrecursionlimit(10000)

def solution(s):
    return solutionHelp(s, 0)

def solutionHelp(s, count):
    if len(s) == 0:
        return count

    sList = list(s)
    x = sList[0]
    xCount, notXCount = 0, 0
    
    for i in range(len(s)):
        if xCount != 0 and notXCount != 0 and xCount == notXCount:
            newS = s[xCount+notXCount:]
            return solutionHelp(newS, count + 1)
        
        if sList[i] == x:
            xCount += 1
        else:
            notXCount += 1
    
    return count + 1
