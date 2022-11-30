import os
from twocaptcha import TwoCaptcha


def solveRecaptcha(sitekey, url):
    api_key = '6a3fe4daa3e77f26f5235e8b615d3e33'

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
        sitekey=sitekey,
        url=url)

    except Exception as e:
        print(e)

    else:
        return result   