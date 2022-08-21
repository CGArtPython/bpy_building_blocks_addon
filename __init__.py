import os
import sys

ADDON_FOLDER_PATH = os.path.dirname(__file__)
VERSION = (0, 0, 21)
MODULE_NAME = "bpybb"
ADDON_NAME = (
    f"[{MODULE_NAME}] bpy Building Blocks v{VERSION[0]}.{VERSION[1]}.{VERSION[2]}"
)

bl_info = {
    "name": "[bpybb] bpy Building Blocks v0.0.21",
    "author": "Viktor Stepanov",
    "version": (0, 0, 21),
    "blender": (2, 83, 0),
    "description": "A collection of helper functions and code used for speeding up Blender 3D Python script development.",
    "category": "Development",
    "doc_url": "https://github.com/CGArtPython/bpy_building_blocks_addon",
}


def register():
    print(f'ENABLED "{ADDON_NAME}" addon')

    print(f"\tadding {MODULE_NAME} to sys path: {ADDON_FOLDER_PATH}")
    sys.path.append(ADDON_FOLDER_PATH)


def unregister():
    print(f'DISABLE "{ADDON_NAME}" addon')

    print(f"\tremoving {MODULE_NAME} from sys path: {ADDON_FOLDER_PATH}")
    sys.path.remove(ADDON_FOLDER_PATH)


if __name__ == "__main__":
    register()
