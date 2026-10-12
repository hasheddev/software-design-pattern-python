#Appears as if it is the underlyting object

class Bitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        print(f"loading image from {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")

def draw_image(image):
    print("About to draw")
    image.draw()
    print("Done drawing image")


class LazyBitMap:
    def __init__(self, filename) -> None:
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()
    



if __name__ == "__main__":
    bmp = LazyBitMap("palm.jpg") #Bitmap("palm.jpg")
    #loads image without drawing
    draw_image(bmp)