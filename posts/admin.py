from django.contrib import admin

from posts.models import Debitcard, Loan, Transaction, contact, new_user

# Register your models here.
admin.site.register(new_user)
admin.site.register(contact)
admin.site.register(Loan)
admin.site.register(Transaction)
admin.site.register(Debitcard)