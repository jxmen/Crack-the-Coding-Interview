n = int(input())
n_numbers = [int(x) for x in list(input().split(" "))]
n_numbers.sort()

m = int(input())
m_numbers = [int(x) for x in list(input().split(" "))]

def has_number(number_list, number):
    left, right = 0, len(number_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if number_list[mid] == number:
            return True

        if number_list[mid] > number:
            right = mid - 1
        else:
            left = mid + 1

    return False

for m_number in m_numbers:
    if has_number(n_numbers, m_number):
        print(1)
    else:
        print(0)
