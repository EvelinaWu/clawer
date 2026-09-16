import os
import shutil

source = "today_spider.log"
target_dir ="history_logs"

##反向縮排:選取後左中括號 往左縮排 反之也可



##檢查目標資料夾是否存在
if not os.path.exists(source_file):
    print(f"找不到來源檔案{source_file}")
    return

##檢查檔案來源是否存在，若存在就做搬移的動作 shutil.move的方法
  if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print(f"建立資料夾:{target_folder}")
    
backup_file("settings.json","my_backups")

##目標參數當作目的地，一方面搬過去在改檔案名稱
##做測試前要先建立一個source同樣的名稱 

import os
import shutil

source = "today_spider.log"
target_dir ="history_logs"

if not os.path.exists(target_file):
    os.makedirs(target_dir)
    print(f"建立資料夾:{target_dir}")

 if os.path.exists(source):
    shutil.move(source, os.path.join(target_dir,"old.log"))
    print(f"日誌以歸檔")
    

