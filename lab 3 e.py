import time

def find_indices(S, a):
    return [i for i, ch in enumerate(S) if ch == a]

start = time.time()
print("Indices:", find_indices("banana", "a"))
end = time.time()
elapsed = (end - start) * 1000
print("Execution time:", f"{elapsed:.3f} ms")

start = time.time()
print("Indices:", find_indices("programming", "m"))
end = time.time()
elapsed = (end - start) * 1000
print("Execution time:", f"{elapsed:.3f} ms")
