class Text:
    """Component Interface"""
    def render(self):
        pass

class PlainText(Text):
    """Concrete Component"""
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text

class TextDecorator(Text):
    """Decorator"""
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return self._wrapped.render()

class BoldDecorator(TextDecorator):
    """Concrete Decorator for Bold"""
    def render(self):
        return f"<b>{super().render()}</b>"

class ItalicDecorator(TextDecorator):
    """Concrete Decorator for Italic"""
    def render(self):
        return f"<i>{super().render()}</i>"

# Usage
simple_text = PlainText("Hello, World!")
print(simple_text.render())  # Output: Hello, World!

bold_text = BoldDecorator(simple_text)
print(bold_text.render())    # Output: <b>Hello, World!</b>

italic_text = ItalicDecorator(simple_text)
print(italic_text.render())  # Output: <i>Hello, World!</i>f

bold_italic_text = ItalicDecorator(bold_text)
print(bold_italic_text.render())  # Output: <i><b>Hello, World!</b></i>
