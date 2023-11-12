import re
import sys

def match_lines_with_numbers(filename, callback):
    matched_lines = []
    
    with open(filename, 'r') as file:
        ls = file.readlines()
        for i, line in enumerate(ls):
            match = re.search(r'\[(\d+)\]', line)  # 괄호 안에 숫자를 찾는 정규표현식 패턴
            if match:
                number = match.group(1)
                callback(i, line.strip(), int(number))

# 파일 경로 설정
filename = 'a.c'

max_size = 0
def call(linenumber, line, count):
    global max_size
    if max_size < count:
        max_size = count
    # print(f"{linenumber}, {count}");


match_lines_with_numbers(filename, call)

print(max_size)