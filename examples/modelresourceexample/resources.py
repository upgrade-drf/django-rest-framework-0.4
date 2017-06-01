from olddjangorestframework.resources import ModelResource
from olddjangorestframework.reverse import reverse
from modelresourceexample.models import MyModel


class MyModelResource(ModelResource):
    model = MyModel
    fields = ('foo', 'bar', 'baz', 'url')
    ordering = ('created',)

    def url(self, instance):
        return reverse('model-resource-instance',
                       kwargs={'id': instance.id},
                       request=self.request)
