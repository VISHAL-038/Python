def permutations(s, p):
    if len(s) == 0:
        print(p)
        return

    for i in range(len(s)):
        ch = s[i]
        n_s = s[:i] + s[i+1:]
        permutations(n_s, p + ch)
        

print(permutations("abcde", ""))



