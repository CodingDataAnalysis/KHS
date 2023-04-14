N = int(input())
client_list = [dict() for _ in range(N)]
for idx in range(N):
    client_list[idx]["idx"] = idx
    client_list[idx]["old"], client_list[idx]["name"] = input().split()
    client_list[idx]["old"] = int(client_list[idx]["old"])
client_list.sort(key=lambda x: (x["old"], x["idx"]))
for item in client_list:
    print(item["old"], item["name"])