from django import template

register = template.Library()


@register.inclusion_tag('core/components/paginator.html', takes_context=True,)
def render_paginator(context):
    request = context['request']
    paginator = context['paginator']
    page_obj = context['page_obj']

    # conservar filtros GET, excluyendo page
    params = request.GET.copy()
    params.pop('page', None)

    query = params.urlencode()
    page_query = f'{query}&' if query else ''

    return {
        'is_paginated': context['is_paginated'],
        'paginator': paginator,
        'page_obj': page_obj,
        'page_query': page_query,
        'paginas': paginator.get_elided_page_range(
            number=page_obj.number,
            on_each_side=3,
            on_ends=1,
        ),
    }
