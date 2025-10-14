class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


def teste(x: int):
    if x < 0:
        return False
    return str(x) == str(x)[::-1]


print(teste(-121))
