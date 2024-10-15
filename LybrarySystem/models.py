from django.db import models

# Create your models here.
class Book(models.Model):
    bookAuthor = models.TextField()
    bookName = models.TextField() # models.TextField()
    bookDate = models.DateField()
    bookPageCount = models.IntegerField()
    bookInstances = models.IntegerField()
    #photolikecount = models.IntegerField()
    def __str__(self):
        return self.bookName

    def __repr__(self):
        return self.bookName

class Reader(models.Model):
    readerFirstName = models.TextField()
    readerSecondName = models.TextField() # models.TextField()
    bookBirthday = models.DateField()
    hashPassword = models.TextField()
    #bookInstances = models.IntegerField()
    #photolikecount = models.IntegerField()
    def __str__(self):
        return self.readerFirstName+' '+self.readerSecondName

    def __repr__(self):
        return self.readerFirstName+' '+self.readerSecondName

class BookANDReader(models.Model):
    bookID = models.TextField()
    readerID = models.TextField() # models.TextField()
    dateIssue  = models.DateField()
    dateIreceipt = models.TextField()
    #bookInstances = models.IntegerField()
    #photolikecount = models.IntegerField()
    def __str__(self):
        return self.bookID+' '+self.readerID

    def __repr__(self):
        return self.bookID+' '+self.readerID