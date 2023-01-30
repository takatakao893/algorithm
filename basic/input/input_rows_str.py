import sys
# 複数行の入力 -> 文字列
'''
echo $'Ex\nCalibur' | python input_rows_str.py
'''
data = sys.stdin.read()
print(data)