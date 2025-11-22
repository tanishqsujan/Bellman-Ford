def sumstring(s):

    def check(a, b, rem):
        sum1 = str(int(a) + int(b))
        if not rem:
            return True
        if not rem.startswith(sum1):
            return False
        return check(b, sum1, rem[len(sum1):])

    n = len(s)

    for i in range(1, n):
        for j in range(i+1, n):
            a = s[:i]
            b = s[i:j]
            rem = s[j:]

            if (a.startswith("0") and len(a) > 1) or (b.startswith("0") and len(b) > 1):
                continue

            if check(a, b, rem):
                return True
    return False


s = input("Enter string: ")
if sumstring(s):
    print("YES, it is a Sum String.")
else:
    print("NO, it is NOT a Sum String.")