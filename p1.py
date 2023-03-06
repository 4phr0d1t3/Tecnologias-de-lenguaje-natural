import re
import pandas as pd

df = pd.read_csv('tweets.csv', sep='\t', lineterminator='\r', header=(0))
arrayOfTweets = df["Tweet"].map(str)

userRegularExpression = r'@{1}([a-zA-Z]|[0-9]|_)+'
hashtagRegularExpression = r'#{1}([a-zA-Z]|[0-9])+'
# hourRegularExpression = r'((0|1)*[0-9]|(2{1}[0-3])):[0-5][0-9](am|pm|AM|PM)?'
hourRegularExpression = r':[0-5][0-9](am|pm|AM|PM)?'

numberOfUsers = 0
numberOfHashtags = 0
numberOfHours = 0

for tweet in arrayOfTweets:
	numberOfUsers += len(re.findall(userRegularExpression, tweet))
	numberOfHashtags += len(re.findall(hashtagRegularExpression, tweet))
	numberOfHours += len(re.findall(hourRegularExpression, tweet))

# test = re.findall(hashtagRegularExpression, "hola #comEstas hijo #0189us0w9df #la neta no se qu ehace")
# print(test)

print("Users :", numberOfUsers)
print("Hashtags :", numberOfHashtags)
print("Hours :", numberOfHours)
