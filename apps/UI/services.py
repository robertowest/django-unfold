import json
import random
from decimal import Decimal

# valor máximo de usuarios por celda para escalar la intensidad del color
MAX_COHORT_COUNT = 5000

# cada celda: (usuarios, porcentaje); usuarios 0 = celda vacía
COHORT_ROWS = [
    ('October 27, 2026', 40436, [(4098, 16), (4838, 52), (4645, 43), (4412, 31), (4256, 20), (4640, 92), (4071, 59), (4643, 35), (4833, 84)]),
    ('October 28, 2026', 32434, [(4382, 24), (4486, 19), (4261, 27), (3957, 65), (3467, 36), (3142, 43), (3138, 100), (3266, 31), (2335, 16)]),
    ('October 29, 2026', 24003, [(4064, 24), (4075, 55), (3491, 51), (2853, 86), (3074, 48), (2599, 39), (1421, 81), (1336, 22), (1090, 46)]),
    ('October 30, 2026', 18591, [(4503, 16), (4227, 35), (3365, 91), (2310, 78), (1954, 15), (1528, 49), (704, 11), (0, 0), (0, 0)]),
    ('October 31, 2026', 13651, [(4492, 23), (3699, 51), (3053, 17), (1316, 56), (1091, 63), (0, 0), (0, 0), (0, 0), (0, 0)]),
    ('November 01, 2026', 11455, [(4993, 41), (3542, 73), (1836, 84), (1084, 64), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]),
    ('November 02, 2026', 10137, [(4189, 76), (3309, 15), (1912, 67), (727, 30), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]),
    ('November 03, 2026', 8814, [(4165, 38), (3367, 76), (1282, 71), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]),
]

COHORT_GROUP_TOTALS = [34886, 31543, 23845, 16659, 13842, 11909, 9334, 9245, 8258]

SEGMENTS = [
    {'label': 'Marketing', 'percent': 44, 'color': 'bg-primary-600'},
    {'label': 'Analytics', 'percent': 40, 'color': 'bg-base-700 dark:bg-base-400'},
    {'label': 'Key account', 'percent': 16, 'color': 'bg-base-200 dark:bg-base-600'},
]

PROGRESS_STATS = [
    {'label': 'Weekly logins', 'value': '20,134', 'delta': '12%', 'trend': 'up'},
    {'label': 'Active sessions', 'value': '8,541', 'delta': '8%', 'trend': 'up'},
    {'label': 'Emails sent', 'value': '38,971', 'delta': '3%', 'trend': 'up'},
    {'label': 'Feedback received', 'value': '1,268', 'delta': '14%', 'trend': 'up'},
    {'label': 'Bug reports', 'value': '42', 'delta': '2%', 'trend': 'down'},
]

IMPORTANT_METRICS = [
    {'label': 'Total users', 'value': '12,847', 'delta': '15%', 'trend': 'up'},
    {'label': 'Active users', 'value': '8,932', 'delta': '8%', 'trend': 'up'},
    {'label': 'New signups', 'value': '1,456', 'delta': '23%', 'trend': 'up'},
    {'label': 'Churn rate', 'value': '234', 'delta': '5%', 'trend': 'down'},
    {'label': 'Monthly revenue', 'value': '89,567', 'delta': '12%', 'trend': 'up'},
    {'label': 'Conversion rate', 'value': '3.4', 'delta': '0%', 'trend': 'flat'},
    {'label': 'Avg session time', 'value': '247', 'delta': '7%', 'trend': 'up'},
    {'label': 'Bounce rate', 'value': '42.8', 'delta': '3%', 'trend': 'down'},
    {'label': 'Page views', 'value': '156,789', 'delta': '18%', 'trend': 'up'},
    {'label': 'Support tickets', 'value': '89', 'delta': '12%', 'trend': 'down'},
    {'label': 'Satisfaction', 'value': '4.7', 'delta': '2%', 'trend': 'up'},
    {'label': 'Mobile users', 'value': '7,834', 'delta': '25%', 'trend': 'up'},
    {'label': 'Email opens', 'value': '23,456', 'delta': '9%', 'trend': 'up'},
    {'label': 'Social shares', 'value': '1,234', 'delta': '14%', 'trend': 'up'},
    {'label': 'API calls', 'value': '456,789', 'delta': '6%', 'trend': 'up'},
    {'label': 'Server uptime', 'value': '99.9', 'delta': '0%', 'trend': 'flat'},
]

TOP_EARNINGS = [
    ('Oct. 22, 2025', Decimal('2341.89'), Decimal('1876.45')),
    ('Oct. 23, 2025', Decimal('1987.23'), Decimal('2109.67')),
    ('Oct. 24, 2025', Decimal('3456.78'), Decimal('1543.21')),
    ('Oct. 25, 2025', Decimal('1765.43'), Decimal('2987.65')),
    ('Oct. 26, 2025', Decimal('2876.54'), Decimal('1234.56')),
    ('Oct. 27, 2025', Decimal('1543.21'), Decimal('2765.43')),
    ('Oct. 28, 2025', Decimal('3210.98'), Decimal('1987.65')),
]


def get_cohort_rows():
    """
    Prepara las filas de la tabla de retención con la intensidad de color de cada celda.
    """
    filas = []
    for fecha, total, celdas in COHORT_ROWS:
        filas.append({
            'date': fecha,
            'total': f'{total:,}',
            'cells': [
                {
                    'users': usuarios,
                    'percent': porcentaje,
                    'empty': usuarios == 0,
                    # escalamos entre 5% y 60% para que el texto siga siendo legible
                    'intensity': 5 + min(55, round(usuarios / MAX_COHORT_COUNT * 55)),
                }
                for usuarios, porcentaje in celdas
            ],
        })
    return filas


def get_retention_context():
    """
    Devuelve todo el contenido de la página de retención.
    """
    return {
        'cohort_rows': get_cohort_rows(),
        'group_totals': [f'{total:,}' for total in COHORT_GROUP_TOTALS],
        'segments': SEGMENTS,
        'progress_stats': PROGRESS_STATS,
        'important_metrics': IMPORTANT_METRICS,
        'top_earnings': [
            (day, f'{income:,.2f}', f'{expenses:,.2f}')
            for day, income, expenses in TOP_EARNINGS
        ],
    }


# muestras del gráfico de salud: 240 puntos cada 2 minutos desde las 9:00
SYSTEM_SAMPLES = 240

SYSTEM_KPIS = [
    {'label': 'CPU Usage', 'value': '8,567', 'delta': '73%', 'trend': 'down'},
    {'label': 'Memory Usage', 'value': '16,384', 'delta': '45%', 'trend': 'up'},
    {'label': 'Disk Space', 'value': '2,048', 'delta': '89%', 'trend': 'down'},
]

SYSTEM_FUNCTIONS = [
    {'name': 'CPU usage', 'color': 'bg-red-500', 'time': '45.67 seconds', 'usage': 78, 'price': Decimal('89.23')},
    {'name': 'Memory usage', 'color': 'bg-orange-500', 'time': '89.12 seconds', 'usage': 34, 'price': Decimal('156.78')},
    {'name': 'Disk usage', 'color': 'bg-yellow-400', 'time': '156.89 seconds', 'usage': 67, 'price': Decimal('234.56')},
    {'name': 'Network usage', 'color': 'bg-yellow-300', 'time': '23.45 seconds', 'usage': 91, 'price': Decimal('67.89')},
    {'name': 'Error rate', 'color': 'bg-green-500', 'time': '78.34 seconds', 'usage': 2, 'price': Decimal('45.12')},
]


def _generar_serie(generador, base, variacion, minimo, maximo):
    """
    Genera una serie con variaciones suaves y algún pico, acotada entre minimo y maximo.
    """
    valores = []
    valor = base
    for _ in range(SYSTEM_SAMPLES):
        valor += generador.uniform(-variacion, variacion)
        if generador.random() < 0.03:
            valor += generador.uniform(variacion * 2, variacion * 4)
        valor = max(minimo, min(maximo, valor))
        valores.append(round(valor, 1))
    return valores


def get_system_chart_json():
    """
    Devuelve los datos del gráfico de líneas en formato JSON para el componente de unfold.
    """
    generador = random.Random(42)
    minutos = [9 * 60 + i * 2 for i in range(SYSTEM_SAMPLES)]
    etiquetas = [f'{m // 60}:{m % 60:02d}' for m in minutos]

    cpu = _generar_serie(generador, base=40, variacion=6, minimo=5, maximo=95)
    errores = _generar_serie(generador, base=2, variacion=1.5, minimo=0, maximo=12)

    return json.dumps({
        'labels': etiquetas,
        'datasets': [
            {
                'label': 'CPU',
                'data': cpu,
                'borderColor': 'var(--color-primary-600)',
                'pointRadius': 0,
                'fill': False,
                'maxTicksXLimit': 20,
            },
            {
                'label': 'Errores',
                'data': errores,
                'borderColor': '#e11d48',
                'pointRadius': 0,
                'fill': False,
                'maxTicksXLimit': 20,
            },
        ],
    })


def get_system_status_bars():
    """
    Devuelve las barras de estado del sistema (gris = intervalo sin datos).
    """
    barras = []
    for indice in range(60):
        # intervalos sin datos cada ciertas posiciones, como en la demo
        if indice in (9, 22, 36, 50, 56):
            barras.append({'color': 'bg-base-200 dark:bg-base-700', 'tooltip': 'Sin datos'})
        else:
            barras.append({'color': 'bg-primary-600', 'tooltip': 'Operativo'})
    return barras


def get_system_context():
    """
    Devuelve todo el contenido de la página de sistema.
    """
    return {
        'system_kpis': SYSTEM_KPIS,
        'system_chart_json': get_system_chart_json(),
        'system_status_bars': get_system_status_bars(),
        'system_functions': SYSTEM_FUNCTIONS,
    }


# dias de la semana en orden, empezando por el lunes
DIAS_SEMANA = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

PRODUCT_CARDS = [
    {'name': 'Product A', 'value': '$6,139.16', 'delta': '+1.17%'},
    {'name': 'Product B', 'value': '$8,622.47', 'delta': '+2.87%'},
    {'name': 'Product C', 'value': '$3,724.50', 'delta': '+8.01%'},
]

TRENDING_PRODUCTS = [
    {'name': 'Social marketing e-book', 'amount': '$6,600.57', 'percent': 63},
    {'name': 'Freelancing tasks', 'amount': '$3,900.63', 'percent': 29},
    {'name': 'Development coaching', 'amount': '$9,147.26', 'percent': 67},
    {'name': 'Product consulting', 'amount': '$7,702.20', 'percent': 85},
    {'name': 'Other income', 'amount': '$8,707.14', 'percent': 62},
    {'name': 'Course sales', 'amount': '$5,771.04', 'percent': 16},
    {'name': 'Ads revenue', 'amount': '$8,657.56', 'percent': 46},
]


def _etiquetas_desde(dia_inicio, cantidad):
    """
    Devuelve etiquetas de días consecutivos empezando por dia_inicio.
    """
    indice = DIAS_SEMANA.index(dia_inicio)
    return [DIAS_SEMANA[(indice + i) % 7] for i in range(cantidad)]


def get_commerce_performance_json():
    """
    Gráfico de barras positivas (ventas), negativas (gastos) y línea de tendencia.
    """
    generador = random.Random(7)
    etiquetas = _etiquetas_desde('Tue', 31)
    positivas = [generador.randint(40, 95) for _ in etiquetas]
    negativas = [-generador.randint(20, 70) for _ in etiquetas]
    tendencia = [generador.randint(45, 85) for _ in etiquetas]

    return json.dumps({
        'labels': etiquetas,
        'datasets': [
            {'label': 'Ventas', 'data': positivas, 'backgroundColor': 'var(--color-primary-600)', 'barThickness': 4},
            {'label': 'Gastos', 'data': negativas, 'backgroundColor': '#ef4444', 'barThickness': 4},
            {'label': 'Tendencia', 'data': tendencia, 'type': 'line', 'borderColor': 'var(--color-primary-300)', 'pointRadius': 0, 'fill': False},
        ],
    })


def _linea_semanal_json(semilla, base, variacion, color):
    """
    Serie de 29 días (4 semanas) para un gráfico de línea.
    """
    generador = random.Random(semilla)
    etiquetas = _etiquetas_desde('Mon', 29)
    valores = []
    valor = base
    for _ in etiquetas:
        valor = max(10, valor + generador.uniform(-variacion, variacion))
        valores.append(round(valor, 2))
    return json.dumps({
        'labels': etiquetas,
        'datasets': [
            {'label': 'Serie', 'data': valores, 'borderColor': color, 'pointRadius': 0, 'fill': False},
        ],
    })


def get_commerce_context():
    """
    Devuelve todo el contenido de la página de comercio.
    """
    return {
        'product_cards': PRODUCT_CARDS,
        'performance_chart_json': get_commerce_performance_json(),
        'revenue_chart_json': _linea_semanal_json(11, base=50, variacion=12, color='var(--color-primary-600)'),
        'expenses_chart_json': _linea_semanal_json(12, base=45, variacion=12, color='#ef4444'),
        'trending_products': TRENDING_PRODUCTS,
        'trending_total': '$1,234,567.89',
    }


GASTOS_CATEGORIAS = [
    {'name': 'Advertising', 'total': '$34,231', 'color': '#2563eb', 'items': [('Google Ads', '$18,750'), ('Meta Ads', '$12,340'), ('Other', '$3,141')]},
    {'name': 'Marketing', 'total': '$12,340', 'color': '#16a34a', 'items': [('Social Media', '$18,750'), ('Search Engines', '$12,340'), ('Other', '$3,141')]},
    {'name': 'Travel', 'total': '$18,750', 'color': '#ea580c', 'items': [('Hotels', '$8,920'), ('Flights', '$6,340'), ('Car Rentals', '$3,490')]},
    {'name': 'Food & Drinks', 'total': '$8,750', 'color': '#dc2626', 'items': [('Restaurants', '$4,250'), ('Cafes', '$2,890'), ('Supermarkets', '$1,610')]},
]

TOP_SPENDERS = [
    {'amount': '$22,500', 'name': 'John Doe', 'email': 'sample@example.com'},
    {'amount': '$18,500', 'name': 'Jane Doe', 'email': 'sample2@example.com'},
    {'amount': '$15,500', 'name': 'Jim Doe', 'email': 'sample3@example.com'},
]

RADAR_LABELS = ['Marketing', 'Operations', 'Technology', 'Personnel', 'Equipment', 'Utilities', 'Travel']


def get_spending_context():
    """
    Devuelve todo el contenido de la página de gastos, con los datos de los gráficos en JSON.
    """
    colores = ['var(--color-primary-900)', 'var(--color-primary-600)', 'var(--color-primary-500)', 'var(--color-primary-300)']
    reparto = {
        'labels': ['Advertising', 'Marketing', 'Travel', 'Food & Drinks'],
        'datasets': [{'data': [10, 20, 30, 40], 'backgroundColor': colores, 'borderWidth': 0}],
    }
    radar = {
        'labels': RADAR_LABELS,
        'datasets': [
            {'label': 'Este mes', 'data': [19, 6, 9, 6, 9, 9, 17], 'borderColor': 'var(--color-primary-600)', 'backgroundColor': 'rgba(124, 58, 237, 0.15)', 'pointRadius': 3},
            {'label': 'Mes anterior', 'data': [8, 11, 10, 5, 15, 4, 9], 'borderColor': 'var(--color-base-400)', 'backgroundColor': 'rgba(148, 163, 184, 0.15)', 'borderDash': [4, 4], 'pointRadius': 3},
        ],
    }
    return {
        'spending_categories': GASTOS_CATEGORIAS,
        'spending_top': TOP_SPENDERS,
        'spending_total': '$1,234,567.89',
        'spending_solid_percent': 44,
        'spending_striped_percent': 33.1,
        'doughnut_json': json.dumps(reparto),
        'pie_json': json.dumps(reparto),
        'radar_json': json.dumps(radar),
    }


def _serie_sparkline(semilla, base, variacion):
    """
    Serie corta para las mini gráficas de estado de pedidos.
    """
    generador = random.Random(semilla)
    valores = []
    valor = base
    for _ in range(60):
        valor = max(5, valor + generador.uniform(-variacion, variacion))
        valores.append(round(valor, 1))
    return json.dumps({
        'labels': list(range(len(valores))),
        'datasets': [{
            'label': 'Pedidos',
            'data': valores,
            'borderColor': 'var(--color-primary-600)',
            'pointRadius': 0,
            'fill': False,
            'tension': 0.3,
            'displayXAxis': False,
            'displayYAxis': False,
        }],
    })


PEDIDOS_ESTADISTICAS = [
    {'label': 'Pending', 'value': '201', 'delta': '24.2%', 'semilla': 21, 'base': 50, 'variacion': 10},
    {'label': 'Processing', 'value': '190', 'delta': '24.2%', 'semilla': 22, 'base': 40, 'variacion': 9},
    {'label': 'Delivered', 'value': '192', 'delta': '24.2%', 'semilla': 23, 'base': 55, 'variacion': 8},
    {'label': 'Cancelled', 'value': '203', 'delta': '24.2%', 'semilla': 24, 'base': 45, 'variacion': 12},
]

PEDIDO_PRODUCTOS = [
    {'name': 'Signal Ledger', 'quantity': 3, 'price': '€49,999.00', 'total': '€149,997.00'},
    {'name': 'Titan Workspace', 'quantity': 4, 'price': '€125.00', 'total': '€500.00'},
    {'name': 'Catalyst Operator', 'quantity': 4, 'price': '€14,999.00', 'total': '€59,996.00'},
    {'name': 'Ember Assistant', 'quantity': 3, 'price': '€5.00', 'total': '€15.00'},
    {'name': 'Ember Scheduler', 'quantity': 5, 'price': '€1,599.99', 'total': '€7,999.95'},
    {'name': 'Catalyst Terminal', 'quantity': 7, 'price': '€1,999.00', 'total': '€13,993.00'},
]

PEDIDOS = [
    {'number': 'ORD-1000', 'customer': 'Jasmine Taylor', 'products_count': 6, 'total': '€232,500.95', 'status': 'CANCELLED', 'expanded': True, 'products': PEDIDO_PRODUCTOS},
    {'number': 'ORD-0999', 'customer': 'Caitlin Ortiz', 'products_count': 4, 'total': '€885,679.50', 'status': 'SHIPPED'},
    {'number': 'ORD-0997', 'customer': 'Nathaniel Cox', 'products_count': 9, 'total': '€598,184.49', 'status': 'PENDING'},
    {'number': 'ORD-0996', 'customer': 'Scott Fernandez', 'products_count': 5, 'total': '€308,395.49', 'status': 'PENDING'},
    {'number': 'ORD-0995', 'customer': 'Adam Schmidt', 'products_count': 9, 'total': '€184,424.06', 'status': 'PROCESSING'},
    {'number': 'ORD-0994', 'customer': 'Amy Daugherty', 'products_count': 9, 'total': '€249,089.24', 'status': 'CANCELLED'},
    {'number': 'ORD-0993', 'customer': 'John Smith', 'products_count': 10, 'total': '€173,430.80', 'status': 'SHIPPED'},
    {'number': 'ORD-0992', 'customer': 'Nancy Ellison', 'products_count': 9, 'total': '€350,227.95', 'status': 'DELIVERED'},
]

PAGINAS = list(range(1, 11))


def get_orders_context():
    """
    Devuelve el contenido de la página de pedidos, con las mini gráficas en JSON.
    """
    estadisticas = [
        {**estadistica, 'sparkline_json': _serie_sparkline(estadistica['semilla'], estadistica['base'], estadistica['variacion'])}
        for estadistica in PEDIDOS_ESTADISTICAS
    ]
    return {
        'order_stats': estadisticas,
        'orders': PEDIDOS,
        'order_pages': PAGINAS,
        'orders_total': '999 orders',
    }
