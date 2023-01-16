# 格子状の経路 r行c列の経路の通り数
def countroute_m(n,m): # 行数と列数を指定
    def countroute(row, col): # インデックスを指定
        if row==0 or col==0:
            return 1
        elif memo[row][col] != 1: # メモが記録されている
            return memo[row][col]
        else:
            memo[row][col] = countroute(row, col-1) + countroute(row-1, col)
            return memo[row][col]
    
    memo = [[1 for _ in range(m)] for _ in range(n)]
    return countroute(n-1, m-1)

print(countroute_m(6,6))
