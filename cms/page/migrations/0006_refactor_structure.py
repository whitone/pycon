# Generated by Django 4.1.7 on 2023-03-24 01:55

import base.blocks.accordion
from django.db import migrations
import page.blocks.slider_cards_section
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_add_illustration_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.fields.StreamField([('text_section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('is_main_title', wagtail.blocks.BooleanBlock(default=False, required=False)), ('subtitle', wagtail.blocks.CharBlock(required=False)), ('body', wagtail.blocks.RichTextBlock(required=False)), ('illustration', wagtail.blocks.ChoiceBlock(choices=[('cathedral', 'Cathedral'), ('florence', 'Florence'), ('florence2', 'Florence2'), ('handWithSnakeInside', 'Hand With Snake Inside'), ('snake1', 'Snake1'), ('snake2', 'Snake2'), ('snake4', 'Snake4'), ('snake5', 'Snake5'), ('snakeBody', 'Snake Body'), ('snakeCouple', 'Snake Couple'), ('snakeDNA', 'Snake D N A'), ('snakeHead', 'Snake Head'), ('snakeInDragon', 'Snake In Dragon'), ('snakeInDragonInverted', 'Snake In Dragon Inverted'), ('snakeLetter', 'Snake Letter'), ('snakeLongNeck', 'Snake Long Neck'), ('snakePencil', 'Snake Pencil'), ('snakeTail', 'Snake Tail'), ('snakeWithBalloon', 'Snake With Balloon'), ('snakeWithContacts', 'Snake With Contacts'), ('snakesWithBanner', 'Snakes With Banner'), ('snakesWithCocktail', 'Snakes With Cocktail'), ('snakesWithDirections', 'Snakes With Directions'), ('snakesWithOutlines', 'Snakes With Outlines'), ('tripleSnakes', 'Triple Snakes')], icon='image', required=False)), ('accordions', wagtail.blocks.ListBlock(base.blocks.accordion.Accordion)), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(required=False)), ('link', wagtail.blocks.CharBlock(required=False))]))])), ('map', wagtail.blocks.StructBlock([('longitude', wagtail.blocks.DecimalBlock(decimal_places=6, max_digits=9)), ('latitude', wagtail.blocks.DecimalBlock(decimal_places=6, max_digits=9)), ('zoom', wagtail.blocks.IntegerBlock(default=15)), ('link', wagtail.blocks.URLBlock())])), ('slider_cards_section', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(page.blocks.slider_cards_section.SimpleTextCard))]))], use_json_field=True),
        ),
    ]