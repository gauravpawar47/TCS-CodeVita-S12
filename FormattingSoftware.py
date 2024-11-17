# Formatting Software Solution in PYTHON
# SUBSCRIBE OUR CHANNEL "EDUTECH BARSHA"
def main():
    n, r, c = map(int, input().split())
    matrices = []
    
    for _ in range(n):
        matrix = []
        for _ in range(r):
            row = list(map(int, input().split()))
            matrix.append(row)
        matrices.append(matrix)

    try:
        while True:
            m = int(input()) - 1
            for i in range(r):
                print(" ".join(map(str, matrices[m][i])))
            print()
    except EOFError:
        pass

if __name__ == "__main__":
    main()