import csv
import os

data = [ {"品名": "台積電", "股價": 800, "評等": "買進"},
    	{"品名": "聯發科", "股價": 1000, "評等": "持有"},
    	{"品名": "鴻海", "股價": 150, "評等": "買進"}]

file_name = "stocks.csv"

# 存取文件的步驟
# 1. 開啟/建立文件
# 2. 讀取/寫入文件
# 3. 關閉文件

def save_csv(data, file_name):
    with open(file_name, mode="w", encoding="utf-8-sig", newline="") as f:
        fieldnames = ["品名","股價","評等"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(data)


def read_csv(file_name):
    with open(file_name, mode="r", encoding="utf-8-sig") as f:
        
        reader = csv.DictReader(f)
        for row in reader:
            print(row)


def append_csv(file_name):
    name = input("品名：")
    price = int(input("股價："))
    grade = input("評等：")
    
    new_data = {"品名": name, "股價": price, "評等": grade}

    not_exist = False

    if not os.path.exists(file_name):
        not_exist = True

    with open(file_name, mode="a", encoding="utf-8-sig", newline="") as f:
        fieldnames = ["品名","股價","評等"]
        writer = csv.DictWriter(f, fieldnames = fieldnames)
        if not_exist:
            writer.writeheader()
            
        writer.writerow(new_data)


save_csv(data, file_name)

while True:
    append_csv(file_name)
    read_csv(file_name)
    yes_or_no = input("是否繼續(y/n)：")
    if yes_or_no=="n":
        break





