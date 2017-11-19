import requests

from mogulfrontend.settings import MOGUL_API_BASE_HOST


def search_listings(**kwargs):
	url = MOGUL_API_BASE_HOST + '/api/v1/listings/search'
	response = requests.get(url, params=kwargs)
	print("result", response.status_code)
	return response