import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

@csrf_exempt
def index(request):
  if request.method == "POST":
    return index_POST(request)
  else:
    return index_GET(request)

def index_POST(request):
  data = json.loads(request.body)
  m = Message(name=data["name"], body=data["body"])
  m.save()
  body = json.dumps(m.id)
  return HttpResponse(body, "application/json")

def index_GET(request):
  if "since" in request.GET:
    id = int(request.GET["since"])
    messages = Message.objects.filter(id__gt=id)
  else:
    messages = Message.objects.all()
  data = []
  for m in messages:
    data.append({
      "id": m.id,
      "t": str(m.t),
      "name": m.name,
      "body": m.body,
    })
  body = json.dumps(data)
  return HttpResponse(body, "application/json")
