import os
import pygame
"""
Global constants
"""

# Colors
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 255) 
BLUE     = (  52, 152, 219)
GREEN    = (  46, 204, 113)
YELLOW   = ( 241, 196,  15)
RED      = ( 231,  76,  60)

# Screen dimensions
SCREEN_WIDTH  = 1000
SCREEN_HEIGHT = 600


# Paths images
"""
Player
"""
# Face
PLAYER_FACE     = pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Face.png"))
# Walk
PLAYER_WALKING_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (1).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (2).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (3).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (4).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (5).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (6).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (7).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (8).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (9).png")),
                        pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Walk/Walk (10).png"))
                        ]  
# Dead
PLAYER_DYING_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (1).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (2).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (3).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (4).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (5).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (6).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (7).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (8).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (9).png")),
                pygame.image.load(os.path.join("Assets", "Sprites/personage/Fox/Dead/Dead (10).png"))
                ]

"""
Enemies
"""
# Walk
ENEMY_DESERT_WALKING_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_000.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_001.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_002.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_003.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_004.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_005.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_006.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_007.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_008.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Desert Enemy/Walking/0_Golem_Walking_009.png"))
                            ]

ENEMY_JUNGLE_WALKING_FRAMES = [pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_000.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_001.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_002.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_003.png")),
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_004.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_005.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_006.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_007.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_008.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_009.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_010.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_011.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_012.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_013.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_014.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_015.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_016.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/jungle enemy/Walking/Golem_03_Walking_017.png"))
                            ]
ENEMY_SNOW_WALKING_FRAMES   = [pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_000.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_001.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_002.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_003.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_004.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_005.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_006.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_007.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_008.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_009.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_010.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_011.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_012.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_013.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_014.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_015.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_016.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_017.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_018.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_019.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_020.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_021.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_022.png")), 
                            pygame.image.load(os.path.join("Assets", "Sprites/Enemies/Snow enemy/Walking/0_Golem_Walking_023.png"))
                            ] 
# Dead

"""
Platforms
"""
# These constants define our platform types:
#   Path location of sprite
#   Width scale of sprite
#   Height scale of sprite

# Desert
DESERT_GRASS_LEFT    = (os.path.join("Assets", "Levels/Desert/Tile/14.png"), 70, 50)
DESERT_GRASS_MIDDLE  = (os.path.join("Assets", "Levels/Desert/Tile/15.png"), 70, 50)
DESERT_GRASS_RIGHT   = (os.path.join("Assets", "Levels/Desert/Tile/16.png"), 70, 50)
DESERT_STONE_PLATFORM_TOP_LEFT   = (os.path.join("Assets", "Levels/Desert/Tile/1.png"), 70, 70)
DESERT_STONE_PLATFORM_TOP_MIDDLE = (os.path.join("Assets", "Levels/Desert/Tile/2.png"), 70, 70)
DESERT_STONE_PLATFORM_TOP_RIGHT  = (os.path.join("Assets", "Levels/Desert/Tile/3.png"), 70, 70)
DESERT_STONE_PLATFORM_MIDDLE     = (os.path.join("Assets", "Levels/Desert/Tile/5.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_LEFT   = (os.path.join("Assets", "Levels/Desert/Tile/12.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_MIDDLE = (os.path.join("Assets", "Levels/Desert/Tile/9.png"), 70, 70)
DESERT_STONE_PLATFORM_BOTTOM_RIGHT  = (os.path.join("Assets", "Levels/Desert/Tile/13.png"), 70, 70)

# Jungle

# Snow

"""
Objects
"""
# These constants define our platform types:
#   Path location of sprite
#   Width scale of sprite
#   Height scale of sprite

# Standard
BLACKBERRY   = (os.path.join("Assets", "Sprites/Objects/Fruits/shadow/32.png"), 70, 70)

# Desert
DESERT_CACTUS  = (os.path.join("Assets", "Levels/Desert/Objects/Cactus (1).png"), 79, 80)
DESERT_CACTUS_2  = (os.path.join("Assets", "Levels/Desert/Objects/Cactus (3).png"), 67, 73)
DESERT_STONE = (os.path.join("Assets", "Levels/Desert/Objects/Stone.png"), 68, 40)
DESERT_SKELETON = (os.path.join("Assets", "Levels/Desert/Objects/Skeleton.png"), 90, 32)

# Jungle

# Snow