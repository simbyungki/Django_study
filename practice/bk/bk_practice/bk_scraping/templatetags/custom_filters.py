from django import template

register = template.Library()

@register.filter(name='get_temp_class')
def get_temp_class(value):
	return_class = ''
	if int(value) < 18 :
		return_class = 'cold'
	elif int(value) > 26 :
		return_class = 'hot'
	return return_class