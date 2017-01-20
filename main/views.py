from django.shortcuts import render

# Create your views here.
def home(request):
	template = 'home.html'
	if request.method == 'POST':
		model = Hashtag(request.POST)
		# if model.is_valid():
			
		
	context = {}
	return render(request, template, context)
def about(request):
	template = 'about.html'
	context = {}
	return render(request, template, context)
def contact(request):
	template = 'contact.html'
	context = {}
	return render(request, template, context)