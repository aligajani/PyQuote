##PyQuote
#####Beautify your quotes


PyQuote is a simple script that allows you to overlay a quote and it's author on a well designed template. PyQuote is kind of clever too. The red bar grows with the number of lines in your text. 

![image](http://i.imgur.com/aTKFVQj.png)

####Installation

It works on Python 2+, and you need Pillow, the image manipulation library.

Install Pillow using `pip install Pillow`.


####Customization

Boot up PyQuote `py = PyQuote()` and let the magic begin.

This is where your quote and text data goes in.


`quote = "The best way to predict the future is to invent it."`

`author = "Alan Kay"`

You can customize the number of words per line. We have set it to `5` here.

`chunk = py.chunk(quote, 5)`

Then, to render or overlay the text on top of the template, do the following.

`py.draw(chunk, author, "vinkk-template.jpg", ["h-ul.ttf", "h-th.ttf"], [45, 50])`

The `draw()` method takes in 5 arguments:

* chunk - This is the raw quote text broken into line chunks
* author - This is the author text, such as `Alan Kay`
* template -  This is the file path to the template background
* font - This is a list in order [font for quote, font for author]
* size - This is a list in order [size for quote, size for quote]

That's all. Check out the [making](https://www.youtube.com/watch?v=WpNkFRj3cJk&feature=youtu.be) of PyQuote on Youtube. Enjoy

####License

The MIT License (MIT)

Copyright (c) Ali Gajani aligajani.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


