from mojang import MojangAPI



re = []



var = 0
usernames = ["AcaciaButton", "AcaciaDoor", "AcaciaFence", "AcaciaFenceGate", "AcaciaLeaves", "AcaciaLog", "AcaciaPlanks", "AcaciaPressurePlate", "AcaciaSapling", "AcaciaSign", "AcaciaSlab", "AcaciaStairs", "AcaciaTrapdoor", "AcaciaWood", "ActivatorRail", "Allium", "AmethystCluster", "AncientDebris", "Andesite", "AndesiteSlab", "AndesiteStairs", "AndesiteWall", "Anvil", "Azalea", "AzealeaLeaves", "AzureBluet", "Bamboo", "BambooShoot", "Barrel", "Barrier", "Basalt", "Beacon", "Bedrock", "BeeNest", "Beehive", "Beetroots", "Bell", "BigDripleaf", "BirchButton", "BirchDoor", "BirchFence", "BirchFenceGate", "BirchLeaves", "BirchLog", "BirchPlanks", "BirchPressurePlate", "BirchSapling", "BirchSign", "BirchSlab", "BirchStairs", "BirchTrapdoor", "BirchWood", "BlackBanner", "BlackBed", "BlackCarpet", "BlackConcrete", "BlackConcretePowder", "BlackGlazedTerracotta", "BlackShulkerBox", "BlackStainedGlass", "BlackStainedGlassPane", "BlackTerracotta", "BlackWool", "Blackstone", "BlackstoneSlab", "BlackstoneStairs", "BlackstoneWall", "BlastFurnace", "BlockOfAmethyst", "BlockOfCoal", "BlockOfCopper", "BlockOfDiamond", "BlockOfEmerald", "BlockOfGold", "BlockOfIron", "BlockOfLapisLazuli", "BlockOfNetherite", "BlockOfQuartz", "BlockOfRawCopper", "BlockOfRawGold", "BlockOfRawIron", "BlockOfRedstone"]


while "yes" == "yes":    
    fsf = MojangAPI.get_uuid(usernames[var])
    if not fsf:
        print(usernames[var])
    else:
        print(fsf)
    var = var + 1





    
    
