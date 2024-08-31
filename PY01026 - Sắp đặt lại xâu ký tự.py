for T in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    s1.sort()
    s2.sort()
    print (f"Test {T + 1}: ", end="")
    print ("YES" if s1 == s2 else "NO")
