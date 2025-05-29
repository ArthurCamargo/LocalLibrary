from django.db import models
from django.urls import reverse

from django.db.models import UniqueConstraint # Constraints field to
                                              # unique values
from djang.db.models.functions import Lower # Returns lower cased value of field

# Genre model

class Genre(models.Model):
    """ Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="""Enter a book genre (e.g. Science Fiction, French Poetry
                                       etc...)"""
    )

    def __str__(self):
        """ String for representing the Model object"""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        ordering = ["-name"]
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = """Genre already exists (case
                insensitive match)"""
            ),
        ]
