# Exo5: Create an algo for the binary search

t = range(1, 100)
le = 0
ri = len(t)-1
rem = -1
x = int(input("enter a positif number to be search! "))
while le <= ri:
 if rem != -1:
    break
 if rem == -1:
    mi = (le + ri) // 2
    if x == t[mi]:
       rem = mi
    elif x < t[mi]:
         ri = mi - 1
    else:
        le = mi + 1

if rem == -1:
    print("No element in the list.")
else:
    print("element ", x, "in position: ", rem)
