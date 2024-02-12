from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, './index.html')


def clothes(request):
    logger.debug('Clothes page accessed')
    return render(request, './clothes.html')


def footwear(request):
    logger.debug('Footwear page accessed')
    return render(request, './footwear.html')


def jacket(request):
    logger.debug('Jacket page accessed')
    return render(request, './jacket.html')
