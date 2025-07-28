def merger_strings(str1, str2):
    ans = ""
    min_len = min(len(str1), len(str2))
    for i in range(min_len):
        ans += s1[i] + s2[i]
    ans += str1[min_len:] + str2[min_len:]
    return ans


s1 = input("Enter a string s1: ")
s2 = input("Enter a string s2: ")

print("Reversed s1: " + s1[::-1])

a = int(input("Enter a number a (1 <= a <= b): "))
b = int(input("Enter a number b (a <= b <= len(s2): "))

if 1 <= a <= b <= len(s2):
    print("Reversed s2 from a to b: " + s2.replace(s2[a - 1: b:], s2[a - 1: b:][::-1]))
else:
    print("Not a valid number")

s3 = s1[1::2]
# s3 = ''.join(s1[i] for i in range(len(s1)) if i % 2 != 0)
print("Removed even index number of s1: " + s3)

s4 = merger_strings(s1, s2)
print("Merged string from s1 and s2: " + s4)
