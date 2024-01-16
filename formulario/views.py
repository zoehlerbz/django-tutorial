from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, 'formulario.html')

@csrf_exempt
def formulario(request):
    if request.method == 'POST':    # O e-mail só será tratado se for enviado via 'POST'
        email = request.POST.get('chave')

        print(email)

        if email is not None:
            # Responda à requisição com sucesso
            response_data = {'status': 'success', 'message': str(email)}
            return JsonResponse(response_data)
        else:
            # Responda à requisição com erro
            response_data = {'status': 'error', 'message': 'Dado não encontrado.'}
            return JsonResponse(response_data)
    else:
        # Responda à requisição com erro, permitindo apenas requisições POST
        response_data = {'status': 'error', 'message': 'Apenas requisições POST são permitidas.'}
        return JsonResponse(response_data)