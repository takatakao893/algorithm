import sys
'''
sys.stdin.realine()をEOFに達するまで
EOFに到達すると空文字列返す
echo $'EX\nCalibur\nabc\ndef' | python input_row_loop.py
'''

while True:
    line = sys.stdin.readline().rstrip()
    if not len(line):
        break
    print(line)