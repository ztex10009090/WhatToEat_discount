# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponse
import json
from discount.models import *


# Create your views here.


def index(request):
    return HttpResponse("home")


def get_discount(request):
    test = {'test': 0}

    try:
        discounts = []
        for d in Discount.objects.all():
            discount = {'Store': d.Store, 'Discount_Number': d.Discount_Number, 'Deadline': d.Deadline,
                        'Notice': d.Notice}

            discounts.append(discount)
        test['discounts'] = discounts
        test['test'] = 1
    except Exception as error:
        test['message'] = str(error)
    return JsonResponse(test)
