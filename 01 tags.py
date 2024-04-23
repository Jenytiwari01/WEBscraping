import requests
from bs4 import BeautifulSoup
with open("sample.html","r") as f:
    html_doc=f.read() #html doc ma sample file ko contain as a string aaucha


soup= BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())#just pretty the sample object

#print(soup.title.string, type(soup.title.string))
# print(soup.div) gives the div elements
#print(soup.find_all("div"))
#for link in soup.find_all("a"):
   #print(link.get("href"))#gives all links of a tag
# for link in soup.find_all("a"):
#     print(link.get("href"))
# s=soup.find(id="link3")
# print(s.get("href"))
#print(s.href)#gives null so
#print()

# print(soup.select("div.italic"))

# print (soup.select("span#italic"))
# print soup.find(calss_="box").parent
# print(soup.span.get("class"))
# print(soup.find(class_="italic"))#class is a reserved word

# for child in soup.find(class_="container").children:
    # print(child)
# i = 0
# for parent in soup.find(class_="box").parents:
#     i += 1
#     print(parent)
#     if i == 2:
#         break

# 

# ulTag=soup.new_tag("ul")

# liTag=soup.new_tag("li")
# liTag.string="home"
# ulTag.append(liTag)


# liTag=soup.new_tag("li")
# liTag.string="about"
# ulTag.append(liTag)


# soup.html.body.insert(0 , ulTag)
# with open("modified.html","w")as f:
#     f.write(str(soup))

# cont=soup.find(class_="container")
# print(cont.has_attr("contenteditable"))

# def has_class_but_not_id(tag):
#     return tag.has_attr("class") and not tag.has_attr("id")

# results = soup.find_all(has_class_but_not_id)
# print(results)

def has_id_but_not_class(tag):
    return tag.has_attr("id") and not tag.has_attr("class")

results = soup.find_all(has_id_but_not_class)
print(results)