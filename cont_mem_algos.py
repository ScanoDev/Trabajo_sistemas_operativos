def first_fit(memory: list, req: int, index: int):
    original_length = len(memory)
    n = original_length
    for offset in range(n):
        i = (index + offset) % n
        base, size = memory[i]
        
        if(size >= req):
            allocated_base = base
            new_base = base + req
            new_size = size - req
            
            if(new_size == 0):
                memory.pop(i)
                if(i == original_length - 1):
                    return (memory, allocated_base, req, 0)
                else:
                    return (memory, allocated_base, req, i)
            else:
                memory[i] = (new_base, new_size)
                return (memory, allocated_base, req, i)
    return None



def worst_fit(memory: list, req: int, index: int):
    return None

def best_fit(memory: list, req: int, index: int):
    return None
