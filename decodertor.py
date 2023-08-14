def outer (message):
    print("In the outer funtion")

    def inner():
        print("calling the inner funtion")
        print(message)

    return inner

#file =outer( "Hi I am shahriar")
#file()
