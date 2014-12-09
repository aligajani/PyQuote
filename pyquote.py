__author__ = 'aligajani'

#   MIT License: www.aligajani.com
#   PyQuote | pyquote.py
#   Beautify your quotes

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class PyQuote():

    # Break quote into seperate lines

    def chunk(self, quote, step):

        line = quote.split()
        chunk = [ line [i:i+step] for i in range(0, len(line), step)]
        return chunk

    # Overlay quote on image with automatic adjustments

    def draw(self, chunk, author, template, font, size):

        # Load template image

        im = Image.open(template)
        draw = ImageDraw.Draw(im)

        # Set font sizes and types

        font_quote = ImageFont.truetype(font[0], size[0])
        font_author = ImageFont.truetype(font[1], size[1])

        # Overlay each line chunk from the raw quote

        for i in range(len(chunk)):
            draw.text((45, 75 * (i+1)), ' '.join(chunk[i]), (255, 255, 255), font=font_quote)

        # Get width of author text

        w = font_author.getsize(author)[0]

        exponential_padding = 750 - w
        draw.text((exponential_padding, 425), author, (255, 255, 255), font=font_author)

        # Draw a rectangle design which increases on quote size

        line_height = 85 * (len(chunk))
        draw.rectangle([0, 80, 12, line_height], fill=(231, 76, 60))

        # Save the image
        im.save('output.jpg', quality=100)


py = PyQuote()

quote = "Better beware of notions like genius and inspiration; they are a sort of magic wand and should be used sparingly by anybody who wants to see things clearly.."
author = "P .J. O'Rourke"

chunk = py.chunk(quote, 6)
py.draw(chunk, author, "vinkk-template.jpg", ["h-ul.ttf", "h-th.ttf"], [45, 50])