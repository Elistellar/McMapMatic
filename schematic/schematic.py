from PIL import Image
from litemapy import Region, BlockState


class Schematic:
    
    @classmethod
    def get_palette(cls, colors: dict[tuple[int, int, int], str]):
        _colors = []
        for color in colors.keys():
            _colors += list(color)
        
        palette = Image.new('P', (1, 1), 0)
        palette.putpalette(_colors)
        palette.convert('RGB')
        return palette
    
    @classmethod
    def edit_image(cls, image: bytes, palette: Image) -> Image:
        base_image = Image.open(image)
        square_image = Image.new(mode='RGB', size=(128, 128))
        square_image = base_image.convert('RGB').quantize(palette=palette).convert('RGB')
        return square_image
    
    @classmethod
    def generate(cls, image: Image, palette: dict[tuple[int, int, int], str]) -> "Schematic":
        region = Region(0, 0, 0, 128, 1, 128)
    
        schem = region.as_schematic(
            name='McMapMatic',
            author='Elistellar',
            description='Generated with Mc MapMatic'
        )
        
        for y in range(128):
            for x in range(128):
                pixel = image.getpixel((x, y))
                region.setblock(x, 0, y, BlockState(palette[pixel]))
        
        return schem
