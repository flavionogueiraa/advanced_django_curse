'''
Shift + Alt + O para organizar as importações (vs code)
'''

from django.views.generic.detail import DetailView

from ..models import Person, Venda


class PersonDetailView(DetailView):
    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related(
            'documento'
        ).get(pk=pk)
    
    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)

        context['vendas'] = Venda.objects.filter(
            pessoa=self.object
        )

        return context
    