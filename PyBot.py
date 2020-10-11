from selenium.webdriver.common.keys import Keys
from BotProtocols import Surface
from selenium import webdriver
from time import sleep
import random
import sys

if __name__ == "__main__":
    
    username = "username"
    password = "password"

    Bot = Surface(username, password)
    Bot.openPage()
    Bot.login()
    
    

    #list of hashtags to target
    hashtag_list = ["f4f", "like4follow", "like4like", "likeforlike", "follow4follow"]
    #list of comments to post
    comment_list = [
                        ["this", "the", "your"],
                        ["photo", "picture", "pic", "shot", "snapshot"],
                        ["is", "looks", "feels", "is really"],
                        [
                            "great","super","good", "very good", "good", "wow",
                            "WOW","cool","GREAT","magnificent","magical",
                            "very cool","stylish","beautiful","so beautiful","so stylish",
                            "so professional","lovely","so lovely","very lovely","glorious",
                            "so glorious","very glorious","adorable","excellent","amazing",
                        ],
                        [".", "..", "...", "!", "!!", "!!!"]
                    ]

    while True:
        try:
            tag = random.choice(hashtag_list) #random hashtag from the list
            Bot.like_photos(tag)
            Bot.type_comments(comment_list)
            sleep(25)
        except Exception:
            print("exception")
            Bot.closeBrowser()
            sleep(60)
            Bot = Surface(username, password)
            Bot.login()

    print("finished")
    Bot.closeBrowser()
