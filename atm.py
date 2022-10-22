class Atm():
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin

    def balance(self):
        print("Your balance is 50000")

    def cashwithdrawl(self,cashwithdrawl):
        print("You have withdrawn",cashwithdrawl)




cardnumber=input("enter your card number")
pin=input("enter your pin")


new_user = Atm(cardnumber, pin)

new_user.balance()

cash=input("enter the amount of cash you want to withdraw")

new_user.cashwithdrawl(cash)