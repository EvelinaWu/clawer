import csv
import os

data = [{"品名":"台積電","股價":800,"評等":"買進"},
        {"品名":"聯發科","股價":1000,"評等":"持有"},  
        {"品名":"鴻海","股價":150,"評等":"買進"}]

file_name = "stocks.csv"
        
        #如何將資料匯出csv的檔案(考試會考)
         #with會幫忙簡短程式
         ##一般在文件存取的時候會有 個步驟
         ##1.開啟/建立文件 2.讀取/寫入文件 3.(自動關閉)關閉文件

         ##寫入或是匯出 會覆蓋現有的資料 A

        ##編碼方式用UTF8
        
with open(file_name,mode="w",encoding="utf-8", newline="")as f:
     fieldnames =["品名","股價","評等"]
     writer = csv.DictWriter(f, fieldnames = fieldnames) #轉換成一個串流物件
        ##把你的資料匯出成csv檔 csv.Dicwriter
     writer.writeheader() ##可以在csv檔案裡加入欄位名稱
     writer.writerows(data)##將資料寫進去

#底下程式是用來讀取
with open(file_name,mode="w",encoding="utf-8")as f:

     reader = csv.DictReader(f) ##希望讀取進來的資料是字典模式
     for row in reader:
         print(row)
         
