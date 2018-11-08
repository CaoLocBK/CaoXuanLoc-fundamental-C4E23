from youtube_dl import YoutubeDL

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=tCV4dSMeQzE'])

# Download multiple youtube videos

dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=dns2WLu8Su8','https://www.youtube.com/watch?v=ogNgzv8Hl7A'])

#Download audio
option = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}