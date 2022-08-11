from django import template

register = template.Library()


# Регистрируем наш фильтр под именем censor, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   censor_list = ['редиска', 'обормот', 'баран']
   if not isinstance(value, str):
      raise ValueError('Фильтр цензурирования применяется только к переменным строкового типа')
   for word in censor_list:
      value = value.replace(word[1:],'*'*(len(word)-1))
   return value


