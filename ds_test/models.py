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


class Request(models.Model):
    time = models.DateTimeField(blank=False, null=False)
    path = models.CharField(max_length=2000, null=True, blank=True)
    method = models.CharField(max_length=7, null=False, blank=False)
    protocol = models.CharField(max_length=64, null=True, blank=True)
    remote_addr = models.CharField(max_length=64, null=True, blank=True)
    http_user_agent = models.TextField(null=True, blank=True)
    response_status = models.PositiveIntegerField(blank=False, null=False)