"'#Enter a string'"
S = input()
SS = S[0]
L = ' '
i = 1
for i in range(1, len(S)):
    if SS[-1] <= S[i]:
        SS = SS+S[i]
    else:
        if len(SS) > len(L):
            L = SS
        SS = S[i]
    if len(SS) > len(L):
        L = SS
print(L)
