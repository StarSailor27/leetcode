from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Data structure - dictionary
        dic = {'2' : ['a', 'b', 'c'], 
               '3' : ['d', 'e', 'f'],
               '4' : ['g', 'h', 'i'],
               '5' : ['j', 'k', 'l'],
               '6' : ['m', 'n', 'o'],
               '7' : ['p', 'q', 'r', 's'],
               '8' : ['t', 'u', 'v'],
               '9' : ['w', 'x', 'y', 'z']
        }
        
        q0 = deque()
        q1 = deque()
        q2 = deque()
        q3 = deque()
        qList = [q0, q1, q2, q3]
        
        # Initial insert queue
        digitList = list(digits)
        length = len(digitList)
        for i in range(length):
            for word in dic[digitList[i]]:
                qList[i].append(word)
        
        cycle = 1
        for i in range(length):
            cycle *= len(qList[i])
            
        output = []
        
        # corner case - Input : ""
        if(length == 0):
            return None
        
        for i in range(cycle):
            
            str_d = ''
            divisor = 1
            for j in range(length):
                if (j != 0):
                    divisor *= len(qList[length-j])
                #print('[j={0} divisor={1}'.format(j, divisor))
                if ((i % divisor == 0) and (i != 0)):
                    qList[length-j-1].rotate()
                str_d += qList[length-j-1][0]
            output.append(str_d[::-1])
        return output