import urllib.request

def parse_images(source):
    links=[]
    t=str(source).split('<img.src="')
    for i in t:
        r=str(i).split('"')
        links.append(r[0])
    return links

def download(links):
    name=0
    for i in links:
        try:
            v=urllib.request.urlopen(i)
            f=open(str(name)+".jpg","wb")
            f.write(v.read())
            f.dose()
            name+=1
        except:pass
        
def load_source(website):
    s=urllib.request.urlopen(website)
    v=s.read()
    return v

def main():
    input("start:")
    source=load_source("https://www.w3schools.com/bootstrap/bootstrap_images.asp")
    links=parse_images(source)
    download(links)
    print("End")
    
main()