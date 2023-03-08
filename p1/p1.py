import re
import pandas as pd

df = pd.read_csv('tweets.csv', sep='\t', lineterminator='\r', header=(0))
arrayOfTweets = df["Tweet"].map(str)

userRegularExpression = r'@{1}([a-zA-Z]|[0-9]|_)+'
hashtagRegularExpression = r'#{1}([a-zA-Z]|[0-9])+'
hourRegularExpression = r':[0-5][0-9](am|pm|AM|PM)?'
dateRegularExpression = r'\d\d?([/]|[-])\d\d?(([/]|[-])\d\d?(\d\d)?)?'

numberOfUsers = 0
numberOfHashtags = 0
numberOfHours = 0
numberOfDates = 0

for tweet in arrayOfTweets:
	numberOfUsers += len(re.findall(userRegularExpression, tweet))
	numberOfHashtags += len(re.findall(hashtagRegularExpression, tweet))
	numberOfHours += len(re.findall(hourRegularExpression, tweet))
	numberOfDates += len(re.findall(dateRegularExpression, tweet))

print("Frequencies")
print("\tUsers :", numberOfUsers)
print("\tHashtags :", numberOfHashtags)
print("\tHours :", numberOfHours)
print("\tDates :", numberOfHours)
