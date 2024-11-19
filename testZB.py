import requests

cookies = {
    '_gcl_au': '1.1.1644151718.1731558811',
    '_ga_1F6WJN99ZG': 'GS1.1.1731975106.2.1.1731975259.26.0.0',
    '_ga': 'GA1.1.877316510.1731558811',
    'cf_clearance': 'NGLVGGrt9kc14jCY4aVfPlf6535VxTBtmRG0CMOR_Ww-1731559110-1.2.1.1-GEAHsIpshZdshVR_l6JPaNM3T9.yYM6VRM.sg7o7Yi.SIp7BlvzLj66K_3G9bZTNys.FArZOV5F_KQ7TyUK1wC6Dtn5Cwn6TAjh4mAxpWjOGOpJJaANh7DQGbViTuy28XM68pucrbjG2IQR.J2Pxe9tWfk9Fgkh.cVzOrnVYKRC76N8kbDsLHHw1BxgIIaMVGSX0XA_kLzeixFcGVCj2c9Yb2y4pElE0CD0MgnrExD1UkdS_eclzEod5EJSBRP0aodnvp.QwY_N.JrgbtPxquDuMFyRkOjKrpH3rZxi5F3mon364G4pwnMoZLsX2B6So762Uy6qN9rdAspHGs5UoJ8VMC71G48D4QvvvNqc4Ysrp3u9H5hL1Oc4E3Zuh3bBL',
    'bblastvisit': '1731559117',
    'bblastactivity': '1731559126',
    'bbdiscussion_view': '{%22452933%22:1731559126}',
    'zabbix_language': 'en',
    'zbcfipc': 'VN',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.zabbix.com/',
    'Connection': 'keep-alive',
    # 'Cookie': '_gcl_au=1.1.1644151718.1731558811; _ga_1F6WJN99ZG=GS1.1.1731975106.2.1.1731975259.26.0.0; _ga=GA1.1.877316510.1731558811; cf_clearance=NGLVGGrt9kc14jCY4aVfPlf6535VxTBtmRG0CMOR_Ww-1731559110-1.2.1.1-GEAHsIpshZdshVR_l6JPaNM3T9.yYM6VRM.sg7o7Yi.SIp7BlvzLj66K_3G9bZTNys.FArZOV5F_KQ7TyUK1wC6Dtn5Cwn6TAjh4mAxpWjOGOpJJaANh7DQGbViTuy28XM68pucrbjG2IQR.J2Pxe9tWfk9Fgkh.cVzOrnVYKRC76N8kbDsLHHw1BxgIIaMVGSX0XA_kLzeixFcGVCj2c9Yb2y4pElE0CD0MgnrExD1UkdS_eclzEod5EJSBRP0aodnvp.QwY_N.JrgbtPxquDuMFyRkOjKrpH3rZxi5F3mon364G4pwnMoZLsX2B6So762Uy6qN9rdAspHGs5UoJ8VMC71G48D4QvvvNqc4Ysrp3u9H5hL1Oc4E3Zuh3bBL; bblastvisit=1731559117; bblastactivity=1731559126; bbdiscussion_view={%22452933%22:1731559126}; zabbix_language=en; zbcfipc=VN',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

response = requests.get(
    'https://www.zabbix.com/documentation/current/en/devel/modules/file_structure/actions',
    cookies=cookies,
    headers=headers,
)
print(response.status_code)
print(response.url)
#print(response.json())
print(response.history)
print(response.encoding)
with open ('zb.txt', 'w', encoding='utf-8') as file: 
    file.write(str(response.content))
