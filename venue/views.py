from django.shortcuts import render
from django.views.generic.base import View


class VenueView(View):
    template_name = 'venue/venue.html'

    def get(self, request):
        ctx = {
            'event_location': {'latlng': {'lat': 37.511235, 'lng': 127.059599}, 'info': {'content': 'pyconkr'}},
            'restaurant_list': [
                {'latlng': {'lat': 37.51282812457079, 'lng': 127.06401046341387}, 'info': {'content': 'restaurant a'}},
                {'latlng': {'lat': 37.50797304536229, 'lng': 127.05550115756093}, 'info': {'content': 'restaurant b'}},
                {'latlng': {'lat': 37.50869481112821, 'lng': 127.05637614122692}, 'info': {'content': 'restaurant c'}},
                {'latlng': {'lat': 37.50944375677513, 'lng': 127.06437136680920}, 'info': {'content': 'restaurant d'}},
                {'latlng': {'lat': 37.50748697015004, 'lng': 127.05506231989347}, 'info': {'content': 'restaurant e'}}
            ],
            'accommodation_list': [
                {'latlng': {'lat': 37.51435967683805, 'lng': 127.06337957404655}, 'info': {'content': 'accommodation a'}},
                {'latlng': {'lat': 37.51391291664461, 'lng': 127.06116283180526}, 'info': {'content': 'accommodation b'}},
                {'latlng': {'lat': 37.51015326590988, 'lng': 127.05474163454825}, 'info': {'content': 'accommodation c'}},
                {'latlng': {'lat': 37.51014856903361, 'lng': 127.05581894104238}, 'info': {'content': 'accommodation d'}},
                {'latlng': {'lat': 37.51302008170415, 'lng': 127.06338887595672}, 'info': {'content': 'accommodation e'}}
            ]
        } # dummy data
        return render(request, self.template_name, ctx)
