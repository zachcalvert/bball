from django import template

register = template.Library()

@register.filter(name='format_date')
def format_date(value):
	days = ((0,'Sun'), 
            (1,'Mon'), 
            (2,'Tue'), 
            (3,'Wed'), 
            (4,'Thu'),  
            (5,'Fri'), 
            (6, 'Sat'),)
	date_object = value.date
	weekday = date_object.weekday()
	tup = days[weekday]
	day = tup[1]

	return '{0} {1} - {2}'.format(day, date_object, value.tipoff)



