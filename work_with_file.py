
"""
data = open("test.txt")
#print(data.read())
data.readlines()
#data.close()

"""

# data = open("test.txt")
# a = (data.readlines())
# res = list(map(lambda x: x[:-1], a))

# print(res)
#homework 1
"""
with open ("test.txt","r") as f:
    print(f.read())
"""

#hoemwork 2

"""with open ("test.txt","r") as f:
    print(f.readline())"""

#homework 3

"""with open ("test.txt","a+") as f:
    f.write("Bu birinchi qator \n")
    f.write("Bu ikkinchi qator ")
    f.seek(0)
    print(f.read())"""

#homework 4
"""
with open ("test.txt","r") as f:

    print(f.readlines())


"""

#homework 5

# with open ("test.txt","r") as f:

#     print(len(f.readlines()))

# homework 6

# import json
# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# with open ("test.txt",'w+') as f:
#     for i in color:
#         json.write(i)


# homemwork 7 
# all = []
# with open("test.txt", "r") as f:
#     for i in f:
#         for j in i:
#             all.append(j)
# print(all)

# homework 8

















# homework 9
# res = {}
# with open ("test.txt","r") as f:
#     for i in f:
#         a = i.split()
#         for j in a:
#             if j in res:
#                 res[j] += 1
#             else:
#                 res[j] = 1

# print(res)     






# import requests
# from bs4 import BeautifulSoup

# response = requests.get("https://soffstudy.uz/posts")
# print(response.status_code)
# pprint(response.content)

# soup = BeautifulSoup(response.content,"html.parser")
# posts = soup.find_all("div",class_= "card-info")
# post_titles = soup.find_all("div", "btn btn-tag bg-gray-800 hover-up")
# catigory = soup.find_all("div", "btn btn-tag bg-gray-800 hover-up")

# rasm olish uchin

"""img = soup.find_all("img", "h-100")
for i in img:
    print(i['src'])"""



# print (post_titles)

# for i in post_titles:
#     print(i.text)

# for i in posts:
#     post_titles = i.find('h4').text
#     catigory = i.find("div", class_ = "btn btn-tag bg-gray-800 hover-up").text
#     picture = i.find('div', {id: "h-100"})
#     print(picture)
#     # print(catigory)
#     # print(post_titles)




# import json
# import requests
# from bs4 import BeautifulSoup


# response = requests.get("https://soffstudy.uz/posts")
# with open('fayl.json','w+') as f:
#     json.loads()







# import requests
# from pprint import pprint
# from bs4 import BeautifulSoup

# response = requests.get("https://soffstudy.uz/posts")
# # pprint(response.content)
# # print(response.status_code)

# soup = BeautifulSoup(response.content,"html.parser")
# data = soup.find_all('div', class_ = 'card-info')
# img = soup.find_all('img', 'h-100')
# img1 = soup.find_all('img', 'logo-night')
# for i in img1:
#     print(i['src'])
# for i in img:
#     print(i['src'])


# for i in data:
#     tit = i.find('h4').text
#     did = i.find('div', 'btn btn-tag bg-gray-800 hover-up').text
#     print (did)
#     print(tit)






















