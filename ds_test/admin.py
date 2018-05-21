from django.contrib import admin

from ds_test.models import Book, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_authors', 'isbn', 'price', 'publish_date')


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
