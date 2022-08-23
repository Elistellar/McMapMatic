from math import floor

from litemapy import BlockState


class BaseColor:
    """
    Represent a Minecraft map color.
    cf https://minecraft.fandom.com/wiki/Map_item_format#Color_table
    """
    
    def __init__(self, id: int, color: tuple[int, int, int], blocks: list[BlockState]):
        self.id = id
        self.blocks = blocks
        
        self.color_1 = (floor(color[0] * 0.71), floor(color[1] * 0.71), floor(color[2] * 0.71))
        self.color_2 = (floor(color[0] * 0.86), floor(color[1] * 0.86), floor(color[2] * 0.86))
        self.color_3 = self.base_color = color
        self.color_4 = (floor(color[0] * 0.53), floor(color[1] * 0.53), floor(color[2] * 0.530))


colors = [
    BaseColor(1, (127, 178, 56), [
        BlockState('minecraft:grass_block'),
        BlockState('minecraft:slime_block'),
    ]),
    BaseColor(2, (247, 233, 163), [
        BlockState('minecraft:sand'),
        BlockState('minecraft:birch_planks'),
        BlockState('minecraft:birch_slab'),
        BlockState('minecraft:sandstone'),
        BlockState('minecraft:bone_block'),
        BlockState('minecraft:scaffolding'),
    ]),
    BaseColor(3, (199, 199, 199), [
        BlockState('minecraft:mushroom_stem'),
        BlockState('minecraft:cobweb'),
        BlockState('minecraft:white_candle'),
    ]),
    BaseColor(4, (255, 0, 0), [
        BlockState('minecraft:redstone_block'),
        BlockState('minecraft:tnt'), 
    ]),
    BaseColor(5, (160, 160, 255), [
        BlockState('minecraft:packed_ice'),
        BlockState('minecraft:ice'), 
        BlockState('minecraft:blue_ice'), 
    ]),
    BaseColor(6, (167, 167, 167), [
        BlockState('minecraft:iron_block'),
        BlockState('minecraft:grindstone'), 
        BlockState('minecraft:lodestone'), 
    ]),
    BaseColor(7, (0, 124, 0), [
        BlockState('minecraft:oak_leaves'),
        BlockState('minecraft:birch_leaves'),
        BlockState('minecraft:spruce_leaves'),
        BlockState('minecraft:jungle_leaves'),
        BlockState('minecraft:acacia_leaves'),
        BlockState('minecraft:dark_oak_leaves'),
        BlockState('minecraft:mangrove_leaves'),
        BlockState('minecraft:azalea_leaves'),
        BlockState('minecraft:flowering_azalea_leaves'),
    ]),
    BaseColor(8, (255, 255, 255), [
        BlockState('minecraft:snow_block'),
        BlockState('minecraft:white_wool'), 
        BlockState('minecraft:white_concrete'),
    ]),
    BaseColor(9, (164, 168, 184), [
        BlockState('minecraft:clay'),
    ]),
    BaseColor(10, (151, 109, 77), [
        BlockState('minecraft:dirt'),
        BlockState('minecraft:jungle_planks'),
        BlockState('minecraft:jungle_slab'),
        BlockState('minecraft:brown_mushroom_block'),
    ]),
    BaseColor(11, (112, 112, 112), [
        BlockState('minecraft:cobblestone'),
        BlockState('minecraft:cobblestone_slab'),
        BlockState('minecraft:stone'),
        BlockState('minecraft:stone_slab'),
    ]),
    BaseColor(12, (64, 64, 255), [
        BlockState('minecraft:water'),
    ]),
    BaseColor(13, (142, 119, 72), [
        BlockState('minecraft:oak_planks'),
        BlockState('minecraft:oak_slab'),
    ]),
    BaseColor(14, (255, 252, 245), [
        BlockState('minecraft:diorite'),
        BlockState('minecraft:diorite_slab'),
        BlockState('minecraft:quartz_block'),
        BlockState('minecraft:quartz_slab'),
    ]),
    BaseColor(15, (216, 127, 51), [
        BlockState('minecraft:acacia_planks'),
        BlockState('minecraft:acacia_slab'),
        BlockState('minecraft:red_sand'),
        BlockState('minecraft:orange_wool'),
        BlockState('minecraft:orange_concrete'),
        BlockState('minecraft:pumpkin'),
        BlockState('minecraft:red_sandstone'),
        BlockState('minecraft:red_sandstone_slab'),
        BlockState('minecraft:honey_block'),
        BlockState('minecraft:honeycomb_block'),
        BlockState('minecraft:waxed_copper_block'),
        BlockState('minecraft:waxed_cut_copper_slab'),
    ]),
    BaseColor(16, (178, 76, 216), [
        BlockState('minecraft:magenta_wool'),
        BlockState('minecraft:magenta_concrete'),
        BlockState('minecraft:purpur_block'),
        BlockState('minecraft:purpur_slab'),
    ]),
    BaseColor(17, (102, 153, 216), [
        BlockState('minecraft:light_blue_wool'),
        BlockState('minecraft:light_blue_concrete'),
    ]),
    BaseColor(18, (229, 229, 51), [
        BlockState('minecraft:yellow_wool'),
        BlockState('minecraft:yellow_concrete'),
        BlockState('minecraft:hay_block'),
        BlockState('minecraft:sponge'),
    ]),
    BaseColor(19, (127, 204, 25), [
        BlockState('minecraft:lime_wool'),
        BlockState('minecraft:lime_concrete'),
        BlockState('minecraft:melon'),
    ]),
    BaseColor(20, (242, 127, 165), [
        BlockState('minecraft:pink_wool'),
        BlockState('minecraft:pink_concrete'),
    ]),
    BaseColor(21, (76, 76, 76), [
        BlockState('minecraft:gray_wool'),
        BlockState('minecraft:gray_concrete'),
    ]),
    BaseColor(22, (153, 153, 153), [
        BlockState('minecraft:light_gray_wool'),
        BlockState('minecraft:light_gray_concrete'),
    ]),
    BaseColor(23, (76, 127, 153), [
        BlockState('minecraft:cyan_wool'),
        BlockState('minecraft:cyan_concrete'),
    ]),
    BaseColor(24, (127, 63, 178), [
        BlockState('minecraft:purple_wool'),
        BlockState('minecraft:purple_concrete'),
        BlockState('minecraft:mycelium'),
        BlockState('minecraft:amethyst_block'),
    ]),
    BaseColor(25, (51, 76, 178), [
        BlockState('minecraft:blue_wool'),
        BlockState('minecraft:blue_concrete'),
    ]),
    BaseColor(26, (102, 76, 51), [
        BlockState('minecraft:dark_oak_planks'),
        BlockState('minecraft:dark_oak_slab'),
        BlockState('minecraft:spruce_planks'),
        BlockState('minecraft:spruce_slab'),
        BlockState('minecraft:brown_wool'),
        BlockState('minecraft:brown_concrete'),
        BlockState('minecraft:soul_sand'),
    ]),
    BaseColor(27, (102, 127, 51), [
        BlockState('minecraft:green_wool'),
        BlockState('minecraft:green_concrete'),
        BlockState('minecraft:moss_block'),
        BlockState('minecraft:dried_kelp_block'),
    ]),
    BaseColor(28, (153, 51, 51), [
        BlockState('minecraft:red_wool'),
        BlockState('minecraft:red_concrete'),
        BlockState('minecraft:bricks'),
        BlockState('minecraft:brick_slab'),
        BlockState('minecraft:nether_wart_block'),
        BlockState('minecraft:mangrove_planks'),
        BlockState('minecraft:mangrove_slab'),
    ]),
    BaseColor(29, (25, 25, 25), [
        BlockState('minecraft:black_wool'),
        BlockState('minecraft:black_concrete'),
        BlockState('minecraft:obsidian'),
        BlockState('minecraft:coal_block'),
        BlockState('minecraft:basalt'),
        BlockState('minecraft:blackstone'),
        BlockState('minecraft:blackstone_slab'),
    ]),
    BaseColor(30, (250, 238, 77), [
        BlockState('minecraft:gold_block'),
        BlockState('minecraft:bell'),
    ]),
    BaseColor(31, (92, 219, 213), [
        BlockState('minecraft:prismarine_bricks'),
        BlockState('minecraft:prismarine_brick_slab'),
        BlockState('minecraft:diamond_block'),
    ]),
    BaseColor(32, (74, 128, 255), [
        BlockState('minecraft:lapis_block'),
    ]),
    BaseColor(33, (0, 217, 58), [
        BlockState('minecraft:emerald_block'),
    ]),
    BaseColor(34, (129, 86, 49), [
        BlockState('minecraft:spruce_planks'),
        BlockState('minecraft:spruce_slab'),
        BlockState('minecraft:podzol'),
    ]),
    BaseColor(35, (112, 2, 0), [
        BlockState('minecraft:netherrack'),
        BlockState('minecraft:nether_bricks'),
        BlockState('minecraft:magma_block'),
    ]),
    BaseColor(36, (209, 177, 161), [
        BlockState('minecraft:calcite'),
        BlockState('minecraft:white_terracotta'),
    ]),
    BaseColor(37, (159, 82, 36), [
        BlockState('minecraft:orange_terracotta'),
    ]),
    BaseColor(38, (149, 87, 108), [
        BlockState('minecraft:magenta_terracotta'),
    ]),
    BaseColor(39, (112, 108, 138), [
        BlockState('minecraft:light_blue_terracotta'),
    ]),
    BaseColor(40, (186, 133, 36), [
        BlockState('minecraft:yellow_terracotta'),
    ]),
    BaseColor(41, (103, 117, 53), [
        BlockState('minecraft:lime_terracotta'),
    ]),
    BaseColor(42, (160, 77, 78), [
        BlockState('minecraft:pink_terracotta'),
    ]),
    BaseColor(43, (57, 41, 35), [
        BlockState('minecraft:tuff'),
        BlockState('minecraft:gray_terracotta'),
    ]),
    BaseColor(44, (135, 107, 98), [
        BlockState('minecraft:light_gray_terracotta'),
    ]),
    BaseColor(45, (87, 92, 92), [
        BlockState('minecraft:cyan_terracotta'),
        BlockState('minecraft:mud'),
    ]),
    BaseColor(46, (122, 73, 88), [
        BlockState('minecraft:purple_terracotta'),
    ]),
    BaseColor(47, (76, 62, 92), [
        BlockState('minecraft:blue_terracotta'),
    ]),
    BaseColor(48, (76, 50, 35), [
        BlockState('minecraft:brown_terracotta'),
    ]),
    BaseColor(49, (76, 82, 42), [
        BlockState('minecraft:green_terracotta'),
    ]),
    BaseColor(50, (142, 60, 46), [
        BlockState('minecraft:red_terracotta'),
    ]),
    BaseColor(51, (37, 22, 16), [
        BlockState('minecraft:black_terracotta'),
    ]),
    BaseColor(52, (189, 48, 49), [
        BlockState('minecraft:crimson_nylium'),
    ]),
    BaseColor(53, (148, 63, 97), [
        BlockState('minecraft:crimson_planks'),
        BlockState('minecraft:crimson_slab'),
    ]),
    BaseColor(54, (92, 25, 29), [
        BlockState('minecraft:crimson_hyphae'),
    ]),
    BaseColor(55, (22, 126, 134), [
        BlockState('minecraft:warped_nylium'),
        BlockState('minecraft:oxidized_copper'),
    ]),
    BaseColor(56, (58, 142, 140), [
        BlockState('minecraft:warped_planks'),
        BlockState('minecraft:warped_slab'),
    ]),
    BaseColor(57, (86, 44, 62), [
        BlockState('minecraft:warped_hyphae'),
    ]),
    BaseColor(58, (20, 180, 133), [
        BlockState('minecraft:warped_wart_block'),
    ]),
    BaseColor(59, (100, 100, 100), [
        BlockState('minecraft:deepslate'),
    ]),
    BaseColor(60, (216, 175, 147), [
        BlockState('minecraft:raw_iron_block'),
    ]),
    BaseColor(61, (127, 167, 150), [
        BlockState('minecraft:glow_lichen'),
        BlockState('minecraft:verdant_froglight'),
    ]),
]
