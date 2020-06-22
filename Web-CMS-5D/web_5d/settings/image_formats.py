from wagtail.images.formats import Format, register_image_format, unregister_image_format

register_image_format(Format('right', 'Right-aligned',
                             'richtext-image right img-responsive', 'width-500'))
unregister_image_format('right')
