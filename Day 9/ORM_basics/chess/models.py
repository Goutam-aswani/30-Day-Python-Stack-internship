from django.db import models

class chess_openings(models.Model):
    first_move_by_white = models.CharField(max_length=5)
    first_move_by_black = models.CharField(max_length=5)

    opening_name = models.CharField(max_length=50)