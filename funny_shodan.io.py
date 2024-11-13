from bs4 import BeautifulSoup as bb
import requests, argparse

parser = argparse.ArgumentParser(description="Funny shodan.io IPs")
parser.add_argument("-q", nargs='+', type=str, help="Provide shodan search query", required=True)
args = parser.parse_args()
search=' '.join(args.q)
try:
    url = f"https://www.shodan.io/search/facet?query={search}&facet=ip"
    head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
    res = requests.get(url, headers=head, timeout=10, allow_redirects=True)
    if res.status_code == 200:
        data = bb(res.content, "html.parser")
        dd = data.find('div',class_='card card-padding container u-full-width')
        ips = dd.find_all('strong')
        for i in ips:
            print(i.string)
    else:
        print(f"status: {res.status_code}")
except:
    pass
