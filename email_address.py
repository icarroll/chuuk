import cairocffi as cairo

recording = cairo.RecordingSurface(cairo.CONTENT_COLOR_ALPHA, None)
rcontext = cairo.Context(recording)
with rcontext:
    rcontext.set_source_rgba(0,0,0,0)
    rcontext.paint()

rcontext.move_to(0,14)
rcontext.set_font_size(14)
text = "icarroll@pobox.com"
rcontext.show_text(text)

xoffset,yoffset, xsize,ysize = recording.ink_extents()
print xoffset,yoffset, xsize,ysize

surface = cairo.SVGSurface("content/extra/email_address.svg", xsize+xoffset*2, ysize+yoffset*2)
context = cairo.Context(surface)
context.set_source_surface(recording, 0, 0)
context.paint()
