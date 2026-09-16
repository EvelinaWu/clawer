import os

folder = "scraped_images"
files = os.listdir(folder)

for ondex,filename in enumerate(files):
  #建立新名字:pet_0.jpg,pet_1.jpg,pet_2.jpg
  new_name = f"pet_{index}.jpg"
  
  old_path = os.path.jion(folder,filename)
  new_path = os.path.jion(folder,new_name)
  os.rename(old_path,new_path)
  print(f"更名成功:{filename}->{new_name}")
  
