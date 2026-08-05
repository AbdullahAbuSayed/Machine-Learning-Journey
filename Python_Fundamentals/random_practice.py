# n= int(input("total name :"))
# name_list=[]
# for r in range(n):
#     name=input(f"Enter your {r+1} name :")
#     name_list.append(name)
#     print (name)

# for k in name_list:
#     print(f"your name is {k}")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

if __name__ == "__main__":
    nums = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_val = 23
    
    result = binary_search(nums, target_val)
    print(result)