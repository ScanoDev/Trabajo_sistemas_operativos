
def FirstFit(memory: list, req: int, index: int):
    for index in range(index, len(memory)):
        if(memory[index][1]-req >= 0):
            oldBase = memory[index][0]
            memory[index][0]+=req
            memory[index][1]-=req
            return (memory, memory[index][0], memory[index][1], oldBase, index)
    return None

def main():
    memoria = [[0x04800000, 0x00a00000],
            [0x01e00000, 0x00400000],
            [0x02500000, 0x01400000],
            [0x07201800, 0x01200000],
            [0x08402c00, 0x00700000],
            [0x06d01000, 0x00500000],
            [0x06100c00, 0x00c00000],
            [0x05200400, 0x00f00000]]
    req = 0x01000000
    index=0
    print(FirstFit(memoria, req, index))
    #print(0x014000000-req)

if __name__ == "__main__":
    main()