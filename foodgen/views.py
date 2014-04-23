from django.views import generic
from .models import Gen



class WelcomeView(generic.TemplateView):
    template_name = 'foodgen/welcome.html'



class GenList(generic.ListView):
    model = Gen


class RandomView(generic.ListView):
    model = Gen
    template_name = 'foodgen/random.html'
    context_object_name = 'random_food'
    queryset = Gen.objects.order_by('?')[:1]

class RandomFastFoodView(generic.ListView):
    model = Gen
    template_name = 'foodgen/random_fastfood.html'
    context_object_name = 'random_food'
    queryset = Gen.objects.filter(utype='fast food').order_by('?')[:1]


class RandomSitDownView(generic.ListView):
    model = Gen
    template_name = 'foodgen/random_sitdown.html'
    context_object_name = 'random_food'
    queryset = Gen.objects.filter(utype='sit down').order_by('?')[:1]


class RandomLessThanView(generic.ListView):
    model = Gen
    template_name = 'foodgen/random_lessthan10.html'
    context_object_name = 'random_food'
    queryset = Gen.objects.filter(price=True).order_by('?')[:1]

class RandomMoreThanView(generic.ListView):
    model = Gen
    template_name = 'foodgen/random_morethan10.html'
    context_object_name = 'random_food'
    queryset = Gen.objects.filter(price=False).order_by('?')[:1]