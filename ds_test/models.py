from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    def full_name(self):
        return ' '.join(filter(None, [self.first_name, self.middle_name, self.last_name]))


class Book(models.Model):
    title = models.CharField(max_length=512, blank=False, null=False)
    authors = models.ManyToManyField(Author)
    isbn = models.CharField(max_length=17, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    # TODO add isbn correctness check
