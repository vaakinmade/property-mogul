from django.views import generic
from django.shortcuts import render

from service.mogul_api import interface

import json
from iso8601 import parse_date


class SearchMogulView(generic.View):
	def convert_to_datetime(self, response):
		listing = list()
		for each in response.json().get('results'):
			each.update({"created_at":parse_date(each['created_at'])})
			listing.append(each)
		return listing

	def get(self, request):
		query_dict = self.request.GET

		if query_dict:
			query = (query_dict.dict())
			response = interface.search_listings(**query)

			listings = {"listings" : self.convert_to_datetime(response)}
			return render(request, 'listings/search_result.html', listings)
		else:
			return render(request, 'listings/search_result.html')


class ListingDetailView(generic.View):

	def split_features(self, response):
		listing = response.json()
		features_list = listing.get('features').split(",")
		listing.update({"features":features_list})
		return listing

	def get(self, request, pk):
		response = interface.detail_listings(self.kwargs.get('pk'))
		listing = {"listing": self.split_features(response)}
		return render(request, 'listings/listing_detail.html', listing)