import os
import shutil
import glob

source = r"C:\Users\python_idle_code\my_backups"
target_dir =r"C:\Users\python_idle_code\history_logs"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"建立資料夾:{target_dir}")

ini_files = glob.glob(os.path.join(source,"*.*"))
for file in ini_files:
    file_name = os.path.basename(file)
    new_file = "old_"+file_name
    shutil.copy(file, os.path.join(target_dir,new_file))
    print(file,new_file)

#任務
#1.先用 py1-4.py在主目線下(例如C:(Users(Useripython_idle code)建立多個不同的檔案・例加
# 20260902_095049_data.txt
# 20260902_095539_data.txt
# 20260902_101029_data.txt
#2.透過 py1-4-1將這些檔案自動搬移到 history_logs 目錄
# 並自動改檔名為
# old_2026002_095049_data.txt
# old_20260902_095539_data.txt
#old_20260902_101029_data.txt

import os
import shutil
import glob
source = "*data*.txt" #含有data名字的檔案
target_dir = "history_logs" #目標資料夾

for source in glob.glob("*data*.txt"):
    if os.path.exists(source):
        shutil.move(source, os.path.join(target_dir, f"old_{source}"))
        print(f"已將 {source} 移動到 {target_dir}/old_{source}")

##原本

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
    
##老師改的


import os
import shutil

target_dir ="history_logs"

def move_file(source):
  if not os.path.exists(target_dir):
    os.makedirs(target_dir)
    print(f"建立資料夾:{target_dir}")

  if os.path.exists(source):
    shutil.move(source, os.path.join(target_dir,"old_"+source))
    print(f"日誌已歸檔")


print(os.listdir("."))

for f in os.listdir("."):
    if os.path.isfile(f):
        if "txt" in f:
            move_files(f)
            print(f)
















