for T in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    for i in range(n):
        while len(st) and a[i] >= a[st[-1]]:
            st.pop()
        if len(st):
            print (i - st[-1], end=" ")
        else:
            print (i + 1, end=" ")
        st.append(i)
    print ()
