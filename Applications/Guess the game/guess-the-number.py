import random
system = random.randint(0, 10)
score = 100
while True:
  try: 
   player = int(input("guess a no between 1 to 10 \n"))
   if player == system:
     print("Damn you are genius")
     break
    
   elif player > 10:
     print("Bro I said 1 to 10")
     score -= 10
     
   elif player > system:
     print(f"Nope the number is lesser than {player}")
     score -= 10
    
  
   elif player < system:
     print(f"Nope the number is greater than {player}")
     score -= 10
  except:
   print("Atleast type a correct spelling")

print(f" So your score is {score}")
