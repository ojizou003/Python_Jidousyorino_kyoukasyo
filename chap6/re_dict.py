import re

dict_file = "./ejdict-hand-utf8.txt"

while True:
    print("正規表現を入力してください。[q]で終了。")
    re_str = input()
    if re_str == "":
        continue
    if re_str == "q":
        break
    with open(dict_file, "rt", encoding="utf-8") as f:
        cnt = 0
        while True:
            line = f.readline()  # 1行だけ読む
            if not line:
                break
            word, mean = line.split("\t")
            if re.search(re_str, word):
                print(word)
                cnt += 1
                if cnt > 50:  # 最大50件
                    break
