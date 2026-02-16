import time

def index(T, P):
    for i in range(len(T) - len(P) + 1):
        if T[i:i+len(P)] == P:
            return i
    return -1

start = time.time()
print("Index:", index("Data Structures", "Struct"))
end = time.time()
elapsed = (end - start) * 1000
print("Execution time:", f"{elapsed:.3f} ms")

start = time.time()
print("Index:", index("Operating Systems", "Systems"))
end = time.time()
elapsed = (end - start) * 1000
print("Execution time:", f"{elapsed:.3f} ms")
