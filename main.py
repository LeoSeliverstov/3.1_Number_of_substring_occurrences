s, t = input(), input()
# s, t = 'abababa', 'aba'
count = 0

for i in range(len(s)):
    if t in s[i:i + len(t)]:
        count += 1
print(count)
