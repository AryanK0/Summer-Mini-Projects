def subset_selection(arr, target):
    # Basic implementation of finding subsets that sum to target
    res = []
    def backtrack(start, path, current_sum):
        if current_sum == target:
            res.append(path)
            return
        if current_sum > target:
            return
        for i in range(start, len(arr)):
            backtrack(i + 1, path + [arr[i]], current_sum + arr[i])
    backtrack(0, [], 0)
    return res

if __name__ == '__main__':
    print('Subsets summing to 10:', subset_selection([1, 2, 3, 4, 5, 6, 7], 10))