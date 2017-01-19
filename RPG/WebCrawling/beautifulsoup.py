import urllib.request
from bs4 import BeautifulSoup

if __name__ == "__main__":
    print("Hello World")
    req = urllib.request.Request("http://finance.daum.net/item/newsview.daum?code=096770&docid=MD20161121172002429&hpage=1&no=1");
    data = urllib.request.urlopen(req).read()

    bs = BeautifulSoup(data, 'html.parser')

    l = bs.find_all('a')

    idx = 0
    for s in l:
        try:
            print("%d : %s" % (idx, str(s)))
        except UnicodeEncodeError:
            print("Errror : %d" % (idx))
        finally:
            idx += 1


