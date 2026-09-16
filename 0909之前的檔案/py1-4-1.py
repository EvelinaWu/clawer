import os
import shutil

source = "today_spider.log"
target_dir ="history_logs"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"建立資料夾:{target_dir}")

if os.path.exists(source):
    shutil.move(source, os.path.join(target_dir,"old.log"))
    print(f"日誌已歸檔")
    

