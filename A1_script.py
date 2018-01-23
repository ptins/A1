
# coding: utf-8

# In[1]:


# keys/tokens/secrets
consumer_key = 'xxx'
consumer_secret = 'xxx'
access_token = 'xxx'
access_token_secret = 'xxx'


# In[2]:


# tweepy setup 
# !pip3 install tweepy
import tweepy


# In[3]:


# oauth setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[4]:


# save IDs we care about
user_ids = [34373370, 26257166, 12579252]


# # Task 1

# In[5]:


def write_profile_information(user):
    f = open('profile_information.txt','a')
    f.write('Screen Name: {}\n'.format(user.screen_name))
    f.write('User Name: {}\n'.format(user.name))
    f.write('User Location: {}\n'.format(user.location))
    f.write('User Description: {}\n'.format(user.description))
    f.write('Number of Followers: {}\n'.format(user.followers_count))
    f.write('Number of Friends: {}\n'.format(user.friends_count))
    f.write('Number of Statuses: {}\n'.format(user.statuses_count))
    f.write('User URL: {}\n'.format(user.url))
    f.write('-----\n')
    f.close()


# In[6]:


# [write_profile_information(user) for user in api.lookup_users(user_ids)]


# # Task 2

# In[7]:


def write_social_information(user):
    friends = user.friends()
    followers = user.followers()
    f = open('social_information.txt','a')
    f.write('Friend List ({}):\n{}\n'.format(user.screen_name,[friend.screen_name for friend in friends]))
    f.write('Follower List ({}):\n{}\n'.format(user.screen_name,[follower.screen_name for follower in followers]))
    f.write('-----\n')
    f.close()


# In[8]:


# [write_social_information(user) for user in api.lookup_users(user_ids)]


# # Task 3

# In[9]:


class StreamListener(tweepy.StreamListener):
    
    def __init__(self):
        self.num_tweets = 0
        open('tweets.txt', 'w').close()
        super(StreamListener, self).__init__()        
    
    def on_status(self, status):        
        if self.num_tweets < 50:
            print('{} -- {}'.format(self.num_tweets, status.text))
            with open('tweets.txt', 'a') as tf:
                tf.write(status.text)
                tf.write('\n')
                self.num_tweets += 1
            return True
        else:
            return False
            
    def on_error(self, status_code):
        if status_code == 420:
            return False


# In[10]:


stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)


# In[11]:


keywords = ['Indiana', 'weather']
latlong = [-86.33,41.63,-86.20,41.74] # corresponds to South Bend region


# In[12]:


# (1) collect tweets that contain one of the following two keywords: [Indiana, weather] 
# stream.filter(track=keywords, async=True)

# (2) collect tweets that originate from the geographic region around South Bend
# stream.filter(locations=latlong, async=True)

