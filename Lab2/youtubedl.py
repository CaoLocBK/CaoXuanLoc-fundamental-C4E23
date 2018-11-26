from youtube_dl import YoutubeDL

# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=tCV4dSMeQzE'])

# Download multiple youtube videos

dl = YoutubeDL()
dl.download(['https://www.youtube.com/watch?v=d3q11cVhJBo'])

#Download audio
option = {
    'default_search': 'ytsearch',
    'max_downloads': 1
}