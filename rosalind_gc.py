file_name = "rosalind_gc.txt"
l_num = []
l_c = []
l_g = []
l_len = []
l_cont = []
s = ""
with open(file_name, "r") as handle:
    for line in handle:
        s += line  # line들을 하나의 문자열로
    s = s.replace("\n", "")  # \n 없애기
list = s.split(">")  #'>'기준으로 list만들기.
list.remove("")  # list의 첫번째요소가 공백이라서 지워줌.
for i in range(len(list)):
    l_num.append(list[i][:13])  # >Rosalind_3417
    l_c.append(list[i].count("C"))
    l_g.append(list[i].count("G"))
    l_len.append(len(list[i][13:]))  # 염기서열만 포함한 seq의 길이
    l_cont.append((l_c[i] + l_g[i]) / (l_len[i]) * 100)  # gc 비율 계산
print(l_num[l_cont.index(max(l_cont))])  # gc비율이 가장 큰 부분의 첫번쨰 줄 출력.
print(round(max(l_cont), 6))  # gc비율의 최댓값 출력.
