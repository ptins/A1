# CSE40437/CSE60437 - A1

This is the first assignment for my Social Sensing/Cyber-Physical Systems Class.

## Getting Started

Download everything from either (1) my dropbox (folder A1) or (2) clone this repository on GitHub.

### Prerequisites

I developed this in Python 3.6.4, and used the tweepy library to access Twitter's API. 
Tweepy can be installed with the following command, which is also listed in my Python script.

```
pip3 install tweepy
```

## Running the Script

My preferred way to run this program is in a Jupyter notebook, which can be installed via the following command.

```
python3 -m pip install --upgrade pip
python3 -m pip install jupyter
```

After installing Jupyter, you can open my notebook (A1.ipynb) with the following command.

```
jupyter notebook A1.ipynb
```

You can then run cells individually.


If you elect to run this program from the command line, use the following command.

```
python3 -A1_script.py
```

Regardless of the method used above, make sure to comment/uncomment out certain lines to avoid rate limits on Twitter's API.

### Task 1

Task - Given a list of user IDs, please write a data crawler to collect the users' profile information.

Make sure the following line is not commented out.

```
[write_profile_information(user) for user in api.lookup_users(user_ids)]
```

I saved the resulting file containing the profile information in profile_information.txt

### Task 2

Task - Given a list of user IDs, please write a data crawler to collect the user social network information (i.e., the lists of screen names of the user's friends and followers)

Make sure the following line is not commented out.

```
[write_social_information(user) for user in api.lookup_users(user_ids)]
```

I saved the resulting file containing the profile information in social_information.txt

### Task 3.1

Task - Please write a data crawler to collect tweets that contain one of the following two keywords: [Indiana, weather]

NOTE: For Task 3.1, the stream for this subsection requires that the other stream be commented out.
See below. 

```
# (1) collect tweets that contain one of the following two keywords: [Indiana, weather] 
stream.filter(track=keywords, async=True)

# (2) collect tweets that originate from the geographic region around South Bend
# NOTE THAT THE BELOW LINE IS COMMENTED OUT
# stream.filter(locations=latlong, async=True)
```

I saved the resulting file containing the tweets in tweets_keywords.txt (note the name difference from 'tweets.txt')

### Task 3.2

Task - Please write a data crawler to collect tweets that originate from the geographic region around South Bend.

NOTE: As above, the stream for this subsection requires that the other stream be commented out.
See below.

```
# (1) collect tweets that contain one of the following two keywords: [Indiana, weather] 
# NOTE THAT THE BELOW LINE IS COMMENTED OUT
# stream.filter(track=keywords, async=True)

# (2) collect tweets that originate from the geographic region around South Bend
stream.filter(locations=latlong, async=True)
```

I saved the resulting file containing the tweets in tweets_latlong.txt (note the name difference from 'tweets.txt')

