for T in range(int(input())):
    d, m = map(int, input().split())
    if m == 1:
        print ("Ma Ket" if d <= 19 else "Bao Binh")
    elif m == 2:
        print ("Bao Binh" if d <= 18 else "Song Ngu")
    elif m == 3:
        print ("Song Ngu" if d <= 20 else "Bach Duong")
    elif m == 4:
        print ("Bach Duong" if d <= 19 else "Kim Nguu")
    elif m == 5:
        print ("Kim Nguu" if d <= 20 else "Song Tu")
    elif m == 6:
        print ("Song Tu" if d <= 20 else "Cu Giai")
    elif m == 7:
        print ("Cu Giai" if d <= 22 else "Su Tu")
    elif m == 8:
        print ("Su Tu" if d <= 22 else "Xu Nu")
    elif m == 9:
        print ("Xu Nu" if d <= 22 else "Thien Binh")
    elif m == 10:
        print ("Thien Binh" if d <= 22 else "Thien Yet")
    elif m == 11:
        print ("Thien Yet" if d <= 22 else "Nhan Ma")
    else:
        print ("Nhan Ma" if d <= 21 else "Ma Ket")
