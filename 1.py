

periviouscourses=input("Please enter the courses you have taken previously with letter grades: ")


if ( periviouscourses.count(":") == periviouscourses.count(";") +1 )  == True: 
 currentcourses=input("Please enter the courses you have taken this semester with letter grades: ")
 if (currentcourses.count(":") == currentcourses.count(";") +1 ) == True:
  
  currentcourses=currentcourses.replace(":",";")
  currentcourses= currentcourses.split(";")
  periviouscourses=periviouscourses.replace(":",";")
  periviouscourses= periviouscourses.split(";")
  
  checkcourse=input("Please enter the course you want to check: ")
 
  if checkcourse in currentcourses:
    ind1=currentcourses.index(checkcourse)
    
  
    list1=["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "a", "a-", "b+", "b", "b-", "c+", "c", "c-", "d+", "d"]
    list2= ["f","F"]
    list3=["U","u"]
    if currentcourses[ind1+1] in list1:
     print("You can choose between", "S and", currentcourses[ind1+1].capitalize(), "for", checkcourse, end="." )
    else:
      if checkcourse in periviouscourses:
        ind3=periviouscourses.index(checkcourse)
        
        if periviouscourses[ind3+1] in list1 or periviouscourses[ind3+1] in list2:
         print("Your grade for", checkcourse, "is F." )
        elif periviouscourses[ind3+1] in list3:
          print("Your grade for", checkcourse, "is U.")
      else:
        print("Your grade for", checkcourse, "is U.")
  else:
     print("You didn't take", checkcourse ,"this semester." )
 else:
    print("Invalid input")
else:
  print("Invalid input")
