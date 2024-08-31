n = int(input())
a = list(map(int, input().split()))
st = []
for i in a:
    if len(st) == 0 or i + st[-1] & 1:
        st.append(i)
    else:
        st.pop()
print (len(st))
