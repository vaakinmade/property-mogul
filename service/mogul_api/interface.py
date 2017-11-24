import requests

from mogulfrontend.settings import MOGUL_API_BASE_HOST


def get_rent_listings():
	url = MOGUL_API_BASE_HOST + '/api/v1/listings/rent'
	response = requests.get(url)
	return response

def get_sale_listings():
	url = MOGUL_API_BASE_HOST + '/api/v1/listings/sale'
	response = requests.get(url)
	return response

def search_listings(**kwargs):
	url = MOGUL_API_BASE_HOST + '/api/v1/listings/search'
	response = requests.get(url, params=kwargs)
	return response

def detail_listings(listing_pk):
	url = MOGUL_API_BASE_HOST + '/api/v1/listings/' + listing_pk
	response = requests.get(url)
	return response