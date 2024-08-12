import requests
import re

def CheckAvalibility(SampleProductID):
    headers = {
        'authority': 'www.drmartens.com.au',
        'accept': '*/*',
        'accept-language': 'en-AU,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
        'cookie': 'PHPSESSID=j36n1vlq9afmfd3cet0v9dimc2; X-Magento-Vary=833192239749766514ad13a72b5d7590b4cd3e2f; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; _ga=GA1.3.995931561.1662050564; _gid=GA1.3.1628952254.1662050564; _gac_UA-113320546-1=1.1662050564.CjwKCAjwsMGYBhAEEiwAGUXJaWJwg0WMymjkRPvLT7wP73wuNa6q01XAk-LAGxgH76smj4VkqPQfCxoCWTYQAvD_BwE; BVBRANDID=26c3b869-61b2-43e5-a66d-717128465131; form_key=Vv1hj7QJKqikaBvy; mage-cache-sessid=true; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; _gcl_aw=GCL.1662050565.CjwKCAjwsMGYBhAEEiwAGUXJaWJwg0WMymjkRPvLT7wP73wuNa6q01XAk-LAGxgH76smj4VkqPQfCxoCWTYQAvD_BwE; _gcl_au=1.1.1639166689.1662050565; _hjFirstSeen=1; _hjSession_1677073=eyJpZCI6ImM2ZTIyOTVkLWZlNzYtNDY3ZC1hMzBjLTBmOWQ1MDI2MTMyOCIsImNyZWF0ZWQiOjE2NjIwNTA1NjQ5NzgsImluU2FtcGxlIjpmYWxzZX0=; _fbp=fb.2.1662050565602.1275759596; _tt_enable_cookie=1; _ttp=f89e3d29-bdae-4e79-9c27-36cbf1c6ff77; __zlcmid=1BklC8G7WiATwyw; mage-messages=; mage-banners-cache-storage=%7B%7D; SLIBeacon=l1647a383898141a09718183008b20d; SLISYNC=1; _hjSessionUser_1677073=eyJpZCI6IjgxYzBmMTk2LTVkNDYtNTRjNi05OTliLThlZTA4MGZmYjQ2OCIsImNyZWF0ZWQiOjE2NjIwNTA1NjQ3NzQsImV4aXN0aW5nIjp0cnVlfQ==; sqsess=id=5d0589d7-6e51-40f4-8266-462b286709e0; sqvisitor=id=946751af-e76e-4ad5-8684-af9617f4e63b; gs_v_GSN-296339-M=; form_key=Vv1hj7QJKqikaBvy; BVImplmain_site=25064; trending-product-cache-storage=%7B%7D; sqshowmaintenance.1514247712=false; BVBRANDSID=ae0ca289-8de5-45a0-9a2e-b4bbd40cf236; forterToken=4246dd292cac4fb0ade4974cafaf4dcb_1662053595407__UDF43_13ck; cto_bundle=cJJ6wl9OTVA4R1dJcWpqd0ElMkJMQ2swdlprTmhjNWxFSFRmanI5TUQ0emc0UXM5aldkSU5pU01tJTJGJTJGdkRneFRLRWFwZUFOM0pJNE8yT0NuMHJyUmFYUTdTUHJDNUlhNXA5aENzdnlqaiUyRmVjNFNVSFFIOXRIY3pKVUtJVmJ4MEY4U2pBRmd3NXN2RUxBdiUyRkN0SnRVc241eGI2T2FFMmlVSmx6ZHF6Q2diSlloVHljM2l3JTNE; tfc-l=%7B%22a%22%3A%7B%22v%22%3A%22ca5fcfc4-3ff7-4122-a697-b04edcd4f3f1%22%2C%22e%22%3A1662139998%7D%2C%22k%22%3A%7B%22v%22%3A%22u472aq3dm5n6gcfpscvfq9vjb1%22%2C%22e%22%3A1724949832%7D%2C%22c%22%3A%7B%22v%22%3A%22adult%22%2C%22e%22%3A1724949831%7D%7D; tfc-s=%7B%22v%22%3A%22tfc-fitrec-product%3D5%22%7D; gs_u_GSN-296339-M=7f1b5a49e053043f047200bb3a916153:4211:6895:1662053602720; 19509.vst=%7B%22s%22%3A%22%22%2C%22t%22%3A%22new%22%2C%22lu%22%3A1662053619475%2C%22lv%22%3A1662050607019%2C%22lp%22%3A0%7D; datadome=E7WGstA256Y0Ak26dBHyJ0NQnNpAatp2JOQSatN1SLPhAcTNG8T4Voj..4ZfGjvUm._J3tLebA7-NEZCkmveMe5dQxO39iXxJ3d2qGuV0~k4z2VO93dGNclymIS0FQg',
        'dnt': '1',
        'referer': 'https://www.drmartens.com.au/1460-8-eye-boot-smooth-11822006-bsm.html',
        'sec-ch-device-memory': '8',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="105.0.5195.54", "Not)A;Brand";v="8.0.0.0", "Chromium";v="105.0.5195.54"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-newrelic-id': 'VQcDVFdTDxABXVJbBgUPVVI=',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = (
        ('quote_item_id', ''),
        ('collect_qty', '1'),
        ('product_id', ""),
        ('simple_product_id', SampleProductID),
        ('collect_distance', '12742'),
        ('collect_postcode', '2000'),
    )

    response = requests.get('https://www.drmartens.com.au/collectplace/place/getplaces/current_product/', headers=headers, params=params)

    return response.json()