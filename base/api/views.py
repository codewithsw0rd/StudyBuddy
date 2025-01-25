from rest_framework.decorators import api_view


def getRoute(request):
    routes = [
        'GET /api',
        'GET /api/rooms', 
        'GET /api/rooms/:id',
    ]

    return JsonResponse(routes, safe=False)