from django.db import models


NATIONALITY_CHOICES = [
      ('US', 'United States'),
      ('UK', 'United Kingdom'),
      ('CA', 'Canada'),
      ('AU', 'Australia'),
      ('IN', 'India'),
      ('BR', 'Brazil'),
      ('FR', 'France'),
      ('DE', 'Germany'),
      ('JP', 'Japan'),
      ('CN', 'China'),
      ('IT', 'Italy'),
      ('ES', 'Spain'),
      ('MX', 'Mexico'),
      ('RU', 'Russia'),
      ('ZA', 'South Africa'),
    # Add more nationalities as needed
]

class Actor(models.Model):
      name = models.CharField(max_length=100)
      birth_date = models.DateField(null=True, blank=True)
      nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, null=True, blank=True)

      def __str__(self):
          return self.name
      