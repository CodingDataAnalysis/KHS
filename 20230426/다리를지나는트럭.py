bridge_length = 100  # 올라갈 수 있는 트럭 개수
weight = 100   # 다리가 견딜 수 있는 무게
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
# 지나가는 트럭의 무게

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    while bridge:
        curr_weight = bridge.pop(0)
        answer += 1
        if truck_weights:
            curr_weight += truck_weights[0]
            if curr_weight + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer

print(solution(bridge_length, weight, truck_weights))