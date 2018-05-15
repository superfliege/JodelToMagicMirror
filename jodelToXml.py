#Developed by superfliege (Fabrice)

#Need to install and fill informations. Please read: https://github.com/nborrmann/jodel_api



from __future__ import print_function
import jodel_api
import time



lat, lng, city = 00,00,"Berlin" #TODO add something (privacy)

j = None
accountvalid = False

#Read Tokent
try:
	f = open('token','r')
	dict_accountdata = eval(f.read())
	f.close()
	print(dict_accountdata)
except:
	print("token file not found..skipping authentification")


#Login
try:
	j = jodel_api.JodelAccount(lat=lat, lng=lng, city=city, access_token='XXX', expiration_date='1518130677', refresh_token='XXX', distinct_id='5a739b75633fde0016eb80d1', device_uid='bd1986a13456033f57d0', is_legacy=True) #TODO add something (privacy)
	accountvalid = True
except:
	print("Jodel account not valid anymore.")
	accountvalid = False
	
#Recreate account
if accountvalid == False:
	print("Create jodel account.")
	j = jodel_api.JodelAccount(lat=lat, lng=lng, city=city)
	dict_accountdata = j.refresh_access_token()
	#Create Token
	f = open('token','w+')	
	f.write(str(dict_accountdata[1]))	
	f.close()				   
max_jodel = 3
while True:
	print("Debug: Fetching data from jodel.")
	
	dict_posts_recent = j.get_posts_recent(skip=0, limit=max_jodel, after=None, mine=False, hashtag=None, channel=None)
	posts_recent = []
	for i in xrange(0, max_jodel):
		posts_recent.append(dict_posts_recent[1]["posts"][i]["message"].encode('utf-8'))

	dict_posts_popular = j.get_posts_popular(skip=0, limit=max_jodel, after=None, mine=False, hashtag=None, channel=None)
	posts_popular = []
	for i in xrange(0, max_jodel):
		posts_popular.append(dict_posts_popular[1]["posts"][i]["message"].encode('utf-8'))

	dict_posts_discussed = j.get_posts_discussed(skip=0, limit=max_jodel, after=None, mine=False, hashtag=None, channel=None)
	posts_discussed = []
	for i in xrange(0, max_jodel):
		posts_discussed.append(dict_posts_discussed[1]["posts"][i]["message"].encode('utf-8'))

	#HTML OUTPUT
	outFile = open('jodelexport.html', 'w')
	outFile.write("<head>")
	outFile.write("<meta charset='UTF-8'>")
	outFile.write("<style> \
        .jodeltable{ \
                font-size: 20px; \
                align='right'; \
				height: 600px; \
				width: 900px; \
                cellpadding='10'; \
        } \
        .jodeltable td, tr \
        { \
                line-height: 1.0; \
                border: 1px solid #ddd; \
        } \
        .jodeltable td{ \
				width: 300px; \
                text-align:  left; \
        } \
        </style>")
	outFile.write("</head>")
	outFile.write("<table class='jodeltable'>")
	outFile.write("<td> NEUSTE JODEL</td>" + "<td> MEIST KOMMENTIERT</td>" + "<td> TOP JODEL </td>")
	for i in xrange(0, max_jodel):
		outFile.write("<tr>")
		outFile.write("<td>" + posts_recent[i] + "</td>" + "<td>" + posts_discussed[i] + "</td>" + "<td>" +  posts_popular[i]+ "</td>")
		outFile.write("</tr>")
	outFile.write("</table>")
	outFile.close()

	time.sleep(180)
