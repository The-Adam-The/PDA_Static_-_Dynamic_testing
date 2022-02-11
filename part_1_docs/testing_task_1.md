### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

#'Import Card' missing

class CardGame: 
# no 'def __init__():, without this it can be hard to error test as unsure if 'card.value' is being treated like an object instatiated by another class, or if a member of this class that has been incorrectly named.

  def check_for_ace(self, card):
    if card.value = 1: # function code only nested by 2 spaces / no self parameter applied to 'card.value' if it's initialised within 'CardGame' 
        return True
    else  # missing ':' after else statement
        return False
   

  dif highest_card(self, card1 card2): #missing ',' between parameters / typo with the word 'dif'/
  if card1.value > card2.value: # if tree not nested/ # card1.value and card2.value has no 'self'
      return card #undefined var 'card'
  else:
      return card2 
  


def cards_total(self, cards):#Not nested within the class
  total # unassigned variable / function code only nested by 2 spaces
  for card in cards: #card = self.cards
      total += card.value #for loop code only nested by 2 spaces /'total' var undefined
  return "You have a total of" + total #Nested return in loop, will return after one loop
  
```
