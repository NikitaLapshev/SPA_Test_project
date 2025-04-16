from django.http import HttpResponseBadRequest, JsonResponse
from django.views import View
from django.views.generic import ListView

from .forms import CommentForm
from .models import Comment


class AjaxCommentCreateView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return HttpResponseBadRequest('Only AJAX requests are allowed.')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            parent_id = request.POST.get('parent')
            if parent_id:
                try:
                    comment.parent = Comment.objects.get(id=parent_id)
                except Comment.DoesNotExist:
                    return JsonResponse({'success': False, 'error': 'Parent comment not found.'})
            if 'attachment' in request.FILES:
                comment.attachment = request.FILES['attachment']
            comment.save()
            return JsonResponse({'success': True, 'message': 'Comment successfully added.'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})

class CommentListView(ListView):
    model = Comment
    context_object_name = 'comments'
    paginate_by = 25

    def get_ordering(self):
        sort_by = self.request.GET.get('sort', '-date')
        valid_sorts = {
            'username': 'username',
            '-username': '-username',
            'email': 'email',
            '-email': '-email',
            'date': 'date',
            '-date': '-date',
        }
        return valid_sorts.get(sort_by, '-date')

    def get_queryset(self):
        return Comment.objects.filter(parent__isnull=True).order_by(self.get_ordering())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', '-date')
        context['comment_form'] = CommentForm()
        return context



