from art import logo, vs
import sys, os

#print(logo)
from game_data import data
condition=True
#print(data[0])
import random
i=random.randint(0,len(data)-1)
j=random.randint(0,len(data)-1)
if i == j:
  j=random.randint(0,len(data)-1)
score=0
  
def Calsocre():
  ''' this fucntion will add the score '''
  return score + 1

  
while condition:
  print(logo)
  if score > 0:
    print(f"You're right, current score: {score}")
  print(f"compare A: {data[i]['name']}, a {data[i]['description']}, from {data[i]['country']}")
  print(vs)
  print(f"compare B: {data[j]['name']}, a {data[j]['description']}, from {data[j]['country']}")
  check=input("Who has more followers? Type 'A' or 'B': ")
  os.system('cls')
  count_A=data[i]['follower_count']
  count_B=data[j]['follower_count']
  
  if check =='A' and count_A > count_B:
    i=j
    j=random.randint(0,len(data)-1)
    score=Calsocre()
  elif check =='B' and count_B > count_A:
    i=j
    j=random.randint(0,len(data)-1)
    score=Calsocre()
  else:
    print(logo)
    print(f"Sorry, that's wrong. Final score : {score}")
    condition = False
    