

print("Welcome to the new years night fun(!)")
grandmacard=input("plese enter tombala card for your grandma:")
mycard=input("Please enter the Tombala card for You: ")
drawn=input("Please enter the numbers drawn in the order:")



status=""
status2=""
remaning=""


grandmacard=grandmacard.split("-")
mycard=mycard.split("-")
drawn=drawn.split("-")


for x in drawn:
    if x in mycard:
        status="you have it"
        mycard.remove(x)
    else:
      status=""
    if x in grandmacard:
        status2="grandma has it"
        grandmacard.remove(x)
    else:
      status2=""
    if len(mycard) == 0 or len(grandmacard) == 0:
        break
    print("Number",x,"is drawn.",status,status2)
  
if len(mycard) ==0 and len(grandmacard) == 0:
  print("it is a tie")

elif len(grandmacard) == 0:
  print("grandma wins")
  #converting list to a string
  for z in mycard:
    remaning= remaning + z
    remaning= remaning= + "-"
  remaning=remaning[:len(remaning)-1]
  print(remaning)

elif len(mycard) ==0:
  print("you win")
  #converting list to a string
  for y in grandmacard:
    remaning= remaning + y
    remaning= remaning= + "-"
  remaning=remaning[:len(remaning)-1]
  print(remaning)
