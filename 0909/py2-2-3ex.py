import json
import requests

##data =[
## {
##   "機構名稱": "森美牙醫診所",
##   "縣市別代碼": "10018",
##   "行政區域代碼": "10018020",
##   "街道項弄號": "大同里中正路111號1樓、2樓",
##   "負責人": "李森孟",
##   "電話": "(03)5260203"
## },
## {
##   "機構名稱": "黃啟祥牙醫診所",
##   "縣市別代碼": "10018",
##   "行政區域代碼": "10018020",
##   "街道項弄號": "和福街105號",
##   "負責人": "黃啟祥",
##   "電話": "(03)5269095"
## },
## {
##   "機構名稱": "福華牙醫診所",
##   "縣市別代碼": "10018",
##   "行政區域代碼": "10018020",
##   "街道項弄號": "育英里四維路54號1樓",
##   "負責人": "吳英法",
##   "電話": "(03)5262345"
## },
## {
##   "機構名稱": "親民牙醫診所",
##   "縣市別代碼": "10018",
##   "行政區域代碼": "10018020",
##   "街道項弄號": "竹光路２１號",
##   "負責人": "黃宏正",
##   "電話": "(03)5427027"
## },
## {
##   "機構名稱": "如意牙醫診所",
##   "縣市別代碼": "10018",
##   "行政區域代碼": "10018020",
##   "街道項弄號": "光田里水田街131號",
##   "負責人": "呂正德",
##   "電話": "(03)5422765"
## }
##]

url = "https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/106/94b0e54b-ad45-4222-b26c-648773794ded.json"

try:
    response = requests.get(url, timeout=20, verify=False)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.SSLError as e: 
    print("丟出requests.exceptions.SSLError例外，SSLCertVerificationError")
    print(e)

with open("dental_clinics.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


with open("dental_clinics.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    for clinic in loaded_data:
        print(clinic["機構名稱"], clinic["電話"])
##        for field in clinic:
##            print(clinic[field])

        print()

# 任務
# 根據範例2-2-1、2-2-2、2-2-3所學的技巧
# 1. 將以上的資料輸出成 json文件
# 2. 讀取該json文件，並顯示各家診所的名字和電話



