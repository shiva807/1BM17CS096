class paren:
  def __init__(self):
      self.open=[]
      self.i=None
 
  def checkvalid(self, str):
     valid=False
     for each in str:
         if each=='(' or each=='{' or each=='[':
            self.open.append(each)
         elif each==')' or each=='}' or each==']':
            if len(self.open)!=0:
               self.i = self.open.pop()
            else:
               self.i=None

         if each==')' and self.i=='(':
            valid=True
         elif each=='}' and self.i=='{':
            valid=True
         elif each==']' and self.i=='[':
            valid=True
         else:
            valid=False

     if len(self.open)!=0:
        valid=False
     
     if(valid):
       print("Valid string..")
     else:
       print("Invalid string..")


p=paren()
print(p.checkvalid("[[({})]]"))
