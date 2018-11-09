from urllib.request import urlopen
from bs4 import BeautifulSoup

#1. Connect to the page
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/3/-4/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

#2. Download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf8")

#3. Find ROI region
soup = BeautifulSoup(page_content, "html.parser")

print(soup.prettify())

ul = soup.find("ul")