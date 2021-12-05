import os

ADDON_FOLDER_PATH = os.path.dirname(__file__)
VERSION = (0, 0, 0)
MODULE_NAME = "bpybb"
ADDON_NAME = (
    f"[{MODULE_NAME}] bpy Building Blocks v{VERSION[0]}.{VERSION[1]}.{VERSION[2]}"
)

bl_info = {
    "name": "[bpybb] bpy Building Blocks v0.0.0",
    "author": "Viktor Stepanov",
    "version": (0, 0, 0),
    "blender": (2, 83, 0),
    "description": "Helper functions",
    "category": "Development",
    "doc_url": "https://github.com/CGArtPython/bpy_building_blocks_addon",
}


def register():
    print(f'ENABLED "{ADDON_NAME}" addon')


def unregister():
    print(f'DISABLE "{ADDON_NAME}" addon')


if __name__ == "__main__":
    register()
