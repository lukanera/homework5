from django.db import models
from datetime import date

class Library(models.Model):
    name = models.CharField(max_length=100, null=True)

class Member(models.Model):
    name = models.CharField(max_length=100, null=True)
    joined_date = models.DateField(null=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='member')

    def __str__(self):
        return f'{self.name} is in {self.library.name}'

class LibraryCard(models.Model):
    card_number = models.CharField(max_length=100, null=True)
    issue_date = models.DateField(null=True)
    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name="librarycards")

    def __str__(self):
        return f"{self.member.name} has library card number {self.card_number}"

class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    member = models.ManyToManyField(Member, related_name="books")

    def __str__(self):
        return f'{self.title}'

