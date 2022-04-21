# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        detect = 0
        headChange = 0
        cycle = 0
        
        if(head == None):
            return None
        elif(head.next == None):
            return head
            
        pList = head
        pListNxt = head.next
        
        diffInfo = []
        
        # make list of difference beetween pList and pListNxt
        while(True):
            #print('pList/pListNxt = ', pList.val, '/', pListNxt.val)
            if(pList.val == pListNxt.val):
                diffInfo.append(1)
            else:
                diffInfo.append(0)
        
            if(pListNxt.next == None):
                diffInfo.append(0)
                cycle += 1
                break
                
            pList = pList.next
            pListNxt = pListNxt.next
            cycle += 1
            
        #print('length =', length)
        print(diffInfo)
        
        # remove duplication
        pList = head
        pListNxt = head
        
        for i in range(cycle):
            if(detect == 0):
                if(diffInfo[i:i+2] == [0,0]): # Not duplicated
                    pList = pList.next
                    pListNxt = pListNxt.next
                else: # Duplicated
                    detect = 1
                    pListNxt = pListNxt.next
                    if(i==0) and (diffInfo[0]==1): headChange = 1
            else: # detect == 1
                if(diffInfo[i:i+2] == [0,0]): # Not duplicated
                    pListNxt = pListNxt.next
                    pList.next = pListNxt
                    if(headChange == 1):
                        head = pList.next
                        pList = head
                    else:
                        pList = pList.next
                    detect = 0
                    headChange = 0
                else: # Duplicated
                    pListNxt = pListNxt.next
            
            print('[{}/{}] pList = {}, pListNxt = {}, detect = {}, headChange = {}'
                  .format(i,cycle,pList.val, pListNxt.val,detect, headChange))

            if((i == (cycle-1)) and (detect == 1)): # last sequence
                if(headChange == 1):
                    """
                    if(diffInfo[0:2] == [0,1]):
                        head.next = None
                    else:
                    """
                    head = None
                else:
                    pList.next = None
        
        return head
        