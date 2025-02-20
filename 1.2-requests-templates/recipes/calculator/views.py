from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def my_recipe(request, **kwargs):
    try:
        servings = int(request.GET.get('servings', 1))
        if servings <= 0:
            return HttpResponse('Неправильное кол-во порций')
    except ValueError:
        return HttpResponse('Ожидаю на ввод кол-во порций')
    context = {}
    for key, value in kwargs.items():
        if value in list(DATA.keys()) and servings == 1:
            context['recipe'] = DATA.get(value)
            return render(request, 'calculator/index.html', context)
        elif value in list(DATA.keys()) and servings != 1:
            internal_dict = DATA.get(value)
            copy_internal_dict = internal_dict.copy()
            for a, b in copy_internal_dict.items():
                copy_internal_dict[a] = b * servings
                context['recipe'] = copy_internal_dict
            return render(request, 'calculator/index.html', context)
        else:
            context = {}
            return render(request, 'calculator/index.html', context)
