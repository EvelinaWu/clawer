import csv
import os 

new_data = {"品名":"新產品X","股價":500,"評等":"觀察"}
      
file_name = "stocks_2-1_1.csv"
        
        
with open(file_name,mode="w",encoding="utf-8-sig", newline="")as f:
     fieldnames =["品名","股價","評等"]
     writer = csv.DictWriter(f, fieldnames = fieldnames) 
     writer.writeheader() ##可以在csv檔案裡加入欄位名稱
     writer.writerow(new_data)##將資料寫進去


     with open(file_name,mode="w",encoding="utf-8-sig", newline="")as f:
    
     fieldnames =["品名","股價","評等"]
     writer = csv.DictWriter(f, fieldnames = fieldnames) 
        ##把你的資料匯出成csv檔 csv.Dicwriter
     if not_exist:
          writee.writeheader()
     writer.writeheader() ##可以在csv檔案裡加入欄位名稱
     writer.writerow(new_data)##將資料寫進去


with open(file_name, mode="f",encoding= "utf-8-sig") as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(row)

new_data = {"品名":"新產品X","股價":500,"評等":"觀察"}
not_exist = False

if not os.path.exists(file_name):
     not_exist = True 
     
with open(file_name,mode='a', encoding="utf-8-sig" , newline="") as f:
  filenames = ["品名","股價","評等"]
  writer = csv.Dicwriter(f,fieldnames = fieldnames) 
  if not_exist:
    writer.writeheader()
    
  writer.writerow(new_data)
