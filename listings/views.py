from django.views import generic
from django.shortcuts import render

from service.mogul_api import interface

import json
from iso8601 import parse_date


class SearchMogulView(generic.View):
	@staticmethod
	def convert_to_datetime(response):
		listing = list()
		for each in response.json():
			each.update({"created_at":parse_date(each['created_at'])})
			listing.append(each)
		return listing


	def get(self, request):
		query_dict = self.request.GET

		if query_dict:
			query = (query_dict.dict())
			response = interface.search_listings(**query)

			listings = {"listings" : SearchMogulView.convert_to_datetime(response)}
			return render(request, 'listings/search_result.html', listings)
		else:
			return render(request, 'listings/search_result.html')


class ListingDetailView(generic.View):

	def get(self, request, pk):
		response = interface.detail_listings(self.kwargs.get('pk'))
		listing = {"listing": response.json()}
		return render(request, 'listings/listing_detail.html', listing)