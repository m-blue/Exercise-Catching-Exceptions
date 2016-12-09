try:
    f = open("noexist.txt")
    w = f.readlines()
    print w
except IOError:
    print("File does not exist")
except:
    print("Unexpected Error")

try:
    num = raw_input("Input an integer: ")
    int_num = int(num)
    print int_num
except ValueError:
    print ("Could not convert to an integer")
except:
    print("Unexpected Error")
