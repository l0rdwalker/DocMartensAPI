import requests
import re
import json

def GetCatalog():
    headers = {
        'authority': 'www.drmartens.com.au',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-AU,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'sqshowmaintenance.1514247712=false; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _ga=GA1.3.1074272578.1670244787; _gid=GA1.3.1350519258.1670244787; BVBRANDID=4979ca7f-46dc-4279-87a7-264c6a9563a2; BVBRANDSID=bee0539d-2ad8-4bdb-acf9-7b34202927d7; form_key=Y8thoQebaNOBFLvV; trending-product-cache-storage=%7B%7D; mage-banners-cache-storage=%7B%7D; BVImplmain_site=25064; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gcl_au=1.1.922394096.1670244788; mage-messages=; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_1677073=eyJpZCI6ImM4ZDIyYmJkLWY4YTktNGVjZi04OTcyLTBkNjQ3MmUyNGM4MyIsImNyZWF0ZWQiOjE2NzAyNDQ3ODg0NzEsImluU2FtcGxlIjpmYWxzZX0=; _fbp=fb.2.1670244789011.925767738; SLIBeacon_918619713=r098530A146F341389FB47FDCD65379; _tt_enable_cookie=1; _ttp=HMPSgnzZ2H58bfaGM3yLZ5Ymyh-; __zlcmid=1DHlQYhAfsPoDwB; gs_v_GSN-296339-M=; _gcl_aw=GCL.1670244961.Cj0KCQiAyracBhDoARIsACGFcS7rlwMQo5J7UboNwPv-6dtPuJYfc0zmVN41Y-IhRlV3QIcy3jL-6SUaAlhvEALw_wcB; forterToken=59d2802de795468ebcd47f8931dafd0b_1670244960040__UDF43_13ck; _hjSessionUser_1677073=eyJpZCI6IjJmYjMyYzE3LTYyMTctNTNiOS1iN2U4LTZiYTYwOWY0ZDQzMyIsImNyZWF0ZWQiOjE2NzAyNDQ3ODg0MTMsImV4aXN0aW5nIjp0cnVlfQ==; tfc-l=%7B%22a%22%3A%7B%22v%22%3A%2289516734-a95a-4dfa-97a6-1857730a4bcb%22%2C%22e%22%3A1670331361%7D%2C%22k%22%3A%7B%22v%22%3A%22l6joa5ssn7d7jg8flt9rqgmuv9%22%2C%22e%22%3A1733143989%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1733143988%7D%7D; tfc-s=%7B%22v%22%3A%22tfc-fitrec-product%3D2%22%7D; cto_bundle=qbvJeV9Jd0hPMWtMRWpuZDRRSTh3VXpRUlkyWnBudzhLQUFaVEVNSTZURjVocHgwOVpMMWlZVTRWd1F6SExJWlMwR0VaQWh0cFZFWmc1QUdnNEl2TlA2dDZ2M3ZBV1lXVXBHQVUyYksxaE9DWENaZjgzVCUyRjFsVVRrNVRzUHAySTR4OUNUMVdQeGRVdkxIUEdOV3dyQ0ZidzluUmJoQWpJT2JRWVdaQWo0VGpiZ2I3OCUzRA; _gac_UA-113320546-1=1.1670244964.Cj0KCQiAyracBhDoARIsACGFcS7rlwMQo5J7UboNwPv-6dtPuJYfc0zmVN41Y-IhRlV3QIcy3jL-6SUaAlhvEALw_wcB; gs_u_GSN-296339-M=405adc1aa87c5b64ab43ef344246db26:3115:5379:1670244964686; PHPSESSID=3ge6qcp8fc6v2g2c79ksgo728t; X-Magento-Vary=833192239749766514ad13a72b5d7590b4cd3e2f; datadome=3rGpZpBSDujKyw2fnLtebNcb_bOfcWRWGD2iZ67lTpP9ta9Ci6HtmdtSqRZu-zbPxpssULvZw3DuGBW~gSS~g48zfgwA22tjsIgeCHebwwOVoS5NnkzFXH0Pt1dS0Oiy',
        'dnt': '1',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="107.0.5304.122", "Chromium";v="107.0.5304.122", "Not=A?Brand";v="24.0.0.0"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.drmartens.com.au/media/sitemap_docau.xml', headers=headers)

    jsonStr = str(re.findall('<loc>(.*?)</loc>', str(response.content)))
    jsonStr = jsonStr.split(", ")

    catalog = {}

    for x in range(len(jsonStr)-1):
        Row = jsonStr[x].split("/")
        if (len(Row) == 4):
            Row = Row[len(Row)-1].split("-")
            for y in range(len(Row) - 1):
                if (len(Row[y]) == 8):
                    catalog.update({Row[y]: jsonStr[x].replace("'","")})

    return catalog





    