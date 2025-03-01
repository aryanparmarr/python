def Frequency(arr, n):
    mp = {}               # here frequency is counted using hashing by making a dictionary mp to reduce time complexity 
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
    for x in mp:
        print(x, mp[x])
