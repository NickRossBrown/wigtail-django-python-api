""" StreamFields live in here """

from wagtail.core import blocks

class TextBlock(blocks.StructBlock):
    """ basic text block """

    text = blocks.TextBlock(required=False, help_text='add text here')

    class Meta:
        label = "Text"
        icon = "edit"

class RichTextBlock(blocks.RichTextBlock):
    """ Rich text block """

    class Meta:
        label = "Rich Text"
        icon = "edit"