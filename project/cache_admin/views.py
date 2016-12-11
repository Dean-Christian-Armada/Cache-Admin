from django.core.cache import cache
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms


# Create your views here.


def key_value(key):
    val = cache.get(key)
    return {key: val}


def dashboard(request):
    keys = cache.keys('*')
    template = 'cache_admin/dashboard.html'
    context = {}
    data = map(key_value, keys)
    context['data'] = data
    context['title'] = 'Select cache to change'
    return render(request, template, context)

class CacheForm(forms.Form):
	key = forms.CharField(required=True)
	value = forms.CharField(required=True)

	def __init__(self, key=None, value=None, update=False,*args, **kwargs):
		super(CacheForm, self).__init__(*args, **kwargs)
		if update:
			self.fields['key'].widget.attrs['readonly'] = 'readonly'
			self.fields['key'].widget.attrs['value'] = key
			self.fields['value'].widget.attrs['value'] = value


def update(request, key_name):
    value = cache.get(key_name)
    form = CacheForm(key_name, value, True)
    template = 'cache_admin/form.html'
    post = request.POST
    if post:
    	val = post['value']
    	try:
    		val = eval(val)
    	except:
    		pass
    	cache.set(key_name, val)
    	return HttpResponseRedirect(reverse('admin:dashboard'))
    elif request.GET:
    	cache.delete(key_name)
    	return HttpResponseRedirect(reverse('admin:dashboard'))
    context = {}
    context['update'] = True
    context['name'] = 'Cache'
    context['form'] = form
    context['title'] = 'Update cache'
    context['delete'] = key_name
    return render(request, template, context)


def add(request):
	form = CacheForm
	template = 'cache_admin/form.html'
	post = request.POST
	if post:
		val = post['value']
		try:
			val = eval(val)
		except:
			pass
		cache.set(post['key'], val)
		return HttpResponseRedirect(reverse('admin:dashboard'))
	context = {}
	context['add'] = True
	context['name'] = 'Cache'
	context['form'] = form
	context['title'] = 'Add cache'
	return render(request, template, context)
