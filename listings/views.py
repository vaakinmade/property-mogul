from django.views import generic
from django.shortcuts import render

from service.mogul_api import interface


class SearchMogulView(generic.View):

	def get(self, request):
		query_dict = self.request.GET

		if query_dict:
			query = (query_dict.dict())

			response = interface.search_listings(**query)
			listings = {"listings" : response.json()}
			return render(request, 'listings/search_result.html', listings)
		else:
			return render(request, 'listings/search_result.html')


#class ListingListView(generic.ListView):

