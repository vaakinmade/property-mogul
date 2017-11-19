from django.views import generic

from service.mogul_api.interface import MogulAPI


class SearchMogul(generic.ListView):
	context_object_name = "search_items"
	template_name = "listing/search_result.html"

	def get(self, request):
		books_list = services.get_books('2009', 'edwards')
		return render(request,'books.html',books_list)