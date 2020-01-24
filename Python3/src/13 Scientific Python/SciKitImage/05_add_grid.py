import PIL.Image as Image
import PIL.ImageDraw as ImageDraw

    
image = Image.open("images/chris.cropped.jpg")
grid = Image.new('RGBA', size=(image.width, image.height), color=(255,255,255))
blank = Image.new('RGBA', size=(image.width, image.height), color=(255,255,255))
step_size = 50

gridCanvas = ImageDraw.Draw(grid)
for x in range(0, image.width, step_size):
    line = ((x, 0), (x, image.height))
    gridCanvas.line(line, fill=(0, 0, 0), width=1)
    
for y in range(0, image.height, step_size):
    line = ((0, y), (image.width, y))
    gridCanvas.line(line, fill=(0, 0, 0), width=1)

# Make sure images got an alpha channel
image = image.convert("RGBA")

imageWithGrid1 = Image.blend(image, grid, alpha=.05)
imageWithGrid2 = Image.blend(blank, grid, alpha=.025)
# imageWithGrid1.show()
# imageWithGrid2.show()
imageWithGrid1.save("images/chris_with_grid.jpg", "JPEG")
imageWithGrid2.save("images/grid.jpg", "JPEG")
