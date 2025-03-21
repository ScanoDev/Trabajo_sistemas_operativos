def first_fit(memory: list, req: int, index: int):
    original_length = len(memory)
    n = original_length
    for offset in range(n):
        i = (index + offset) % n
        base, size = memory[i]
        
        if(size >= req):
            new_base = base + req
            new_size = size - req
            
            if(new_size == 0):
                memory.pop(i)
                if(i == original_length - 1):
                    return (memory, new_base, new_size, 0)
                else:
                    return (memory, new_base, new_size, i)
            else:
                memory[i] = (new_base, new_size)
                return (memory, new_base, new_size, i)
    return None
