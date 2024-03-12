class Main:

    # ======================================f1
    def f1(self, inputString):
        # ====YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART======
        a = inputString.split(', ')
        for x in a:
            print(x)

    # ======================================f2
    def f2(self, inputString):
        # ====YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART======
        a = inputString.split(', ')
        lst = [x.split() for x in a]
        x = int(lst[0][1]) - int(lst[1][1])
        y = int(lst[2][1]) - int(lst[3][1])
        res = (x**2 + y**2)**(1/2)
        print(round(res))

    # ======================================DO NOT CHANGE THE CODE BELOW=====
    def main(self):
        print("1. Test f1 (2 mark)")
        print("2. Test f2 (1 mark)")
        print("Your selection (1 -> 2): ")
        choice = int(input())
        inputString = input("OUTPUT")
        if choice == 1:
            self.f1(inputString)
        elif choice == 2:
            self.f2(inputString)
        else:
            print("Wrong select")
        print("FINISH")

main = Main()
main.main()
