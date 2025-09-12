from django.shortcuts import render
def show_gallery(request, count=2):
    images = [
        "pic1.jpg",
        "pic2.jpg",
        "pic3.jpg",
        "pic4.jpg",
    ]
    total = 4
    try:
        count = int(count)
    except ():
        count = 2
    if count < 1:
        images_to_show = []
        message = 'zero'
    else:
        images_to_show = images[:count]
        message = None
    context = {
        'images': images_to_show,
        'message': message,
        'requested_count': count,
        'total_images': total,
    }
    return render(request, 'gallery/gallery.html', context)