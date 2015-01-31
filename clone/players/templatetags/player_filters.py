from django import template

register = template.Library()

@register.filter(name='get_percentage')
def get_percentage(value):
	tfgs = value
	print('tfgs {}'.format(tfgs))
	r = value.split(',')
	made = r[0]
	attempted = r[1]
	return round(made/attempted, 3)