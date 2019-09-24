class student:
  def __init__(self):
      self.id=0
      self.age=0
      self.marks=0
      
  def validate_marks(self):
     if self.marks>=0 and self.marks<=100:
        return True
     else:
        return False
        
  def validate_age(self):
     if self.age>20:
        return True
     else:
        return False
        
  def check_qualification(self):
      if self.validate_marks() and self.validate_age():
          if self.marks>=65:
             return True
          else:
             return False
      else:
         return False
         
  def setvalues(self):
    print("Enter student id, age, marks:")
    self.id=int(input())
    self.age=int(input())
    self.marks=int(input())
    
  def getvalues(self):
    if self.check_qualification():
       print("Id:", self.id)
       print("Age:", self.age)
       print("Marks:", self.marks)
    else:
       print("Sorry! You cannot be admitted.")
    
  
ob=student()
ob.setvalues()
ob.getvalues()
