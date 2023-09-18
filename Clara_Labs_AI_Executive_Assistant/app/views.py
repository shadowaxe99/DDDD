
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import process_command

@csrf_exempt
def process_request(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        response = process_command(data)
        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Invalid request method'})

