from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bookmarks.common.decorators import ajax_required, is_ajax
from .forms import ImageCreatForm
from .models import Image

# Create your views here.


@login_required
def image_create(request):
    if request.method == 'POST':
        # formulário foi enviado
        form = ImageCreatForm(data=request.POST)
        if form.is_valid():
            # os dados do formulário são válidos
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # atribui o usuário atual ao item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # redireciona para a view de detalhes do novo item criado
            return redirect(new_item.get_absolute_url())
    
    else:   # request.GET
        # cria o formulário com os dados fornecidos
        # pelo bookmarklet via GET
        form = ImageCreatForm(request.GET)

    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    
    return render(request,
                  'images/image/detail.html',
                  {'section': 'images',
                   'image': image})


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    
    return JsonResponse({'status':'error'})


@login_required
def image_list(request):
    images = Image.objects.all()
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, exibe a primeira página
        images = paginator.page(1)
    except EmptyPage:
        if is_ajax(request):
            # Se a requisição for AJAX e a página estive fora,
            # do intervalo, devolve uma página vazia
            return HttpResponse('')
        # Se a página estiver fora do intervalo,
        # exibe a última página de resultados
        images = paginator.page(paginator.num_pages)

    if is_ajax(request):
        return render(request,
                      'images/image/list_ajax.html',
                      {'section': 'images', 'images': images})
    
    return render(request,
                  'images/image/list.html',
                  {'section': 'images', 'images': images})