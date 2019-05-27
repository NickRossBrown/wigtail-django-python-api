from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index

from callyourmoms import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField


class MemberIndexPage(Page):
    index_page_content = RichTextField(blank=True)
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('index_page_content', classname="full")
    ]

    subpage_types = ['callyourmoms.MemberDetailPage']

    def get_context(self, request, *args, **kwargs):
        """ adding custom stuff to our context """
        context = super().get_context(self, request, *args, **kwargs)
        context ["members"] = MemberDetailPage.objects.live().public()
        return context


class MemberDetailPage(Page):
    name = models.CharField(max_length=255)
    intro = models.CharField(max_length=250)
    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    search_fields = Page.search_fields + [
        index.SearchField('name'),
        index.SearchField('intro'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('intro'),
        StreamFieldPanel("content"),
    ]

    parent_page_types = ['callyourmoms.MemberIndexPage']
    subpage_types = []

    class Meta: 
        verbose_name = "Member Page"
        verbose_name_plural = "Members"


class ArticleIndexPage(Page):
    index_page_content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('index_page_content', classname="full")
    ]

    subpage_types = ['callyourmoms.ArticleDetailPage']

    def get_context(self, request, *args, **kwargs):
        """ adding custom stuff to our context """
        context = super().get_context(self, request, *args, **kwargs)
        context ["articles"] = ArticleDetailPage.objects.live().public()
        return context


class YearTag(models.Model):
    """A year tag to be used for articles"""
    year = models.CharField(max_length=255)

    def __str__(self):
        return self.year


class ArticleDetailPage(Page):
    WEEK_CHOICES = (
        ('undefined', 'UNDEFINED'),
        ('Week 1', 'WEEK-ONE'),
        ('Week 2', 'WEEK-TWO'),
        ('Week 3', 'WEEK-THREE'),
        ('Week 4', 'WEEK-FOUR'),
        ('Week 5', 'WEEK-FIVE'),
        ('Week 6', 'WEEK-SIX'),
        ('Week 7', 'WEEK-SEVEN'),
        ('Week 8', 'WEEK-EIGHT'),
        ('Week 9', 'WEEK-NINE'),
        ('Week 10', 'WEEK-TEN'),
        ('Week 11', 'WEEK-ELEVON'),
        ('Week 12', 'WEEK-TWELVE'),
        ('Week 13', 'WEEK-THIRTEEN'),
        ('Playoffs QuarterFinals', 'PLAYOFFS-QUARTERFINALS'),
        ('Playoffs SemiFinals', 'PLAYOFFS-SEMIFINALS'),
        ('Playoffs Championship', 'PLAYOFFS-CHAMPIONSHIP'),
        ('Pre-Season', 'PRE-SEASON'),
        ('Off-Season', 'OFF-SEASON'),
        ('Post-Season', 'POST-SEASON'),
    )
    thumbnail_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='thumb nail images will be rendered 100 x 100 px'
    )
    thumbnail_description = models.CharField(max_length=250)
    week = models.CharField(max_length=50, choices=WEEK_CHOICES, blank=True, null=True)
    year = models.ForeignKey(
        YearTag,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    api_fields = [
        APIField("thumbnail_image"),
        APIField("thumbnail_description"),
        APIField("week"),
        APIField("year"),
        APIField("content"),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel("thumbnail_image"),
        FieldPanel('thumbnail_description'),
        FieldPanel('week'),
        FieldPanel('year'),
        StreamFieldPanel("content"),
    ]

    parent_page_types = ['callyourmoms.ArticleIndexPage']
    subpage_types = []


    class Meta: 
        verbose_name = "Article"
        verbose_name_plural = "Articles"
