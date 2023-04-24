new_auct = {'rr': 33, 'tt':44}
win = ""
def new_bidder (name, bid):
  new_auct.update({name: bid})

def winner(new_auct):
#  max_name = ""
  max_bid = 0
  for i in new_auct:
    score = new_auct[i]
    if max_bid < score:
      max_bid = score
    print (max_bid + "dsds")
winner(new_auct)

should_continue = True
while should_continue:
  name = input("What your name? \n")
  bid = int(input("What your bid? \n"))
  new_bidder (name, bid)
  cont = input("Are other? y or n ")
  if cont == "n":
    should_continue = False

print(new_auct)
print(f"The winner is {win}")

