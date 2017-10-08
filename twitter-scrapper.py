from twitterscraper import query_tweets

count=0
q=query_tweets("travelling to delhi",1000)
for tweet in q[:1000]:
	#print (type(tweet))
	#print(tweet)
	x=((str(tweet.timestamp.date())).split('-'))
	if(x[0]=="2017" and int(x[1])>8):
		count=count+1
		print(tweet.text.encode('utf-8'))
		print(tweet.timestamp.date())
	else:
	    print(tweet.timestamp.date())
	    print(count)
	    break
	#print(type(x))
	#print(x[0])
