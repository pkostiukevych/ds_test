import json
import decimal
import datetime
import copy

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    def full_name(self):
        return ' '.join(filter(None, [self.first_name, self.middle_name, self.last_name]))

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=512, blank=False, null=False)
    authors = models.ManyToManyField(Author)
    isbn = models.CharField(max_length=17, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    publish_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.title

    def display_authors(self):
        return ', '.join([author.full_name() for author in self.authors.all()])

    # TODO add isbn correctness check

    def save(self, *args, **kwargs):
        new_data = copy.copy(self.__dict__)
        new_data.pop('_state')

        if self.id:
            instance = Book.objects.get(id=self.id)
            old_data = copy.copy(instance.__dict__)
            old_data.pop('_state')

            Logger.objects.create(action='edit', new_data=serialize_obj(new_data), old_data=serialize_obj(old_data))
        else:
            Logger.objects.create(action='create', new_data=serialize_obj(new_data))
        super(Book, self).save(*args, **kwargs)

    def delete(self):
        old_data = self.__dict__
        old_data.pop('_state')
        Logger.objects.create(action='delete', old_data=old_data)
        super(Book, self).delete()


class Request(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=2000, null=True, blank=True)
    method = models.CharField(max_length=7, null=False, blank=False)
    protocol = models.CharField(max_length=64, null=True, blank=True)
    remote_addr = models.CharField(max_length=64, null=True, blank=True)
    http_user_agent = models.TextField(null=True, blank=True)
    response_status = models.PositiveIntegerField(blank=False, null=False)


class Logger(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(choices=(('edit', 'edit'), ('create', 'create'), ('delete', 'delete')), max_length=6)
    old_data = models.TextField(blank=True, null=True, default=None)
    new_data = models.TextField(blank=True, null=True, default=None)


def serialize_obj(data):
    if 'price' in data and isinstance(data['price'], decimal.Decimal):
        data['price'] = '%.2f' % data['price']
    if 'publish_date' in data and isinstance(data['publish_date'], datetime.date):
        data['publish_date'] = data['publish_date'].strftime('%Y-%m-%d')
    return json.dumps(data)
