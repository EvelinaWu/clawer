import json


raw_data = '''
    {
        "status":"success",
        "results":[
            {"id":1,
             "info": {
                 "name":"台北",
                 "weather":"雨"
                 }
            },
            {"id":2,
             "info": {
                 "name":"台中",
                 "weather":"晴"
                }
            }
        ],
        "demo":null
    }
'''

try:
    data = json.loads(raw_data)
    print(data)
##    n  ##用來測試變數未定義的錯誤
    print("台中天氣：",data["results"][1]["info"]["weather"])
except json.decoder.JSONDecodeError:
    print("JSON格式有錯")
except NameError:
    print("變數未定義")
except Exception: # 越上層的例外類別盡量放在後面
    print("丟出例外")





