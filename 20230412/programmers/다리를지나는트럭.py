bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

def solution(bridge_length, weight, truck_weights):
    a = [0] * bridge_length
    sec = 0
    while a:
        sec += 1
        curr_weight = a.pop(0)
        if truck_weights:
            curr_weight += truck_weights[0]
            if curr_weight + truck_weights[0] <= weight:
                a.append(truck_weights.pop(0))
            else:
                a.append(0)
    return sec

print(solution(bridge_length=bridge_length,
               weight=weight,
               truck_weights=truck_weights))