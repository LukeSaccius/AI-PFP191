import random

class Main:

    # =====GuessNumber function==================
    def GuessNumber(self, number):
        # ====YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART====
        a = 0
        b = int(number)
        state = ''
        while(state != 'c'):
            comp = random.randint(a, b)
            state = input('Is ' + str(comp) + ' too high(h), too low(l), or correct(c): ')
            if(state == 'h'): b = comp-1
            elif(state == 'l'): a = comp+1
            print('Well done! The computer guessed your number ' + str(comp) + ' correctly')

    # =======DO NOT CHANGE THE CODE BELOW========
    def main(self):
        number = input("Enter a range for guessed number: ")
        print("OUTPUT")
        self.GuessNumber(number)
        print("Finish")
main = Main()
main.main()

