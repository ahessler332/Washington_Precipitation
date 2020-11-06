
#import requests
# 
# res = requests.get('https://green2.kingcounty.gov/hydrology/DataDownload.aspx?G_ID=321&Parameter=Precipitation')
# print(type(res))
# 
# print(len(res.text))
# 
# print(res.text[:250])
# 
# with open(res.text,'wb') as file:
#     for chunk in res.iter_content(100000):
#         file.write(chunk)
# file.close()    
# import requests 
# from bs4 import BeautifulSoup 
#   
# ''' 
# URL of the archive web-page which provides link to 
# all video lectures. It would have been tiring to 
# download each video manually. 
# In this example, we first crawl the webpage to extract 
# all the links and then download videos. 
# '''
#   
# # specify the URL of the archive here 
# archive_url = "https://green2.kingcounty.gov/hydrology/DataDownload.aspx?G_ID=321&Parameter=Precipitation"
#   
# def get_links(): 
#       
#     # create response object 
#     r = requests.get(archive_url) 
#       
#     # create beautiful-soup object 
#     soup = BeautifulSoup(r.content,'html5lib') 
#       
#     # find all links on web-page 
#     links = soup.findAll('a') 
#   
#     # filter the link sending with .mp4 
#     file_links = [archive_url + link['href'] for link in links if link['href'].endswith('csv')] 
#   
#     return file_links 
#   
#   
# def download_video_series(file_links): 
#   
#     for link in file_links: 
#   
#         '''iterate through all links in video_links 
#         and download them one by one'''
#           
#         # obtain filename by splitting url and getting  
#         # last string 
#         file_name = link.split('/')[-1]    
#   
#         print("Downloading file:%s"%file_name) 
#           
#         # create response object 
#         r = requests.get(link, stream = True) 
#           
#         # download started 
#         with open(file_name, 'wb') as f: 
#             for chunk in r.iter_content(chunk_size = 1024*1024): 
#                 if chunk: 
#                     f.write(chunk) 
#           
#         print("%s downloaded!\n"%file_name) 
#   
#     print("All videos downloaded!")
#     return
#   
#   
# if __name__ == "__main__": 
#   
#     # getting all video links 
#     file_links = get_links() 
#   
#     # download all videos 
#     download_file_series(file_links)

# import urllib3
# http = urllib3.PoolManager()
# file = 'https://green2.kingcounty.gov/hydrology/DataDownload.aspx?G_ID=321&Parameter=Precipitation'
# while True:
#     urllib.request.urlretrieve(file,'C:\Users\alexh\Documents\Geology\Python_Geology' )
#     open('file.csv','wb').write(r.content)

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://green2.kingcounty.gov/hydrology/GaugeMap.aspx")
