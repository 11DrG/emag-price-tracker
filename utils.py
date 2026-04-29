import re


def parse_price(raw_text):
    return float(re.sub(r'[^\d,]', '', raw_text).replace(',', '.'))
