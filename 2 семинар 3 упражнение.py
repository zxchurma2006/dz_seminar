stroka = input()
left = 0
right = len(stroka) - 1
palindrome = True
zerkal = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
    'Y': 'Y', '1': '1', '8': '8',
    'E': '3', 'J': 'L', 'S': '2', 'Z': '5',
    '3': 'E', 'L': 'J', '2': 'S', '5': 'Z','B':'B'
}
while left <= right:
    left1 = stroka[left]
    right1 = stroka[right]
    if left1 in zerkal:
        zerkal1 = zerkal[left1]
        if zerkal1 != right1:
            palindrome = False
            break
    else:
        palindrome = False
        break
    left += 1
    right -= 1
if palindrome:
    print(stroka, "is a mirrored palindrome.")
else:
    print(stroka, "is not a palindrome.")