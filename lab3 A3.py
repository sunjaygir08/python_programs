import time

def substring(s, ip, length):
    return s[ip:ip+length]

start = time.time()
print("Substring:", substring("Cray is a supercomputer", 16, 8))
end = time.time()
elapsed = (end - start) * 1000
print("Execution time:", f"{elapsed:.3f} ms")

start = time.time()
print("Substring:", substring("Unix is a multi-user operating system", 24, 6))
end = time.time()
elapsed = (end - start) * 1000
print("Execution time:", f"{elapsed:.3f} ms")
