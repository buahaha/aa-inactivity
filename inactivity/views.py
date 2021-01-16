from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render


@login_required
@permission_required("inactivity.basic_access")
def index(request):

    context = {"text": "Hello, World!"}
    return render(request, "inactivity/index.html", context)
