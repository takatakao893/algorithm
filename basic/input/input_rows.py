import sys
# 複数行の入力 -> リスト
'''
echo $'Ex\nCalibur' | python input_rows.py
'''
data = sys.stdin.readlines()

print(data)