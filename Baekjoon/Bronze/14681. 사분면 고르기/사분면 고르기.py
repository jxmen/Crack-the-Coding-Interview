def get_quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:  # x > 0 and y < 0
        return 4

def main():
    x = int(input())
    y = int(input())
    print(get_quadrant(x, y))

if __name__ == "__main__":
    main()