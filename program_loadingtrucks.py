from collections import deque
def solution(bridge_length, weight, truck_weights):
    cnt = 0
    current_weight = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)

    while len(trucks) > 0:
        cnt += 1
        current_weight = current_weight - bridge.popleft()
        if current_weight + trucks[0] <= weight:
            current_weight = current_weight + trucks[0]
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
    cnt = len(bridge) + cnt

    return cnt