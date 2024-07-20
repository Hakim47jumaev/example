from django.db import models

class Author(models.Model):
    fname=models.CharField( max_length=50)
    lname=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    age=models.IntegerField()


    def __str__(self) -> str:
        return self.lname+' '+self.fname[0]+'.'

class Book(models.Model):

    GENRE=(
        (1,'Horor'),
        (2,'Historic'),
        (3,'Fantazy')
    )

    title=models.CharField( max_length=50)
    author=models.ForeignKey(Author,   on_delete=models.CASCADE)
    year_of_issue=models.DateField()
    genre=models.IntegerField(choices=GENRE)


    def __str__(self) -> str:
        return self.title