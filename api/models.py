from django.db import models


# creating a table 
class Note(models.Model):
    title=models.CharField(max_length=50) # Charfield = creates a title of 50 length 
    text=models.TextField() #infiite length
    def __str__(self):
        return self.title

#now simply we have to migrate so this will create a table notes in our database and it will have coloums 
