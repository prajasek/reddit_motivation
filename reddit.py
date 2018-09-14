import praw
import webbrowser

#What subreddit you want to view posts from 
subreddit_name = "getmotivated"

reddit = praw.Reddit(client_id = "xxxx-xxxx",
                    client_secret = "xxxxx",
                    password = "xxxx",
                    username = "xxxxx", 
                    user_agent = "get_motivated")

#https://www.reddit.com/r/getmotivated
subreddit = reddit.subreddit(subreddit_name)

post_dict = {"title" : [], "id" : [] , "url" : []}

#hot/new posts
for post in subreddit.hot(limit=5):
    post_dict["title"].append(post.title)
    post_dict["id"].append(post.id)
    post_dict["url"].append(post.url)
    
#add one random post 
for i in range(1): 
    post_dict["title"].append(subreddit.random().title)
    post_dict["id"].append(subreddit.random().id)
    post_dict["url"].append(subreddit.random().url)


# Hot/new 3 post +  1 random post
hot_ten_links = [(post_title,"https://www.reddit.com/r/GetMotivated/comments/"+ post_id) for post_title, post_id in zip(post_dict["title"][2:],post_dict["id"][2:])]

# Open these links in default browser
for links in hot_ten_links:
    webbrowser.open(links[1], new=1)




