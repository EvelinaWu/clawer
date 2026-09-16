import json
##為了方便記錄複雜字串就有了用三引號的方式
raw_data = '''

    {
       "status":"success",
       "result":[
           {"id":1,
            "info": {
                "name":"台北",
                "weather":"雨"
                }
           },
           {"id":2,
            "info":{
                  "name":"台中",
                  "weather":"晴"
              }
           }
       ]
    }
 '''

try:
    data = json.loads(raw_data)
##    n ##用來測試變數未定義的錯誤
    print("台中天氣:",data["results"][1]["info"]["weather"])
except Exception:
    print("丟出例外")
except json.decoder.JSONDecodeError:
    print("JSON格式有錯")
except NameError: #越上層的類別盡量放在後面
    print("變數未定義")


