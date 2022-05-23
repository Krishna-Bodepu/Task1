
def write_file(username,password):
    file = open("accountinfo.txt","a")
    file.write(username)
    file.write(" ")
    file.write(password)
    file.write("\n")
    file.close()