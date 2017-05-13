from django.shortcuts import render, redirect

from .utils import graph_
# Create your views here.
def graph_view(request):
    context = {}
    results = graph_()
    context['results'] = results
    return render(request, 'srgraph/srgraph.html', context)



# def get_drugs(request):
#     if request.is_ajax():
#         q = request.GET.get('term', '')
#         drugs = Drug.objects.filter(short_name__icontains = q )[:20]
#         results = []
#         for drug in drugs:
#             drug_json = {}
#             drug_json['id'] = drug.rxcui
#             drug_json['label'] = drug.short_name
#             drug_json['value'] = drug.short_name
#             results.append(drug_json)
#         data = json.dumps(results)
#     else:
#         data = 'fail'
#     mimetype = 'application/json'
#     return HttpResponse(data, mimetype)
