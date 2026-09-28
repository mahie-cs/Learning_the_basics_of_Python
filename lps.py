s: str = "abacabab"
#lps     :00101232
#index   :01234567
j: int = 0
lps: list[int] = [0]
for i in range(1, len(s)):
    while j > 0 and s[j] != s[i]:
        j = lps[j-1]
    if s[j] == s[i]:
        j += 1
    lps.append(j)
print(lps)
