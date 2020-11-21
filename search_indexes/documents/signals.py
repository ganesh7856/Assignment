from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, **kwargs):
    """Update document on added/changed records.

    Update Product document index if related `Product.Category` (`Category`) fields have been updated
    in the database.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'products':
        # If it is `books.Publisher` that is being updated.
        if model_name == 'Category':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)

        # If it is `books.Author` that is being updated.
        if model_name == 'Product':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)

@receiver(post_delete)
def delete_document(sender, **kwargs):

    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'products':
        if model_name == 'Category':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)
                # registry.delete(_instance, raise_on_error=False)


        if model_name == 'Product':
            instances = instance.books.all()
            for _instance in instances:
                registry.update(_instance)
