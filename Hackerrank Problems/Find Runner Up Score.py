if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    arr.sort()
    mx = arr[len(arr)-1]
    for i in range(len(arr)-1,-1,-1):
        if arr[i]<mx:
            print(arr[i])
            break