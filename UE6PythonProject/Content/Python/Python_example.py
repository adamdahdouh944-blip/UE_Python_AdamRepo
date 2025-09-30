import unreal

def getMaterialByPath(path):

    material = unreal.EditorAssetLibrary.load_asset(path)

    if material:
        unreal.log(f"Material {path} was loaded successfully!")
    else:
        unreal.log(f"Material {path} wasn't found")

    return material

def createMaterialinstance(parent_mat, asset_name, asset_path):
    assetTools = unreal.AssetToolsHelpers.get_asset_tools()
    matFactory = unreal.MaterialInstanceConstantFactoryNew()
    asset = assetTools.create_asset(asset_name, asset_path, None, matFactory)

    #Set Parent
    #parent_mat = unreal.EditorAssetLibrary.load_asset(parent_mat_dir)
    unreal.MaterialEditingLibrary.set_material_instance_parent(asset, parent_mat)

    return asset

parent_mat_path = "/Game/StarterContent/Materials/M_Water_Ocean.M_Water_Ocean"
parent_mat = getMaterialByPath(parent_mat_path)

new_material_asset = createMaterialinstance(parent_mat , "Python_Material", "/Game/CustomAssets")


