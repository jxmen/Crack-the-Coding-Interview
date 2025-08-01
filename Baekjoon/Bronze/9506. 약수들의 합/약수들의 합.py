def get_str(n):
    nums = []
    for num in range(1, n):
        if n % num == 0:
            nums.append(num)

    if sum(nums) == n:
        s = f"{n} = "
        for i in range(len(nums) - 1):
            s += f"{nums[i]} + "
        
        s += str(nums[-1])
        return s
    else:
        return f"{n} is NOT perfect."

if __name__ == "__main__":
    while True:
        n = int(input())
        if n == -1:
            break
    
        print(get_str(n))
