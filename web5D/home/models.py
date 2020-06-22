from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from ckeditor_uploader.fields import RichTextUploadingField

class HomePage(Page):
    body = RichTextUploadingField(blank=True,null=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpage_1 = self.get_children().live()[:1].get()
        blogpage_2 = self.get_children().live()[1:2].get()
        blogpage_3 = self.get_children().live()[2:3].get()
        blogpage_4 = self.get_children().live()[3:4].get()
        blogpage_5 = self.get_children().live()[4:5].get()
        blogpage_6 = self.get_children().live()[5:6].get()
        blogpage_7 = self.get_children().live()[6:7].get()
        context['blogpage_1'] = blogpage_1
        context['blogpage_2'] = blogpage_2
        context['blogpage_3'] = blogpage_3
        context['blogpage_4'] = blogpage_4
        context['blogpage_5'] = blogpage_5
        context['blogpage_6'] = blogpage_6
        context['blogpage_7'] = blogpage_7
        return context

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class ProductsPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)    
    body = RichTextUploadingField(blank=True, null=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(ProductsPage, on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
