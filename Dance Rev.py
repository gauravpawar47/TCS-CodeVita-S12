def minimum_moves(instruct):
    directions = ["up", "down", "left", "right"]
    s = len(instruct)
    dp = [[[float('inf')] * 4 for _ in range(4)] for _ in range(s + 1)]
    
    for i in range(4):
        for j in range(4):
            dp[0][i][j] = 0
    # @placementlelo
  
    for k in range(1, s + 1):
        instr_idx = directions.index(instruct[k - 1])
        for i in range(4):
            for j in range(4):
                if dp[k - 1][i][j] != float('inf'):
                    if instr_idx == i or instr_idx == j:
                        dp[k][i][j] = min(dp[k][i][j], dp[k - 1][i][j])
                    else:
                        dp[k][i][j] = min(dp[k][i][j], dp[k - 1][instr_idx][j] + 1, dp[k - 1][i][instr_idx] + 1)
    
    minimum_moves = float('inf')
    for i in range(4):
        for j in range(4):
            minimum_moves = min(minimum_moves, dp[s][i][j])
    # @placementlelo
    return minimum_moves

if name == "main":
    m = int(input().strip())
    instruct = [input().strip() for _ in range(m)]
    result = minimum_moves(instruct)
    print(result, end="")

