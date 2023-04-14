import sys
N = int(sys.stdin.readline())
coords_list = list(map(int, sys.stdin.readline().rstrip().split()))
coords_list_mod = sorted(list(set(coords_list)))
# 최소값부터 정렬한 리스트에 요소 개수 0~4까지 매핑시킨 딕셔너리 생성
# 각 좌표가 요소 개수의 몇 번째에 해당하는지 좌표 리스트에 매핑하면
# 두 리스트를 비교하는 것보다 시간을 줄일 수 있음
coords_dict = {coords_list_mod[i]:i for i in range(len(coords_list_mod))}
for i in coords_list:
    print(coords_dict[i], end=' ')