def question():
    question1 = "2+4="
    print(question1)
    answer1 = "6"
    i = input("")
    c = "your answer is correct"
    w = "your answer is wrong"
    if i == answer1:
        print(c)
    else:
        print(w)
    question2 = "8x6="
    print(question2)
    o = input("")
    answer2 = "48"

    if o == answer2:
        print(c)
    else:
        print(w)

    question3 = "56+54="
    answer3 = "110"
    print(question3)
    p = input("")
    if p == answer3:
        print(c)
    else:
        print(w)


#set your user name and password a= username and ap = password
a = "ganesh"
g = "rishi"
ap = "125678"
gp = "125678"
print()
print("username")
print("if your account is not create type ""c")
n = input("")
if n == a:
    print("password")
    p=input("")
    if p == ap:
        print(question())

        print(n + "'s test is completed")
        quit()
if n == g:
    print("password")
    p = input("")
    if p == gp:
        print(question())

        print(n + "'s test is completed")
        quit()
if n == "c":
    print("creating account")
    print ("username")
    o = input("")
    print("password")
    h = input("")
    new = o
    newp = h
    print("your account is created succsefully")


    print("username")
    z = input("")
    if z == o:
        print("password")
    else:
        print("username not found")
        quit()
    y = input("")

    if y == h:
        print(question())

        print(z + "'s test is completed")
    else:
        print("password in not found")
    quit()

else:
    print("password or username is not fouded")

print()