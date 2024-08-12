import requests
import re
import json

def GetProductSizeCode(Link):
    headers = {
        'authority': 'www.drmartens.com.au',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-AU,en;q=0.9',
        'cache-control': 'max-age=0',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'sqshowmaintenance.1514247712=false; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _ga=GA1.3.843627352.1663248796; _gid=GA1.3.10161396.1663248796; form_key=wWqUPX21XJJSpmHy; mage-cache-sessid=true; BVBRANDID=d1b5c103-0153-4a60-bcc6-7073a327f8e2; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; trending-product-cache-storage=%7B%7D; mage-banners-cache-storage=%7B%7D; _hjFirstSeen=1; _hjSession_1677073=eyJpZCI6IjIwNDJmNTdjLTU2OTYtNGM2Yi1iMzMyLWQ5MjNkZmYxN2NkYiIsImNyZWF0ZWQiOjE2NjMyNDg3OTg2MzEsImluU2FtcGxlIjpmYWxzZX0=; _gcl_au=1.1.805948142.1663248799; BVImplmain_site=25064; mage-messages=; SLIBeacon_918619713=r508AC22AFEF944BEA6A24F03C6FCED; _fbp=fb.2.1663248799802.916567413; _tt_enable_cookie=1; _ttp=4ce66c22-03f0-40d2-9f91-f7b23b2de721; sqsess=id=6c1fb92a-08b2-4e3b-877a-ecafca6ec2a8; sqvisitor=id=1ec4865b-f510-457f-8c49-c9266ed1e619; __zlcmid=1BylEF3GiU3PohK; gs_v_GSN-296339-M=; forterToken=c6e450561e3443579f3230af829bbd27_1663249556498__UDF43_13ck; _hjSessionUser_1677073=eyJpZCI6ImU1NzY3M2E1LTg2ZWUtNWFkMy04MTg0LTMwMTcxOWQ3ZTU2MiIsImNyZWF0ZWQiOjE2NjMyNDg3OTgzNzIsImV4aXN0aW5nIjp0cnVlfQ==; tfc-l=%7B%22a%22%3A%7B%22v%22%3A%222f7192fa-22ca-4e95-b15c-03f4067d6c69%22%2C%22e%22%3A1663335959%7D%2C%22k%22%3A%7B%22v%22%3A%22qsrs3hg3jfp4857ac34icm7ed0%22%2C%22e%22%3A1726147999%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1726147998%7D%7D; tfc-s=%7B%22v%22%3A%22tfc-fitrec-product%3D2%22%7D; cto_bundle=2chQk19QM0pzbTgyNFhseDhGcVFGZGJMYUx2RFBHNzBDbjBKSFRuSDNJUEg2elNYTXhmZmNVeWRmYiUyQjZSd2w3ZmYzTHRDeFdXWW51YnBYT3JKdEpWbTVqb2tXOTNGeTRxekdVRm45VDhEVjNORTRWZGIwMXRCdWZSTXZkdkxuV09HQ0th; gs_u_GSN-296339-M=ddd4e74173806f49f411d7cba79894f3:3115:5379:1663249563231; datadome=66376ejk.f7_nYpNsBIk2l7_~LCeYbjRLsJYN8tINwR~O7Jk_O.Jqtsj83.Vo_0Atu8YXJjC.NqP8YNerhCA1zFDogg4rM3JYtdNN0losdKDnP7wYoid5wnZ8vjS.P5; 19509.vst=%7B%22s%22%3A%22%22%2C%22t%22%3A%22new%22%2C%22lu%22%3A1663249581424%2C%22lv%22%3A1663248820438%2C%22lp%22%3A0%7D; RT=r=https%3A%2F%2Fwww.drmartens.com.au%2Fvintage-1460-12308601-oxq.html&ul=1663250675155; gs_p_GSN-296339-M=1',
        'dnt': '1',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.102", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    }

    response = requests.get(Link, headers=headers)
    try:
        jsonStr = json.loads((re.search('label":"UK","options":(.*?),"position"', str(response.content)).group(1)))
        return jsonStr
    except:
        return None

