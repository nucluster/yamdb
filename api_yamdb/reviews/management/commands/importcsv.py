import csv
import os

from django.conf import settings
from django.core.management import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title, User

TABLES = {
    User: 'users.csv',
    Genre: 'genre.csv',
    Category: 'category.csv',
    Title: 'titles.csv',
    Review: 'review.csv',
    Comment: 'comments.csv',

}

CSV_FILE_PATH = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        for model, csv_f in TABLES.items():
            with open(
                    os.path.join(CSV_FILE_PATH, csv_f), encoding='utf-8'
            ) as csv_file:
                for record in csv.DictReader(csv_file):
                    if 'author' in record:
                        record['author_id'] = record.pop('author')
                    if 'category' in record:
                        record['category_id'] = record.pop('category')
                    model.objects.get_or_create(**record)
        self.stdout.write(
            self.style.SUCCESS('Success write to database'))
