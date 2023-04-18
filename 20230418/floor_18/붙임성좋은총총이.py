from sys import stdin
N = int(stdin.readline())
infected_peoples = set(['ChongChong'])
for n in range(N):
    people_a, people_b = stdin.readline().rstrip().split()
    if people_a in infected_peoples or people_b in infected_peoples:
        infected_peoples.add(people_a)
        infected_peoples.add(people_b)
print(len(infected_peoples))