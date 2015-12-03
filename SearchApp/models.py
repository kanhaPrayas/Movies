from django.db import models

# Create your models here.
class Users(models.Model):
	name   =  models.CharField(max_length = 255)
	dob    =  models.DateField(null = True, blank = True)
	gender =  models.CharField(max_length=1, null = True, blank = True)
	mobile_no = models.CharField(max_length = 10, unique = True, db_index = True)
	email_id = models.EmailField(max_length = 255, primary_key = True)
	role = models.CharField(max_length = 1)#0:admin,1:user
	status = models.CharField(max_length = 3)

	def __unicode__(self):
		return str(self.name)+'--'+str(self.mobile_no) +'--'+str(self.email_id)

'''
  {
    "99popularity": 83.0,
    "director": "Victor Fleming",
    "genre": [
      "Adventure",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz"
  }
'''


class Movies(models.Model):
	id = models.AutoField(primary_key=True)
	name   =  models.CharField(max_length = 255)
	director =  models.CharField(max_length = 255)
	genre =  models.CharField(max_length=255, null = True, blank = True)
	imdb_score =  models.FloatField(default = 0.0)
	popularity =  models.FloatField(default = 0.0)


	def __unicode__(self):
		return str(self.name)+'--'+str(self.director) +'--'+str(self.imdb_score)




