# Time complexity: O(n)
# Space complexity: O(1)
def twoNumberSum(array, targetSum):
  visited = set()
  for num in array:
    diff = targetSum - num
    if (diff in visited and diff != num):
      return[diff, num]
    visited.add(num)

  return []

def main():
    array = [3, 4, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum(array, targetSum))

main()
