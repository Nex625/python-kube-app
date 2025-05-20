import random


class TextPopulator:
    def random_title(self):
        return random.choice(["Hello", "Test", "Demo"])

    def random_content(self):
        return random.choice(["Lorem ipsum", "Quick brown fox", "Sample text"])
