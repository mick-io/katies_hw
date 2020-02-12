# Week 5
# Code Along 3

while True:
    file_name = input("Enter a file name: ")
    try:
        fhandle = open(file_name, "w+")
        contents = fhandle.read()

        while True:
            text = input("What do you want to write out? ")
            if text.lower() == "done":
                break

            fhandle.write(text + "\n")

    except:
        print("Invalid file name")
    else:
        break
