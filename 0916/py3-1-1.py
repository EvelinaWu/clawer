# raw_data =[
#   {"item":"iphone 15","price":"$29,900"},
#   {"item":"iphone 15","price":"$29,900"},
#   {"item":"ipad Air","price":"$19,500"},
#   {"item":"Macbook","price":"$None"} #缺失值
# ]

# s="$29.900" #python的字串具有immutable(不可變)特性

# s="abcd"
# s="xyz" 

# print(s is S2)#這兩個物件不是同個
# print(s.replace("$",""))
# print(s.replace(", "" "))

# print(s.replace("$","").replace(","))

# class Student:
#    def __init__(self,name,age):
#        self.age=age
       
#    def set_age(self,age):
#        self.age=age
  
#    def get_age(self):
#      return self.age
   
# s1 = Student("Alice",20)
# print(s1.get_age())

# s2 = s1
# s2 = set.age(25)

# print("s2.age=",s2 get_age())
# print("s1.age=",s1 get_age())
# print(s1 is s2)

#請同學將所有商品的價格的價格字串中的"$"和","移除，並將結果轉換為整數
raw_data =[
  {"item":"iphone 15","price":"$29,900"},
  {"item":"iphone 15","price":"$29,900"},
  {"item":"ipad Air","price":"$19,500"},
  {"item":"Macbook","price":"$None"} #缺失值
]

#可以用 迴圈

for item in raw_data:
  print (item)
  # item ["price"] =item["price"].replace("$","").replace(",","")
  # print(item["price"])
  
  price =item["price"]
  
#從表面上看起來真的被修改，若要真的要修改，最好還是把整個raw_data拉出來修改


#我們要如何去除重複 

#print(raw_data)

raw_data = [10,10,20,20,30,30]

# #去除重複資料
# #raw_data =[10,20,30]

# del raw_data[-1]
# print(raw_data)

# raw_data.remove(10)
# print(raw_data)

# print(raw_data.count(20))


# for item in raw_data:
#   count = raw_data.count(item)
#   if count>=2:
#     raw_data.remove(item)
    



# for item in raw_data:
#   count = raw_data.count(item)
#   if count>=2:
#     for i in range(count-1)
#      raw_data.remove(item)
    
    
    
    
#-------------------------------------------------
import pandas as pd

raw_data =[
  {"item":"iphone 15","price":"$29,900"},
  {"item":"iphone 15","price":"$29,900"},
  {"item":"ipad Air","price":"$19,500"},
  {"item":"Macbook","price":"None"} #缺失值
]

# 目的是用來處理表格的二維資料 ，所以也需要先是先確認是否是要的資料

# df = pd.DataFrame(raw_data)#最適合處理 list+dict 格式的資料
# print(df)


#純字典的資料無法使用DataFrame
# df2 = pd.DataFrame({"item":"iphone 15","price":"$29,900"}) 
# print(df2)

# df3 = pd.DataFrame([10,30,60,50,40]) #純list 也可以
# print(df3)


# df.drop_duplicates() #有些方法
# print(df)

# df = df.reset_index(drop=True) #重設為連續的編號
# print(df)

# #利用字典的方式做取代
# df['price'] = df['price'].str.replace("$","").replace(",","")#用前面的寫法複製兩次
# print(df)


# df['price'] = pd.to_numeric(df['price'],errors="coerce")
# print(df)


# #3-1-2___________________________________
# import pandas as pd

# df = pd.DataFrame(
#   {
#      "城市":["台北","台中","高雄"],
#      "溫度":[25,28,30]
#   }
# )


# print(df)

# print("平均溫度:",df["溫度"].mean())

# #加上round會有甚麼影響
# print("平均溫度:",round(df["溫度"].mean(),1))


#真實的天氣資料
# import pandas as pd
# import json

# with open(r"C:\Users\abc\Downloads\F-C0032-027.json",encoding="utf-8")as f:
#   data = json.load(f)
#   print(data)
  
  
# df = pd.DataFrame(data)


#------------------------------------------------

import pandas as pd
import json

with open(r"C:\Users\User\Downloads\F-C0032-027.json",encoding="utf-8")as f:
  data = json.load(f)
  print(data)
#   print()
#   print("溫度:",data["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
  
df = pd.DataFrame(data)
# print(df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])
print("溫度:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] )
print("溫度:")

#要如何取值取在溫度的前後  程式如下----------------------------

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])

temp_data = df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] 
print("溫度:",temp_data)

start = temp_data.index("溫")+1
end = temp_data.index("至")
print("最小溫度:", temp_data[start:end])

start = temp_data.index("至")+1
end = temp_data.index("度")
print("最大溫度:", temp_data[start:end])


#宜蘭----------------------------

import pandas as pd
import json

with open(r"C:\Users\User\Downloads\F-C0032-013.json",encoding="utf-8")as f:
  data = json.load(f)
  print(data)
#   print()
#   print("溫度:",data["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
  
df = pd.DataFrame(data)
# print(df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])
print("溫度:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] )
print("溫度:")

#要如何取值取在溫度的前後  程式如下----------------------------

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])

temp_data = df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] 
print("溫度:",temp_data)

start = temp_data.index("溫")+1
end = temp_data.index("至")
print("最小溫度:", temp_data[start:end])

start = temp_data.index("至")+1
end = temp_data.index("度")
print("最大溫度:", temp_data[start:end])


#南投----------------------------
import pandas as pd
import json

with open(r"C:\Users\User\Downloads\F-C0032-026.json",encoding="utf-8")as f:
  data = json.load(f)
  print(data)
#   print()
#   print("溫度:",data["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
  
df = pd.DataFrame(data)
# print(df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])
print("溫度:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] )
print("溫度:")

#要如何取值取在溫度的前後  程式如下----------------------------

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])

temp_data = df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] 
print("溫度:",temp_data)

start = temp_data.index("溫")+1
end = temp_data.index("至")
print("最小溫度:", temp_data[start:end])

start = temp_data.index("至")+1
end = temp_data.index("度")
print("最大溫度:", temp_data[start:end])

#嘉義----------------------------
import pandas as pd
import json

with open(r"C:\Users\User\Downloads\F-C0032-018.json",encoding="utf-8")as f:
  data = json.load(f)
  print(data)
#   print()
#   print("溫度:",data["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
  
df = pd.DataFrame(data)
# print(df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])
print("溫度:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] )
print("溫度:")

#要如何取值取在溫度的前後  程式如下----------------------------

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])

temp_data = df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] 
print("溫度:",temp_data)

start = temp_data.index("溫")+1
end = temp_data.index("至")
print("最小溫度:", temp_data[start:end])

start = temp_data.index("至")+1
end = temp_data.index("度")
print("最大溫度:", temp_data[start:end])

#新北----------------------------
import pandas as pd
import json

with open(r"C:\Users\User\Downloads\F-C0032-010.json",encoding="utf-8")as f:
  data = json.load(f)
  print(data)
#   print()
#   print("溫度:",data["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
  
df = pd.DataFrame(data)
# print(df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])
print("溫度:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] )
print("溫度:")

#要如何取值取在溫度的前後  程式如下----------------------------

 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])

temp_data = df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] 
print("溫度:",temp_data)

start = temp_data.index("溫")+1
end = temp_data.index("至")
print("最小溫度:", temp_data[start:end])

start = temp_data.index("至")+1
end = temp_data.index("度")
print("最大溫度:", temp_data[start:end])


#新北----------------------------
import pandas as pd
import json

with open(r"C:\Users\User\Downloads\F-C0032-010.json",encoding="utf-8")as f:
  data = json.load(f)
  
  
  # print(data)

df = pd.DataFrame(data)
 
print("縣市:", df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"])

temp_data = df ["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1] 

start = temp_data.index("溫")+1
end = temp_data.index("至")
print("最小溫度:", temp_data[start:end])

start = temp_data.index("至")+1
end = temp_data.index("度")
print("最大溫度:", temp_data[start:end])




start = temp_data.index("溫")+1
end = temp_data.index("至")
print("最小溫度:", temp_data[start:end])

start = temp_data.index("至")+1
end = temp_data.index("度")
print("最大溫度:", temp_data[start:end])


#________________________________

import pandas as pd
import json

files = ["F-C0032-027.json","F-C0032-026.json","F-C0032-018.json","F-C0032-013.json","F-C0032-010.json"]

root_path = r"C:\Users\user\Downloads"

for file in files:
  full_path = root_path +"\\"+file
  
  with open (full_path,encoding="utf-8") as f:
  data = json.load(f)
  
  df = pd.DataFrame(data)
  print("縣市:")  
  