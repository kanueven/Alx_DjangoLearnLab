from django.db import models

# Create your models here.
#Create two models, Author and Book
#    Relationships:
  #  - A one-to-many relationship with Book (an author can have multiple books).
   #  - Many-to-one: Many books can belong to a single author.
    
 
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title