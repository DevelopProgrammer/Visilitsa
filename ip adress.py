import requests
import folium

def get_info_IP(ip = "127.0.15.21"):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        #print(response)

        data = {
            '[IP]' : response.get('query'),
            '[Internet provide]' : response.get('isp'),
            '[Ширина]' : response.get('lat'),
            '[Долгота]' : response.get('lon'),
            '[Город]' : response.get('city'),
            '[Страна]' : response.get('country'),
            '[Почтовый индекс]' : response.get('zip'),
        }

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}')

        for i, j in data.items():
            print(f'{i} : {j}')
    except requests.exceptions.ConnectionError:
        print("Please check your connection")


def main():
    ip = input()
    get_info_IP(ip = ip)

if __name__ == '__main__':
    main()