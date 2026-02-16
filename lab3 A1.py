import time

def length(s):
    count = 0
    for char in s:
        count += 1
    return count

s1 = "A computer is an idiot machine"
s2 = "Data Structures is a prerequisite for compiler construction"

start = time.time()
print("Length:", length(s1))
end = time.time()
elapsed = (end - start) * 1000 # convert to milli sec 
print("Execution time (length):", f"{elapsed:.3f} ms")
start = time.time()
print("Length:", length(s2))    
end = time.time()
elapsed = (end - start) * 1000 # convert to milli sec  
print("Execution time (length):", f"{elapsed:.3f} ms")
