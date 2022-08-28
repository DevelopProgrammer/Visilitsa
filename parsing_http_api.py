import requests
def fetch(url, params):
  headers = params["headers"]
  body = params["body"]
  return requests.post(url, headers=headers, data=body)

response = fetch("https://auto.ru/-/ajax/desktop/listing/", {
  "headers": {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "same-origin",
    "sec-fetch-site": "same-origin",
    "x-client-app-version": "131.0.9909496",
    "x-client-date": "1661466060541",
    "x-csrf-token": "990a9fe16098b3b66417c36adb22bd65f2a7cfd02f49bc87",
    "x-page-request-id": "d3e2a6b0490d8178ec57b7d87ddb6eaa",
    "x-requested-with": "XMLHttpRequest",
    "x-retpath-y": "https://auto.ru/moskva/cars/vaz/all/on-credit/?geo_id=119749",
    "x-yafp": "{\"a1\":\"k50SxkEd3X4lkQ==;0\",\"a2\":\"fjiD0DfABXvjgLPAUVdm1DhMgCvm2g==;1\",\"a3\":\"l5qhF5PyQMX0A8mx0jNWcQ==;2\",\"a4\":\"lEUyJ2rc3JHpKLnHs+7tr61KlUB6VpWNmkjVLpOuYzVyYQ==;3\",\"a5\":\"hj6bO/Th+STR0w==;4\",\"a6\":\"UiE=;5\",\"a7\":\"mb61YJzTJYEYlg==;6\",\"a8\":\"oPulSPztot0=;7\",\"a9\":\"b59wUBcWZnN3uA==;8\",\"b1\":\"6T2xcKQ6PW4=;9\",\"b2\":\"TkCyYGgEm8kbTw==;10\",\"b3\":\"W3S9w9utxKS5Jg==;11\",\"b4\":\"GGyvDOVNLdA=;12\",\"b5\":\"1C+E1Gp0EJlgVg==;13\",\"b6\":\"gfHSqDMjL/bBdQ==;14\",\"b7\":\"r2XIofXtR6vxzQ==;15\",\"b8\":\"X+8LXdC9eDbDZg==;16\",\"b9\":\"fOfIjH8T2//kpQ==;17\",\"c1\":\"kLXJ3w==;18\",\"c2\":\"oqVtbTp27FfXTym+bzK/gg==;19\",\"c3\":\"38pudf7YcUINybXtWRC9CQ==;20\",\"c4\":\"F+yuQLmXUcw=;21\",\"c5\":\"5XcCK7LktN0=;22\",\"c6\":\"JOMQFA==;23\",\"c7\":\"Jd9/Y13FWjo=;24\",\"c8\":\"d8o=;25\",\"c9\":\"znWnC+Bc4xQ=;26\",\"d1\":\"bUuRNlKLFxk=;27\",\"d2\":\"Kxw=;28\",\"d3\":\"iwUSsZvbk9a8HA==;29\",\"d4\":\"jGBfahOalyg=;30\",\"d5\":\"2NQDQQl6qkM=;31\",\"d7\":\"dA/FVyEJP58=;32\",\"d8\":\"8LESb+ZncAI0bM9BDsHuauZTZol1liJ6CXI=;33\",\"d9\":\"w9iakWzvVho=;34\",\"e1\":\"x1HVuDy8Lkdd/w==;35\",\"e2\":\"TIu291xZ7Ew=;36\",\"e3\":\"lfUoIVXsI1M=;37\",\"e4\":\"ZaedY+Qyxms=;38\",\"e5\":\"gy3zS1akF0+r7Q==;39\",\"e6\":\"cH4CnRh2r2M=;40\",\"e7\":\"bron+CT+fBi6FA==;41\",\"e8\":\"RyLLs47imW8=;42\",\"e9\":\"KxNuDTBdKAI=;43\",\"f1\":\"CBhVFIBwmNpaew==;44\",\"f2\":\"/rdPRq2GBzU=;45\",\"f3\":\"bwpNG7DhUVEEnQ==;46\",\"f4\":\"pgzD12gXcjI=;47\",\"f5\":\"w0HvDhKMMeQLrw==;48\",\"f6\":\"f0KTMJzGMuDuBA==;49\",\"f7\":\"AHe/L3MChy+tww==;50\",\"f8\":\"jRNM5Ix0ebcMuQ==;51\",\"f9\":\"m1U/pSivFvM=;52\",\"g1\":\"+Aep/BIpNpn9Gg==;53\",\"g2\":\"LINDaOeBEVVkRw==;54\",\"g3\":\"05IgEHVKQn0=;55\",\"g4\":\"s1U5pgTX+NgGJA==;56\",\"g5\":\"VwQZQ8hdWUE=;57\",\"g6\":\"dI9fifqOOaA=;58\",\"g7\":\"JzbWhr4+DeM=;59\",\"g8\":\"P3FffzvdY3w=;60\",\"g9\":\"f2qgCFUpAD8=;61\",\"h1\":\"xLx+YnM/5KfIVw==;62\",\"h2\":\"sbEB9xaox/lZkw==;63\",\"h3\":\"4sTr3Q2yOHgQsw==;64\",\"h4\":\"HYpRnYkjR7WwBQ==;65\",\"h5\":\"tCx9Yf99waQ=;66\",\"h6\":\"rAZD2yxdEqei9w==;67\",\"h7\":\"sAOYRyE+iWjX1tFaHz4OX9hrdFgf7oNU+a4mk986nnBrnack;68\",\"h8\":\"aCmf67fyI7P64A==;69\",\"h9\":\"rvD/ZRE/Stj+mA==;70\",\"i1\":\"6wEZ0yR/ieU=;71\",\"i2\":\"aP3CNgmna3oKNw==;72\",\"i3\":\"9sEBGephYRXfMg==;73\",\"i4\":\"SKd/puDeeTBA9Q==;74\",\"i5\":\"tz3e5aJacNaKhQ==;75\",\"z1\":\"HuagcV1PHUhCvo4XKHIUcMFiYEB2HLkcXcXD3jQmRHtUuphvQnUDYkT/05Z64XSpEB14wh91VRNSfKsf4agOZw==;76\",\"z2\":\"Eo+CgmjoxRxTcwWclpSBzF46h2EsQJKyxhcj3jRX85UDR7UxopSTQfU7CBrXfxcV+gjXEykPjrfxJw8CP94HJQ==;77\",\"y2\":\"cDaPm44Dhou/zg==;78\",\"y3\":\"NMuMa7rmCtwygA==;79\",\"y6\":\"LAS6r75Sr32/GQ==;80\",\"y8\":\"NC9bRbrF/oyDmw==;81\",\"x4\":\"CLNn26owDNWzTg==;82\",\"z5\":\"2gSrXBIB/sw=;83\",\"z4\":\"nOaQsgd3xSCPQQ==;84\",\"z6\":\"VrNM4wibfm7LKGbh;85\",\"z7\":\"tyvCIwIa/HyinHWi;86\",\"z8\":\"w/HxLOuJXAL5F+iQzv4=;87\",\"z9\":\"PIEhkcnfXeZyFADQ;88\",\"y1\":\"oaj3bJRnsIFyOCKJ;89\",\"y4\":\"x7xBOROA4G2+FEkI;90\",\"y5\":\"/Qn2u2WAjvEbYKaCS3Q=;91\",\"y7\":\"ZhCvsxknzPF0S/Uo;92\",\"y9\":\"N82jZzMKEE7KQEJPVmQ=;93\",\"y10\":\"ZfDn3v2LWqjRsiUGTVQ=;94\",\"x1\":\"MZwgjZhNJ519jAU6;95\",\"x2\":\"fi++guvyRJKbQfzTAZ8=;96\",\"x3\":\"0BERXkTgFO3l7VtG;97\",\"x5\":\"/76c4pSZuFxMjCll;98\",\"z3\":\"9flxkhIUI5+8IKtMjnR34TEOPdKFWNx/Bk4Q8ANXqyY=;99\",\"v\":\"6.3.1\",\"pgrdt\":\"CGvwa8LJdcKJr5vVT4klscL61Wg=;100\",\"pgrd\":\"OjlIpQGIq3z43cjk31zxFi8x+7mssXgFkOu4x1G8G4gj4Z82/m+irDaqflIAU4I9HVqMaf1Rs0abxyGtpJhQeZZ7wqf1sSInfq3PtQNA21P7aB6k2qrD1om1SdIR3G+lFaB6g040alR6HFjyRqcU+xLzPa0elvwHxObBPuIe66VdmX6b+uA1TcaItPPSjGWySXVC8skoyTTqoZFs3N8MuYYOZb4=\"}",
    "cookie": "suid=4c1c7d9066b0dfb3b62e9c906ee14c00.52859ce24b6f2e7bf809e3f833ad9a1a; _csrf_token=990a9fe16098b3b66417c36adb22bd65f2a7cfd02f49bc87; autoru_sid=a%3Ag6307f3c62ub10ffanuiji2f44m20ne2.5974c8b5cff6030f74c6174c4f6effc5%7C1661465542732.604800.12ipVIbbewC4bWnREz6M0A.8zIiYQUYKNF7JbOqF93HsO1NOSk8KCcWQsL45ItIx3c; autoruuid=g6307f3c62ub10ffanuiji2f44m20ne2.5974c8b5cff6030f74c6174c4f6effc5; from=direct; yuidlt=1; yandexuid=6947023571515414909; my=YwA%3D; counter_ga_all7=2; crookie=IkERcpFcqBjpvYqHsEzFbW0Opght9WBhWlPm73rw1zucVrRn+mKdlWFMe6cs6mzWRSHNs9r6UABfe+vQNFbJXdUk0g8=; cmtchd=MTY2MTQ2NTU1MDg0OQ==; Session_id=3:1661465545.5.0.1633974065949:Gae_vA:4f.1.2:1|84340369.23564918.2.2:23564918|515084046.19540356.2.2:19540356|61:10006919.523361.Hfe8fUy3aUOfPKAR7Rphf2pwEro; yandex_login=serbul73; ys=udn.cDrQtNC40LzQsCDRgdC10YDQsQ%3D%3D#c_chck.32688056; i=WhDF3B3geE94LL4A17NrDAfgCw49FYtg0wZQc0Lr7HNEFluJycBDcpvzC1tPt1+pK8EIUIVZI1NIek2UrFv2/OfEQnw=; mda2_beacon=1661465545299; gdpr=0; _ym_isad=1; sso_status=sso.passport.yandex.ru:synchronized; _ym_uid=1661465553697968532; _yasc=P4qX/SVRUIIgafbsNClRHZGhl9YmTyFfJ3WqOIF0q9+ZtDev; layout-config={\"win_width\":855,\"win_height\":740}; from_lifetime=1661465951942; _ym_d=1661465951",
    "Referer": "https://auto.ru/moskva/cars/vaz/all/on-credit/?geo_id=119749",
    "Referrer-Policy": "no-referrer-when-downgrade"
  },
  "body": "{\"catalog_filter\":[{\"mark\":\"VAZ\"}],\"on_credit\":true,\"section\":\"all\",\"category\":\"cars\",\"output_type\":\"list\",\"geo_radius\":200,\"geo_id\":[119749]}",
  "method": "POST"
});

vas_date = response.json()
price = []
for car in vas_date["offers"]:
  price.append(car['price_info']['RUR'])
  print(f"{car['vehicle_info']['mark_info']['name'].ljust(5)} {car['vehicle_info']['model_info']['name'].ljust(5)} {car['price_info']['RUR']}р. {car['vehicle_info']['super_gen']['year_from']} года")
print()
print(f"Самое выгодное предложение по LADA ВАЗ: {min(price)}")