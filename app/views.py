
from multiprocessing import context
from pydoc import describe
from django.shortcuts import render
from django.http.response import HttpResponse
# from django.http.request import HttpRequest
from dataclasses import dataclass


@dataclass
class Team:
    name: str
    description: str
    members: list






def list_teams (request):
    context ={
        "list_teams":["management","procurement","community","documentation"]
    }
    return render(request, "home.html" , context)


# teams_names={
#     Team("Management","Description","Brooks, Chevy, Errin, Kevin, Lukas, Andrew"),
#     Team("Procurement","Description","Mike, Dylan, Anna, Zaul, Luke, River"),
#     Team("Documentation","Description","Colt, Isaiah, Cooper, Cannon, Angela, Antonio, Gabriel"),
#     Team("Community","Description","Joshua, Malcolm, Amber, J.W, Eric"),
# }
  

def management(request):
    context={
        "m_details": ["Management","Description","Brooks, Chevy, Errin, Kevin, Lukas, Andrew"]
    }
    return render(request, "management.html", context)

def procurement(request):
    context={
        "p_details": ["Description","Mike, Dylan, Anna, Zaul, Luke, River"]
    }
    return render(request, "procurement.html", context)

def community(request):
    context={
        "c_details": ["Description","Colt, Isaiah, Cooper, Cannon, Angela, Antonio, Gabriel"]
    }
    return render(request, "community.html", context)

def documentation(request):
    context={
        "d_details": ["Description","Jashua, Malcolm, Amber, J.W, Eric"]
    }
    return render(request, "documentation.html", context)
