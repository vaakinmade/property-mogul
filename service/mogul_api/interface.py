import requests

from mogulfrontend.settings import MOGUL_API_BASE_HOST


def search_listings(**kwargs):
	url = MOGUL_API_BASE_HOST + '/api/v1/listings/search'
	response = requests.get(url, params=kwargs)
	print("result", response.status_code)
	return response

def detail_listings(listing_pk):
	url = MOGUL_API_BASE_HOST + '/api/v1/listings/' + listing_pk
	response = requests.get(url)
	print("result", response.status_code)
	return response