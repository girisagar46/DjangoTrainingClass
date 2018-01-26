from django.shortcuts import render

import requests
API_URL = "https://api.coinmarketcap.com/v1/ticker/?limit=10"


def get_data():
    crypto_data = requests.get(API_URL).json()
    return crypto_data


def crypto_view(request):
    data = get_data()
    ctx = {
        "coins" : data
    }

    return render(request, 'coin.html', context=ctx)


if __name__ == "__main__":
    get_data()