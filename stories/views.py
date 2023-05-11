from django.shortcuts import render

def index_view(request):
    products = [
        {
            "id": 1,
            "name": "Iphone 14 Pro Max",
            "price": 500
        },
        {
            "id": 2,
            "name": "Samsung Galaxy S13",
            "price": 300
        },
    ]

    context = {"products": products}
    return render(request, "index.html", context)
 
def form_view(request):
    return render(request, "form.html", {})