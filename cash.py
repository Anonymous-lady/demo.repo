def get_cents():
  while True:
    cents = int(input("Cash Owed: "))
    if cents >= 0:
      return cents
    
def cal_coins(cents):
  quarters = cents // 25
  cents -= quarters * 25
  if quarters > 0:
        print(f"{quarters} quarter(s)")
    
  dimes = cents // 10 
  cents -= dimes * 10
  if dimes > 0:
        print(f"{dimes} dime(s)")

  nickels =  cents // 5
  cents -= nickels * 5
  if nickels > 0:
     print(f"{nickels} nickel(s)")

  pennies = cents
  if pennies > 0:
     print(f"{pennies} penny(ies)")

def main():
    cents = get_cents()
    cal_coins(cents)

if _name_ == "_main_":
  main()

