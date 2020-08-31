import requests
import favicon


def get_favicon(url):

    try:
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        headers = {'User-Agent': user_agent}
        icons = favicon.get(f"{url}", headers=headers, timeout=2)
    except:
        return ''

    try:
        return icons[0].url
    except:
        return ''
