s = input().split()
print ("YES" if ord(s[0]) + ord(s[2]) - 96 == ord(s[4]) - 48 else "NO")
