n=input("Name?:")
class person:
    def greting(n):
        print("Hello i am "+n+", how are you?")
    def bye():
        print("Bye to you too")
    def eb():
        print("\"wait wha-\"")
        print("*box eplosion*")
    while True:
        print("----MENU----\n1.Say \"Hello\"\n2.Say \"Goodbye\"\n3.\"exploding box\"")
        a=input()
        if a=="1":greting(n)
        if a=="2":bye();break
        if a=="3":eb();break