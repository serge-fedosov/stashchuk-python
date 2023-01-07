class Image:
    def __init__(self, title, resolution, extension) -> None:
        self.title = title
        self.resolution = resolution
        self.extension = extension

    def resize(self, resolution):
        self.resolution = resolution

image_1 = Image('image1', '1024x768', 'jpg')
image_2 = Image('image2', '1680x1080', 'png')
image_3 = Image('image3', '100x200', 'bmp')

print(image_1)
print(image_2)
print(image_3)

print(image_1.resolution)
image_1.resize('200x400')
print(image_1.resolution)
