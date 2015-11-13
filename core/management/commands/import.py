# -*- coding: utf-8 -*-
import csv
from django.core.management.base import BaseCommand, CommandError
from core import models
from tagging.models import Tag


class Command(BaseCommand):
    help = 'Import database from csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def _process_row(self, row):
        (n, author_name, title, quantity, section_name, tags, only, exists) = row

        section_name = section_name.strip()
        section_name = section_name.replace('анрхизм', 'анархизм')
        section_name = section_name.replace('ин.яз', 'ин. яз.')
        section_name = section_name.replace('ин.яз.', 'ин. яз.')
        section_name = section_name.replace('иняз.', 'ин. яз.')
        section_name = section_name.replace('Иняз', 'ин. яз.')
        section_name = section_name.replace('иняз', 'ин. яз.')
        section_name = section_name.replace('ин. яз..', 'ин. яз.')
        section_name = section_name.replace('утопии-антиутопии', 'утопии - антиутопии')
        section_name = section_name.replace('Утопии - антиутопии', 'утопии - антиутопии')
        section_name = section_name.replace('худ. литра', 'художественная литература')
        section_name = section_name.replace('худ.лит-ра', 'художественная литература')
        section_name = section_name.replace('худ.литература', 'художественная литература')
        section_name = section_name.replace('худ.литра', 'художественная литература')
        section_name = section_name.replace('соц. теории. мрак', 'соц. теории')
        section_name = section_name.replace('соц. теории мрак', 'соц. теории')
        section_name = section_name.replace('теория  искусства', 'теория искусства')
        section_name = section_name.replace('филисофия', 'философия')
        section_name = section_name.replace('проф.пособия', 'проф. пособия')
        section_name = section_name.replace('соц.теории', 'соц. теории')
        section_name = section_name.replace('соцтеории', 'соц. теории')

        if section_name in ('НЕТ', '', ):
            section_name = 'отсуствует'

        author, _ = models.Author.objects.get_or_create(name=author_name)
        section, _ = models.Section.objects.get_or_create(name=section_name)
        book, _ = models.Book.objects.get_or_create(
            section=section,
            title = title,
            quantity=quantity or 1,
            quantity_total=quantity or 1
        )

        if not book.authors.filter(id=author.id).exists():
            book.authors.add(author)

        print tags
        Tag.objects.update_tags(book, tags)

    def handle(self, path, *args, **options):
        with open(path) as f:
            reader = csv.reader(f, delimiter=',', quotechar='"')
            reader.next()
            for row in reader:
                self._process_row(row)
