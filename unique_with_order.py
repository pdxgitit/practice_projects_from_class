import time

def remove_dups(list):
    output = []
    for item in list:
        if item not in output:
            output.append(item)
    return output

start = time.time()
results = remove_dups(range(0, 10000))
end = time.time()

print 'Time to execute: ', end - start
print results
