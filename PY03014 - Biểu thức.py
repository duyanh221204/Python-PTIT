for T in range(int(input())):
    s = input()
    k = ""
    for i in s:
        if i == "(" or i == ")":
            k += i
    st = []
    d = 1
    for i in range(len(k)):
        if k[i] == "(":
            print (d, end=" ")
            st.append(d)
            d += 1
        else:
            print (st[-1], end=" ")
            st.pop()
    print ()
