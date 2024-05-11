def minimum_chunks_to_sort(n, a):
    chunks = 1  
    max_seen = a[0]  
    
    for i in range(1,n):
        if a[i]>a[i-1] and a[i] < max_seen: 
            continue
        else:
            chunks += 1
            max_seen = max(max_seen, a[i])
    return chunks

n = 3
cards = [1,4,2]

result = minimum_chunks_to_sort(n, cards)
print(result)