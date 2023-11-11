import requests
import json
import pycountry
from deep_translator import GoogleTranslator
import random

def do_translation(data, to_lang):
	translated = GoogleTranslator(source='auto', target=to_lang).translate(data)
	return translated
def translate_func(data,number):
	countries = [
    'af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu',
    'be', 'bn', 'bho', 'bs', 'bg', 'ca', 'ceb', 'ny',
    'co', 'hr', 'cs', 'da', 'dv', 'doi', 'nl', 'en', 'eo', 'et', 'ee', 'tl',
    'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw',
    'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja', 'jw',
    'kn', 'kk', 'km', 'rw', 'gom', 'ko', 'kri', 'ku', 'ckb', 'ky', 'lo', 'la',
    'lv', 'ln', 'lt', 'lg', 'lb', 'mk', 'mai', 'mg', 'ms', 'ml', 'mt', 'mi',
    'mr', 'mni-Mtei', 'lus', 'mn', 'my', 'ne', 'no', 'or', 'om', 'ps', 'fa',
    'pl', 'pt', 'pa', 'qu', 'ro', 'ru', 'sm', 'sa', 'gd', 'nso', 'sr', 'st',
    'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta',
    'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'ak', 'uk', 'ur', 'ug', 'uz',
    'vi', 'cy', 'xh', 'yi', 'yo', 'zu'
]
	random.shuffle(countries)
	country_amount = len(countries)
	latest_translation = data
	i = 0
	for country in countries:
		print(country)
		latest_translation = do_translation(latest_translation, country)
		print(latest_translation)
		i = i + 1
		print(str(round(i/number*100))+" % "+"completed")
		if i >= number:
			break

	latest = do_translation(latest_translation,"en")
	return latest