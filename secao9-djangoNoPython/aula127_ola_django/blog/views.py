from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        'text': 'Olá blog',
        'title': 'Página blog - '
    }

    return render(
        request,
        'blog/index.html',
        context
    )


def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá exemplo',
        'title': 'Página exemplo - '
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )
