vvod = input().strip().split()
razmer = int(vvod[0])
s = vvod[1]
result = []
for start in range(0, len(s), razmer):
    group = s[start:start + razmer]
    result.append(group[::-1])
print(''.join(result))

