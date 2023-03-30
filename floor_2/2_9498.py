def print_score():
    score = int(input())
    if score >= 90 and score <= 100:
        return print('A')
    elif score >= 80 and score <= 89:
        return print('B')
    elif score >= 70 and score <= 79:
        return print('C')
    elif score >= 60 and score <= 69:
        return print('D')
    else:
        return print('F')
    
if __name__ == "__main__":
    print_score()