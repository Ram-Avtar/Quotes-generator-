from django.shortcuts import render
from .models import Quotes

import random



def home(request):
	context={
		# 'post':random.choice(Quotes.objects.all()),
		'post':Quotes.objects.all(),
	}
	# items = Quotes.objects.all()
	# random_items = random.sample(items,7)
	# random.choice(Quotes.objects.all())
	return render(request,'quote/home.html',context)
# Create your views here.


# change 3 to how many random items you want

# if you want only a single random item
# random_item = random.choice(items)