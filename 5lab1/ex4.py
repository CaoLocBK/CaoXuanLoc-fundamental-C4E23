from pymongo import MongoClient
from matplotlib import pyplot

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
#1 Connect
client = MongoClient(uri)

#2 Get default database
db = client.get_database()

#3 Get collection: lấy dữ liệu từ các ngăn của mongo
post = db["customers"] # lazy loading
# movies = db["customers"]
post_list = post.find()

t_ads = 0
t_wom = 0
t_events = 0
for p in post_list:
    if print(p["ref"]) == "ads":
        t_ads += 1
    elif print(p["ref"]) == "wom":
        t_wom +=1
    elif print(p["ref"]) == "events":
        t_wom +=1
ref_counts = [t_ads, t_wom, t_events]
ref_name = ["Advertisement","Word of mount","Events"]

pyplot.pie(ref_counts, label= ref_name, autopct="%.1f%%",shadow=True,explode=[0,0.05,0])
pyplot.axis("equal")
pyplot.title('References list')

# post.insert_one(new_post)