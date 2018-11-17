import urllib
def read_text():
    quotes = open(r"C:\Users\suryavijay\Desktop\1.txt")
    contents = quotes.read()
    #print(contents)
    quotes.close()
    checkProf(contents)

def checkProf(texttocheck):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+texttocheck)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert, curse word is there please check it!!")
    elif "false" in output:
        print("This document has no curse words, You can share it now!")
    else:
        print("Could nor scan the document properly")
read_text()
