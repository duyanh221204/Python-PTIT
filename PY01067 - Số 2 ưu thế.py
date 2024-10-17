import queue


def kt(n):
    return n.count("2") > len(n) >> 1


for T in range(int(input())):
    n = int(input())
    d = 0
    q = queue.Queue()
    q.put("1")
    q.put("2")
    while q.qsize() > 0:
        m = q.get()
        if kt(m):
            d += 1
            print (m, end=" ")
            if d == n:
                print ()
                break
        for i in range(3):
            q.put(m + str(i))
