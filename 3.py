

def mefunction(x):
  list1=["+","-","/","*"]
  
  length=len(x)
  for y in x:
    if y in list1:
      n=x.count(y)
      if n ==1:
        if x[0] != y and x[length-1] != y:               #input checking fnc
          x=x.split(y)
          if x[0].isdigit() and x[1].isdigit :
            return True
      
while True:     
  operation=input("plese enter an operation:")     
  r=mefunction(operation)                                #putting user given input to my function
 
  if operation == "stop":
    print("bye...")
    break
  else:
    if r :
      def mfunction(x):
        list1=["+","-","/","*"]
  
        for z in x:
          if z in list1:
            #ind=x.index(z)
            x=x.split(z)
            operator=z
            operant1=x[0] 
            operant2= x[1]

        if operator == "+":
          return (int(x[0])+int(x[1]))
        elif operator == "-":
          return (int(x[0])-int(x[1]))
        elif operator == "/":
          return (int(x[0])/int(x[1]))
        elif operator == "*":
          return (int(x[0])*int(x[1]))
      
        

      print(mfunction(operation))
      


    else:
      print("Invalid arithmetic operation!")
