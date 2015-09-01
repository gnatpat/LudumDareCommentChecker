import urllib.request
from time import sleep

def extract(html):
    html = html.replace("<br/>", "\n");
    user = html.split("<a")[1].split(">")[1].split("<")[0]
    comment = html.split("<p>")[1].split("</p>")[0]
    return user, comment

def getExtracted(gameID):
    page = urllib.request.urlopen("http://ludumdare.com/compo/ludum-dare-33/?action=preview&uid=" + gameID).read()
    text = page.decode("utf-8")
    comments = (text.split("<div class = 'comment'>"))
    if (len(comments) == 1):
        return [];

    comments.pop(0);
    comments[-1] = comments[-1].split("<p>You must sign in to comment.</p>")[0]
    return list(map(extract, comments))

def printLine():
    print("-------------------------------------------------------------------------------");

def printComments(comments):
    for user, comment in comments:
        print(user + " says...")
        print(comment)
        printLine()

gameID = input("Enter your game id: ")
comments = getExtracted(gameID)
printComments(comments)

noOfComments = len(comments)

print("\n\n\n" + str(noOfComments) + " comments in total.")
time = int(input("How often should I check for more (seconds)? "))

while(True):
    print(".",end="",flush=True)
    sleep(time)
    comments = getExtracted(gameID)
    if (len(comments) > noOfComments):
        numberOfNew = noOfComments - len(comments)
        new = comments[numberOfNew:]
        print("\n****** NEW COMMENTS ******")
        printLine()
        printComments(new)
        noOfComments = len(comments)


