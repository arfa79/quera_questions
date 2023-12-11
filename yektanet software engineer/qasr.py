def closest_distance(n, heights):
    distance = 0
    current_height = 0
    
    for i in range(n):
        if heights[i] == 1:
            current_height += 1
        elif heights[i] == 2:
            current_height += 2
        
        if heights[i] == 0:
            continue
        
        distance = min(distance, abs(current_height))
    
    return abs(distance)

# ورودی نمونه
n = 5
heights = [1, 2, 1, 0, 2]

# چاپ کمینه فاصله ممکن از قصر خیالی
print(closest_distance(n, heights))
