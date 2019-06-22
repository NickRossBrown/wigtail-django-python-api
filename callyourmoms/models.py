from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index

from callyourmoms import blocks
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.api import APIField
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel


class MemberIndexPage(Page):
    index_page_content = RichTextField(blank=True)
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('index_page_content', classname="full")
    ]

    subpage_types = ['callyourmoms.MemberDetailPage']

    api_fields = [
        APIField("index_page_content"),
    ]

    def get_context(self, request, *args, **kwargs):
        """ adding custom stuff to our context """
        context = super().get_context(self, request, *args, **kwargs)
        context ["members"] = MemberDetailPage.objects.live().public()
        return context


class MemberDetailPage(Page):
    name = models.CharField(max_length=255)
    intro = models.CharField(max_length=250)
    best_finnish = models.CharField(max_length=250, null=True, blank=True)
    weekly_win_total = models.CharField(max_length=250, null=True, blank=True)
    playoffs_made = models.IntegerField(default=0)
    playoffs_won = models.IntegerField(default=0)
    profile_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='thumb nail images will be rendered 100 x 100 px'
    )
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
        ImageChooserPanel("profile_image"),
        FieldPanel("best_finnish"),
        FieldPanel("weekly_win_total"),
        FieldPanel("playoffs_made"),
        FieldPanel("playoffs_won"),
        StreamFieldPanel("content"),
    ]

    parent_page_types = ['callyourmoms.MemberIndexPage']
    subpage_types = []

    api_fields = [
        APIField("name"),
        APIField("intro"),
        APIField("profile_image"),
        APIField("best_finnish"),
        APIField("weekly_win_total"),
        APIField("playoffs_made"),
        APIField("playoffs_won"),
        APIField("content"),
    ]

    class Meta: 
        verbose_name = "Member Page"
        verbose_name_plural = "Members"


class ArticleIndexPage(Page):
    index_page_content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('index_page_content', classname="full")
    ]

    subpage_types = ['callyourmoms.ArticleDetailPage']

    api_fields = [
        APIField("index_page_content"),
    ]

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


class Author(models.Model):
    """An Author tag to be used for signatures"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    authors = models.ManyToManyField('Author')
    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    @property
    def year_date(self):
        return self.year

    api_fields = [
        APIField("thumbnail_image"),
        APIField("authors"),
        APIField("thumbnail_description"),
        APIField("week"),
        APIField("year"),
        APIField("year_date"),
        APIField("content"),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel("thumbnail_image"),
        FieldPanel('authors'),
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


class PodcastIndexPage(Page):
    index_page_content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('index_page_content', classname="full")
    ]

    subpage_types = ['callyourmoms.PodcastDetailPage']

    api_fields = [
        APIField("index_page_content"),
    ]

    def get_context(self, request, *args, **kwargs):
        """ adding custom stuff to our context """
        context = super().get_context(self, request, *args, **kwargs)
        context["podcasts"] = PodcastDetailPage.objects.live().public()
        return context


class PodcastDetailPage(Page):
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
        help_text='thumb nail images will be rendered 200 x 200 px'
    )
    description = models.CharField(max_length=250)
    week = models.CharField(
        max_length=50, choices=WEEK_CHOICES, blank=True, null=True)
    year = models.ForeignKey(
        YearTag,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    podcast_file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    authors = models.ManyToManyField('Author')

    api_fields = [
        APIField("thumbnail_image"),
        APIField("podcast_file"),
        APIField("description"),
        APIField("week"),
        APIField("year"),
        APIField("authors"),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel("thumbnail_image"),
        DocumentChooserPanel('podcast_file'),
        FieldPanel('week'),
        FieldPanel('year'),
        FieldPanel('description'),
        FieldPanel('authors'),
    ]

    parent_page_types = ['callyourmoms.PodcastIndexPage']
    subpage_types = []

    class Meta:
        verbose_name = "Podcast"
        verbose_name_plural = "Podcasts"
