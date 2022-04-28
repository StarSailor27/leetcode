# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # comparison using id(ListNode)
        # Sequential search => Time Limit Exceeded
        """
        pA = headA
        pB = headB
        while True:
            while True:
                if (id(pA) == id(pB)):
                    return pA
                if (pB.next == None): break
                pB = pB.next

            pB = headB
            if (pA.next == None): break
            pA = pA.next
        """
        pA = headA
        pB = headB
        adrA = []
        adrB = []
        while True:
            adrA.append(id(pA))
            if (pA.next == None): break
            pA = pA.next
        while True:
            adrB.append(id(pB))
            if (pB.next == None): break
            pB = pB.next
        print('adrA: ', adrA)
        print('adrB: ', adrB)

        adrA.reverse()
        adrB.reverse()
        print('[R]adrA: ', adrA)
        print('[R]adrB: ', adrB)
        
        flagLongA = len(adrA) > len(adrB)
        order = (lambda x, y: len(adrA) if (flagLongA) else len(adrB))(adrA, adrB)
        lenShort = len(adrB) if (flagLongA) else len(adrA) 
        
        print(order)
        for i in range(order):
                
            if (adrA[i] != adrB[i]) or (i == (lenShort-1)):
            #if (i == (lenShort-1)):
                order = (order - i) if (adrA[i] != adrB[i]) else order - i - 1
                pLong = headA if (flagLongA) else headB 
                print('(i,order) =',i, order)
                break
            #elif (i == (lenShort-1)):
            #    order = order - i  
                
        for i in range(order):
            pLong = pLong.next
        return pLong
            
            
            #elif ((len(adrA) - len(adrB)) == 1):
            #    return headB if flagLongA else headA
        
        #return headA
        
            
            