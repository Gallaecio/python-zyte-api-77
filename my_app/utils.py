import os

from zyte_api import ZyteAPI

def omnifollow_product_extract(product_url):
    zyte_api_key = os.environ.get("ZYTE_API_KEY", "")  # or just set a static key
    client = ZyteAPI(api_key=zyte_api_key)
