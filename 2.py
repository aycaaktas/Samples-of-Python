

movieinfo=input("Please enter movie names and remaining quota: ")
movieinfo=movieinfo.replace(",",":")
movies=movieinfo.split(":")
seats=0
index=-1
genreposition=-1

checkedmovies=[]
checkedseats=[]
lastlist=[]

#print(movies)

moviewanna=input("Please enter the movie you want to watch: ")
if moviewanna in movies:
  people=int(input("Please enter the number of tickets you want to buy: "))
  b=movies.count(moviewanna)


  if b >1: 
    for x in range(1,b+1):
      index=movies.index(moviewanna,index+1)
      seats= seats + int(movies[index+1])
  else:
      index=movies.index(moviewanna)
      seats=movies[index+1] 


  if int(seats) >= people:
    print("The reservation is done!")

  else:
    genre=movies[index+2]
    c=movies.count(genre)
    if c >1:
      for y in range(1,c+1):
        genreposition=movies.index(genre,genreposition+1)
        if moviewanna != movies[genreposition-2]:
          if movies[genreposition-2] not in checkedmovies:
            checkedmovies.append(movies[genreposition-2])
            checkedseats.append(int(movies[genreposition-1]))
          else:
            d=checkedmovies.index(movies[genreposition-2])
            checkedseats[d]= int(checkedseats[d]) + int(movies[genreposition-1])
    

       
    for z in checkedseats:
      if int(z) >= people:
        ind=checkedseats.index(z)
        ind2=checkedmovies[ind]
        if ind2 not in lastlist:
          lastlist.append(ind2)
    if lastlist == []:
        print("There are not enough seats for",moviewanna,"and any other movie with the genre",str(genre)+"!")
    else:
      lastlist.sort()
      print("There are not enough seats for", str(moviewanna)+ "!", "But you can watch one of the following movies from the genre", str(genre) + ":")
      for g in lastlist:
          print('*',g)
else:
  print("There is no such movie in the theater.")
