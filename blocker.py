# -*- coding: utf-8 -*-
import sys
import time
import datetime
import twitter
from settings import *


print("\n\nTrying to block user: %s" % sys.argv[1])


print('\n\n\nEstablish the twitter object')
# see "Authentication" section below for tokens and keys
api = twitter.Api(consumer_key=CONSUMER_KEY,
	consumer_secret=CONSUMER_SECRET,
	access_token_key=OAUTH_TOKEN,
	access_token_secret=OAUTH_SECRET,
	sleep_on_rate_limit=True
    )
	
if(api):
	print('twitter object established')
	print(api)
else:
	print("Something went wrong")
	
#print(api.GetLists())
#print(api.InitializeRateLimit())
print(api.rate_limit)

print("      Getting Your Friends")
users = api.GetFriendIDs(stringify_ids=True)
#print(users)
# for u in users:
	# print(u.name)
	# print(u.screen_name)
	# print()

a=0
print("      Getting %s Friends" % sys.argv[1])
xsers = api.GetFriendIDs(screen_name=sys.argv[1], stringify_ids=True)
for x in xsers:
	print(x)
	a=a+1
	if(a>10):
		break
	# print(x.screen_name)
	# print()
	
ux = set(users)
xx = set(xsers)

zx = xx-ux
a=0
for xz in zx:	
	#print(xz)
	solo=api.CreateBlock(user_id=xz)
	print("%d: Blocking %s" % (a, solo.screen_name))


	
solo = api.CreateBlock(screen_name=sys.argv[1])
print("Finally, blocking %s" % solo.screen_name)




