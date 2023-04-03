n = int(input())

counter = 1   
floor = 1 

# 2번방 이후로 방을 6개 지날 때마다 방이 6개씩 늘어남
# 2~7, 8~19, 20~37, 38~61
while floor < n:
    floor += 6*counter  
    counter += 1       

print(counter)   