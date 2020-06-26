from instapy import InstaPy

print("Hello There! ")
name  = input("I'd like to ask you your name : ")



print("Hi " + name +" Here are some instructions and rule to follow. Before you use this instagram bot to increase your reach.")
print(" ")
print("1. You need to submit your Username and Password, ensuring complete privacy of your details  ")
print("2. You need to set # tags which you might wanna follow and like posts of ")
print("3. There are some standard NSFW(Not safe for work) tags already added by our AI and if you want to add some tags of your own you can add them too")
print("note: though AI is not very polished yet to categorize posts, so we advise to add a lot number of hashtags to follow and avoid.")
print("4. By using this instagram bot, you are agreeing this program to comment, like , follow on your behalf.")
print(" ")
print("This will surely result in increase in your reach of your page/personal Id")
print("But it will not ensure the follow back, it depends on the quality of posts and content on your page.")
print("So We wish that your purpose of using this bot gets fulfilled.")
print(' ')
print("This bot has some limits which ensures it, that it doesn't get recognised as a bot by instagram algorithm")
print("         Will only comment on 21 posts per hour. ")
print("         The bot will keep commenting until it reaches its hourly and daily limits. It will resume commenting after the quota period has passed. ")
print("         This app is in developing phase, so entering tags and comments is a bit hassel right now but we will like to make it easier in upcoming versions. ")
print(" ")
print("-------------------------------------------------------")
print("Firefox browser is needed to be installed in the system.")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Enter your account details : ")
usrname = input("Username: ")
pswrd = input("Password:")

tags = []
print("  ")
print("  ")
print("Enter the number of hashtags you want to add for liking the posts")
nlikes = int(input("Number of tags you want to add for likes (keep it around 20-25)"))
print("please Enter tags without '#' . /n Eg. for #beautiful --> beautiful ")
print("Though adding tags is a tiring process, but its only a one time task.")
for i in range(nlikes):
    tag = input("enter tag : ")  
    tags.append(tag)
    

ntags = ["naked" , "nsfw" , "NSFW" , "tik-tok"]
print("  ")
print("  ")
print("Enter the number of hashtags you want to add for rejecting the posts")
nrejects = int(input("Number of tags you want to add for rejection (keep it around 5-6)"))
print("please Enter tags without '#' . /n Eg. for #tiktok --> tiktok ")
print("Though adding tags is a tiring process, but its only a one time task.")
for i in range(nrejects):
    ntag = input("enter tag : ")
    ntags.append(tag)

print("  ")
print("  ")
commentflag = 'n'
print("Do you like to use comment feature??")
commentflag = input("Y for yes | N for no : ")
print("  ")
print("  ")
if commentflag == 'y' or commentflag == 'Y' :
    comments = []
    print("Add similar type of comments ,which can be posted irrespective of posts.")
    print("for eg.  nice, haha , way to go")
    c = int(input("Enter the number of comments you want to add. "))
    for i in range(c):
        comment = input("Enter Comment : ")
        comments.append(comment)

print("  ")
print("  ")

print("Now sit back and relax, while bot does its work")
print("You can proceed with your other work, bot knows its limits")
print("Since it is in its developing face, you may/may not face an error, OR it may crash, don't worry we don't save any of your details")
print("Just run the program again, enter your details again and carry on.")
print("  ")
print("  ")
print("You can easily trace the bots functionality by looking at the logs given below ")
print("  ")
print("  ")
session = InstaPy(username=usrname, password=pswrd, headless_browser=True).login()

session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

session.like_by_tags(tags, amount=1)
session.set_dont_like(ntags)
session.set_do_follow(True, percentage=50)



if commentflag == 'y' or commentflag == 'Y' :

    session.set_do_comment(True, percentage=50)
    session.set_comments(comments)



session.end()
