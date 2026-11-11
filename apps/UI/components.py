import json

from unfold.components import BaseComponent, register_component


@register_component
class BarChartComponent(BaseComponent):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "data": json.dumps(
                    {
                        "labels": ["Mo", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
                        "datasets": [
                            {
                                "label": "Dataset 1",
                                "data": [12, 19, 3, 5, 2, 3, 9],
                            }
                        ],
                    }
                )
            }
        )
        return context
