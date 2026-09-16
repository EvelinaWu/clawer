import csv
import os 

new_data = {"品名":"新產品X","股價":500,"評等":"觀察"}
      

file_name = "stocks_2-1_1.csv"
        
        #如何將資料匯出csv的檔案(考試會考)
        #with會幫忙簡短程式
        ##一般在文件存取的時候會有3個步驟
        ##1.開啟/建立文件 2.讀取/寫入文件 3.(自動關閉)關閉文件

        ##寫入或是匯出 會覆蓋現有的資料 A

        ##編碼方式用UTF8
        
with open(file_name,mode="w",encoding="utf-8-sig", newline="")as f:
     writer.writeheader() ##可以在csv檔案裡加入欄位名稱

     fieldnames =["品名","股價","評等"]
     writer = csv.DictWriter(f, fieldnames = fieldnames) 
        ##把你的資料匯出成csv檔 csv.Dicwriter
     writer.writerow(new_data)##將資料寫進去

         

##這裡開始
     ##可以先判斷檔案是否存在，先給一個變數

     if not os.path.exists(file_name):
          not_exist = True

     with open(file_name,mode="w",encoding="utf-8-sig", newline="")as f:
     writer.writeheader() ##可以在csv檔案裡加入欄位名稱

     fieldnames =["品名","股價","評等"]
     writer = csv.DictWriter(f, fieldnames = fieldnames) 
        ##把你的資料匯出成csv檔 csv.Dicwriter
     if not_exist:
          writee.writeheader()
     
     writer.writerow(new_data)##將資料寫進去
