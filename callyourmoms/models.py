from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.search import index

from callyourmoms import blocks


class MemberIndexPage(Page):
    intro = RichTextField(blank=True)
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

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
            ("basic_text_block", blocks.TextBlock()),
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
    class Meta: 
        verbose_name = "Member Page"
        verbose_name_plural = "Members"