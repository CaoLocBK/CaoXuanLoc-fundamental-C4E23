from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
#1 Connect
client = MongoClient(uri)

#2 Get default database
db = client.get_database()

#3 Get collection: lấy dữ liệu từ các ngăn của mongo
post = db["posts"] # lazy loading
# movies = db["customers"]
post_list = post.find()

for p in post_list:
    print(p["title"])
    print(p["author"])
    print(p["content"])
new_post = {
"title":"Lệ đá",
"author":"Anh Bằng",
"content":"Hỏi đá xanh rêu bao nhiêu tuổi đời, hỏi gió phiêu du qua bao đỉnh trời, hỏi những đêm thâu đèn vàng héo hắt ái ân bây giờ là nước mắt",
}

# post.insert_one(new_post)