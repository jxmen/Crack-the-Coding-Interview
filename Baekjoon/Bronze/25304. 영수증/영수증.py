def solution(x, item_lines):
    total_item_price = 0
    for item_line in item_lines:
        a, b = item_line[0], item_line[1]
        total_item_price += (a * b)

    return "Yes" if total_item_price == x else "No"

if __name__ == "__main__":
    x = int(input())
    n = int(input())
    itmes_lines = []
    for _ in range(n):
        a, b = map(int, input().split())
        itmes_lines.append([a, b])
    
    print(solution(x, itmes_lines))
