def Percent(seq):
    G_count = seq.count("G")  #
    C_count = seq.count("C")  #
    Total_count = len(seq)
    GC_Sum = int(G_count) + int(C_count)
    Percent_GC = float(GC_Sum / Total_count)  #
    Per_GC = Percent_GC * 100  #
    return Per_GC


File = open("rosalind_gc.txt", "r")

fasta_dic = {}
seq_name = ""

for line in File:
    line = line.strip()
    if line.startswith(">"):
        seq_name = line[1:]
        fasta_dic[seq_name] = ""
    else:
        seq = line
        fasta_dic[seq_name] += seq  ## 1. =을 +=으로 바꿈!
File.close()
print("fasta_dic: ", fasta_dic)
# 딕셔너리에 담긴 각 시퀀스에 해당하는 GC values
dictionary = dict()
for seq_name in fasta_dic:
    dictionary[seq_name] = float(Percent(fasta_dic[seq_name]))  # 레알넘버 취급 int는정수
print("dictionary: ", dictionary)
# 제일 높은 거
for seq_name, seq in fasta_dic.items():
    inverse = [(seq, seq_name) for seq_name, seq in dictionary.items()]
    highest_GC = max(inverse)[1]
print("highest_GC: ", highest_GC)
# 해당 시퀀스 이름 찾기
# for seq_name, seq in fasta_dic.items():
#     #print(seq_name, seq)
#     if seq == highest_GC:  # seq는 염기서열(CGAACACCGCACGACGC...)이므로 highest_GC(Rosalind_3417)과 같을 수 없다.
#         print(seq_name + " " + highest_GC)  # 그래서 print안됨.
for seq_name, seq in dictionary.items():  # 2. fasta_dic->dictionary
    # print(seq_name, seq)
    if seq_name == highest_GC:
        print(seq_name, "\n", round(seq, 6))  # 3.  highest_GC- >seq
