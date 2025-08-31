'''
Looking for optimal pair of elements, thus maximizing heights and width = so more area of water
Starting the pointers at one and two position can lead to confusing choices and more moves than starting from extremes

Either maximum width (or) maximum height.
Also, the usable height is the minimum of two heights, as only that much can be filled.
=> Min(height1, height2)
 
How to calc width then? Right index - Left index - their element positions => Width 

area = height * width

Trade-off: We sacrifice width at each step in the hope of finding a greater height.



'''

height = [1,8,6,2,5,4,8,3,7]

left = 0
right = len(height) - 1
maximum_area = 0
while left < right:
    
    h = min(height[left], height[right])
    w = right - left

    current_area = h * w
    if current_area > maximum_area:
        maximum_area = current_area
        
    if height[left] < height[right]:
        left += 1
    else:
        right -=1
        
print(maximum_area)
