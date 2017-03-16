import os

import requests

EXCERPT_SIZE = 64


def main():
    print('Entro por aquí')
    url = 'http://httpbin.org/get'
    params = dict(
        location='Vigo',
    )
    print(f'Pido url {url}')
    r = requests.get(url, params=params)
    print(f'Esta es la respuesta: {r.status_code}')
    print(r.content)

    url = 'http://httpbin.org/status/201'
    params = dict(
        locationIds=71956,
        variables='temperature',
    )
    print(f'Pido url {url}')
    r = requests.get(url, params=params)
    print(f'Esta es la respuesta: {r.status_code}')
    print(r.content)


if __name__ == '__main__':
    main()
