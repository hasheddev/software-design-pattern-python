class TextStatus:
    def __init__(self):
        self.capitalize = False

class Sentence:
    def __init__(self, plain_text):
        self.text = plain_text
        self.words = plain_text.split(' ')
        self.capitalized = {}
    
    def __getitem__(self, key):
        status = self.capitalized.get(self.words[key], None)
        if status is None:
            status = TextStatus()
            self.capitalized[self.words[key]] = status
        return status
        
    def __str__(self):
        result = []
        for word in self.words:
            status = self.capitalized.get(word, None)
            if status is not None and status.capitalize:
                result.append(word.upper())
            else:
                result.append(word)
        return " ".join(result)