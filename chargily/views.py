from django.http import JsonResponse
from chargily.models import *

def invoice_json(request):
    results = {
        "invoices":[],
    }

    for client in Client.objects.all():
        line = [str(client), []]
        for invoice in client.invoice_set.all():
            line[1].append(str(invoice))

        results["invoices"].append(line)

    return JsonResponse(results)