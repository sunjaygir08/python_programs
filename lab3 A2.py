import time

def concatenate(s1, s2):
    return s1 + s2

start = time.time()
print("Concatenation:", concatenate("But", "ter"))
end = time.time()
elapsed = (end - start) * 1000  # convert to ms
print("Execution time:", f"{elapsed:.3f} ms")

start = time.time()
print("Concatenation:", concatenate("Symmetric ", "Multiprocessing"))
end = time.time()
elapsed = (end - start) * 1000
print("Execution time:", f"{elapsed:.3f} ms")
