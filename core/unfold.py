from django.conf import settings
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static


def environment_callback(request):
    return (
        ['Desarrollo', 'primary']
        if settings.DEBUG
        else ['Producción', 'danger']
    )


def has_model_permission(user, app_label, model_name, action='view'):
    """
    Comprueba si un usuario tiene permiso sobre un modelo Django.

    Considera:
    - Permisos individuales.
    - Permisos heredados de grupos.
    - Superusuarios activos.

    Args:
        user: Instancia del usuario Django.
        app_label: Nombre de la aplicación.
        model_name: Nombre del modelo en minúsculas.
        action: add, change, delete o view.

    Returns:
        bool: True si tiene permiso, False en caso contrario.
    """
    valid_actions = {'add', 'change', 'delete', 'view'}

    if action not in valid_actions:
        raise ValueError(f'Acción no válida: {action}')

    if not user.is_authenticated or not user.is_active:
        return False

    permission = f'{app_label}.{action}_{model_name}'

    return user.has_perm(permission)


def is_superuser(request):
    return request.user.is_superuser


def is_normal_user(request):
    return not request.user.is_superuser


def dashboard_callback(request, context):
    context.update({
        'cards': [
            {'title': _('Usuarios'), 'metric': 128},
            {'title': _('Pedidos hoy'), 'metric': 14},
        ],
    })
    return context


def navigation_callback(request):
    user = request.user

    if not user.is_authenticated:
        return []

    if user.is_superuser:
        return ADMIN_NAVIGATION

    elif user.is_staff:
        return USER_NAVIGATION

    return DEFAULT_NAVIGATION


DEFAULT_NAVIGATION = []

ADMIN_NAVIGATION = [
    {
        'title': _('Navegación'),
        'separator': True,
        'collapsible': True,
        'items': [
            {
                'title': _('Usuarios'),
                'icon': 'person',
                'permission': is_superuser,
                'link': reverse_lazy('admin:auth_user_changelist'),
            },
            {
                'title': _('Grupos'),
                'icon': 'groups',
                'permission': is_superuser,
                'link': reverse_lazy('admin:auth_group_changelist'),
            },
        ],
    },
]

# menú lateral de unfold; los enlaces son '#' hasta sustituirlos por rutas reales
USER_NAVIGATION = [
    {
        'title': _('Dashboards'),
        'collapsible': False,
        'items': [
            {
                'title': _('Bienvenido'),
                'icon': 'speed',
                'link': '#',
                'items': [
                    {'title': _('Panel'),    'link': reverse_lazy('ui:dashboard')},
                    {'title': _('Sistema'),  'link': reverse_lazy('ui:system')},
                    {'title': _('Comercio'), 'link': reverse_lazy('ui:commerce')},
                    {'title': _('Gastos'),   'link': reverse_lazy('ui:spending')},
                ],
            },
        ],
    },
    {
        'title': _('Comercio'),
        'collapsible': False,
        'items': [
            {
                'title': _('Ordenes'),
                'icon': 'shopping_cart',
                'link': reverse_lazy('ui:orders'),
                'badge': '201',
                'badge_variant': 'warning',
                'badge_style': 'solid',
            },
            {
                'title': _('Products'),
                'icon': 'assignment_turned_in',
                'link': '#',
                'badge': '271',
                'badge_variant': 'info',
                'badge_style': 'solid',
            },
            {'title': _('Categories'), 'icon': 'category', 'link': '#'},
            {'title': _('Tags'), 'icon': 'tag', 'link': '#'},
        ],
    },
    {
        'title': _('CRM'),
        'collapsible': False,
        'items': [
            {'title': _('Customers'), 'icon': 'groups', 'link': '#'},
            {
                'title': _('Tickets'),
                'icon': 'event_note',
                'link': '#',
                'badge': '2',
                'badge_variant': 'danger',
            },
        ],
    },
    {
        'title': _('Packages'),
        'collapsible': False,
        'items': [
            {
                'title': _('Auth & Groups'),
                'icon': 'person',
                'link': '#',
                'items': [
                    {'title': _('Users'), 'link': '#'},
                    {'title': _('Groups'), 'link': '#'},
                ],
            },
            {
                'title': _('UI Elements'),
                'icon': 'auto_fix_high',
                'link': '#',
                'items': [{'title': _('Buttons'), 'link': '#'}],
            },
            {
                'title': _('Crispy Forms'),
                'icon': 'dynamic_form',
                'link': '#',
                'items': [
                    {'title': _('Vertical Form'), 'link': reverse_lazy('ui:forms')},
                    {'title': _('Horizontal Form'), 'link': '#'},
                    {'title': _('Formset'), 'link': '#'},
                ],
            },
            {
                'title': _('Celery Beat'),
                'icon': 'alarm_on',
                'link': '#',
                'items': [{'title': _('Periodic tasks'), 'link': '#'}],
            },
            {
                'title': _('Waffle'),
                'icon': 'flag',
                'link': '#',
                'badge': 'NEW',
                'badge_variant': 'primary',
                'items': [{'title': _('Flags'), 'link': '#'}],
            },
            {'title': _('Constance'), 'icon': 'settings', 'link': '#'},
        ],
    },
]

UNFOLD = {
    'SITE_TITLE': 'Administración de Mi Proyecto',
    'SITE_HEADER': 'Mi Proyecto',
    'SITE_SUBHEADER': 'Panel de control',
    'SITE_SYMBOL': 'speed',           # símbolo de Google Material Icons
    'SHOW_HISTORY': True,
    'SHOW_VIEW_ON_SITE': True,
    'ENVIRONMENT': 'core.unfold.environment_callback',
    'DASHBOARD_CALLBACK': 'core.unfold.dashboard_callback',
    'LOGIN': {
        'image': lambda request: static('images/login-bg.jpg'),
    },
    'SIDEBAR': {
        'show_search': lambda request: ( True if request.user.is_superuser else False ),
        'show_all_applications': True,
        'navigation': 'core.unfold.navigation_callback',
    },
}
