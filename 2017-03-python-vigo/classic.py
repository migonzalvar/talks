import os

import requests

EXCERPT_SIZE = 64


def main():
    print('Entro por aquí')
    api_key = os.getenv('API_KEY')
    url = 'http://servizos.meteogalicia.es/apiv3/findPlaces'
    params = dict(
        API_KEY=api_key,
        location='Vigo',
    )
    print('Pido url', url)
    r = requests.get(url, params=params)
    print('Esta es la respuesta:', r.status_code)
    print(r.text[:EXCERPT_SIZE], '...')

    url = 'http://servizos.meteogalicia.es/apiv3/getNumericForecastInfo'
    params = dict(
        API_KEY=api_key,
        locationIds=71956,
        variables='temperature',
    )
    print('Pido url', url)
    r = requests.get(url, params=params)
    print('Esta es la respuesta:', r.status_code)
    print(r.text[:EXCERPT_SIZE], '...')


if __name__ == '__main__':
    main()
