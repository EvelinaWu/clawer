class Student():
  
  def __init__(self, name, age, phone):
    self.name = name 
    self.age = age 
    self.phone = phone 
    
  def take_exam(self):
    print(self.name,"參加考試") #加上誰參加了這個考試
    
  def write_homework(self):
   print(self.name,"寫作業")
   
s1 = Student("羅同學",35,"0912345678")
print(s1.name)
print(s1.age)
print(s1.phone)


s1.take_exam()
s1.do_homework()
#你要物件執行一個事情要 
#看屬性資料就是用下面這個方法#print(s1.name)
