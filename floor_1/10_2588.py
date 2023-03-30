def multiple_threeBythree():
    a = int(input())
    b = input()
    res1 = a * int(b[-1])
    res2 = a * int(b[-2])
    res3 = a * int(b[-3])
    all_res = a * int(b)
    return print(res1, res2, res3, all_res, sep='\n')

if __name__ == "__main__":
    multiple_threeBythree()