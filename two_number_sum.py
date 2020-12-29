def twoNumberSum(array, targetSum):
    result_array = []
    for i, value_at_i in enumerate(array):
        print(f'i-index-> {i}: {value_at_i}')
        remaining_arr = array[i+1:]
        for j, value_at_j in enumerate(remaining_arr):
            if(addToGetTargetSum(value_at_i, value_at_j, targetSum)):
                result_array.append(value_at_i)
                result_array.append(value_at_j)
    return result_array

def addToGetTargetSum(num1, num2, targetSum):
    return num1 + num2 == targetSum

def main():
    print(twoNumberSum([10, 5, 20, 7], 12))

if __name__ == "__main__":
    main()