'''
Use heap :

Min-Heap: Smallest element at the top, each parent is smaller than or equal to its kids.

Max-Heap: Largest element at the top, each parent is larger than or equal to its kids.

'''
import heapq
def gold_wires(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return 1
    
    heapq.heapify(arr)     # Convert to a heap to maintain min-heap, i.e. smallest element is at root node
    total_cost = 0
    
    while len(arr) > 1:
        wire1 = heapq.heappop(arr)
        wire2 = heapq.heappop(arr)
        
        current_cost = wire1 + wire2
        
        total_cost += current_cost
        
        heapq.heappush(arr, current_cost)
        
    return total_cost
    
arr = [7, 6, 8, 6, 1, 1]
print(gold_wires(arr))