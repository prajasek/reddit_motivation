import praw
import webbrowser


reddit = praw.Reddit(client_id = "dv4AghN-m6GxfA",
                    client_secret = "lYi6i98Fc9Iqh8W9WdJfUdfadAY",
                    password = "mobile6120!",
                    username = "wannastro", 
                    user_agent = "get_motivated")

#https://www.reddit.com/r/getmotivated
subreddit = reddit.subreddit("getmotivated")

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




