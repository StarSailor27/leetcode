from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle = [i+1 for i in range(n)]
        queue = deque(circle)
        queue.reverse()
        print(queue)
        while(len(queue) > 1):
            queue.rotate(k-1)
            queue.pop()
            print(queue)
        return queue.pop()