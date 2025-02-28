import os
import uuid
import shutil
from enum import Enum
from pathlib import Path
from dataclasses import dataclass

from unreal_auto_mod import file_io, utilities


class UnrealGuid:
    """
    A class representing an Unreal Engine GUID (Globally Unique Identifier).
    
    Attributes:
        uid (str): The unique identifier (GUID) in uppercase format.
    
    Methods:
        __repr__() -> str: Returns the GUID as a string representation.
        generate_unreal_guid() -> str: Static method to generate a new UUID and return it as a string in uppercase format.
        to_uid() -> str: Returns the GUID as a string.
        from_uid(uid: str) -> UnrealGuid: Class method to create an UnrealGuid object from a given UID string.
    """
    
    def __init__(self, uid: str = None):
        """
        Initializes the UnrealGuid with a given UID string or generates a new one if not provided.
        
        Args:
            uid (str, optional): A string representing the GUID. If not provided, a new GUID is generated.
        """
        if uid:
            self.uid = uid.upper()
        else:
            self.uid = self.generate_unreal_guid()

    def __repr__(self) -> str:
        """
        Returns the GUID as a string representation.
        
        Returns:
            str: The GUID in uppercase format.
        """
        return self.uid

    @staticmethod
    def generate_unreal_guid() -> str:
        """
        Generates a new UUID (GUID) and returns it as a string in uppercase format.
        
        Returns:
            str: The generated UUID in uppercase.
        """
        return str(uuid.uuid4()).upper()

    def to_uid(self) -> str:
        """
        Returns the GUID as a string.
        
        Returns:
            str: The GUID.
        """
        return self.uid

    @classmethod
    def from_uid(cls, uid: str) -> 'UnrealGuid':
        """
        Creates an UnrealGuid object from a given UID string, converting it to uppercase.
        
        Args:
            uid (str): The GUID string to convert to an UnrealGuid object.
        
        Returns:
            UnrealGuid: A new UnrealGuid object created from the provided UID string.
        """
        return cls(uid.upper())


class UnrealCollectionColor:
    """
    A class representing a color with red, green, blue, and alpha components.
    
    Attributes:
        r (float): The red component of the color (between 0.0 and 1.0).
        g (float): The green component of the color (between 0.0 and 1.0).
        b (float): The blue component of the color (between 0.0 and 1.0).
        a (float): The alpha (opacity) component of the color (between 0.0 and 1.0).
    
    Methods:
        get_formatted_string() -> str: Returns the color components as a formatted string.
        get_red() -> float: Returns the red component of the color.
        get_green() -> float: Returns the green component of the color.
        get_blue() -> float: Returns the blue component of the color.
        get_alpha() -> float: Returns the alpha component of the color.
        __repr__() -> str: Returns the color as a formatted string for easy inspection.
    """
    
    def __init__(self, r: float, g: float, b: float, a: float):
        """
        Initializes the color with the given RGBA values.
        
        Args:
            r (float): The red component of the color (between 0.0 and 1.0).
            g (float): The green component of the color (between 0.0 and 1.0).
            b (float): The blue component of the color (between 0.0 and 1.0).
            a (float): The alpha (opacity) component of the color (between 0.0 and 1.0).
        """
        self.r = max(0.0, min(1.0, r))
        self.g = max(0.0, min(1.0, g))
        self.b = max(0.0, min(1.0, b))
        self.a = max(0.0, min(1.0, a))

    def get_formatted_string(self) -> str:
        """
        Returns the color components as a formatted string in the form of:
        (R=0.250000,G=0.018259,B=0.000337,A=1.000000).
        
        Returns:
            str: A string representing the color in a formatted way.
        """
        return f"(R={self.r:.6f},G={self.g:.6f},B={self.b:.6f},A={self.a:.6f})"

    def get_red(self) -> float:
        """
        Returns the red component of the color.
        
        Returns:
            float: The red component of the color.
        """
        return self.r

    def get_green(self) -> float:
        """
        Returns the green component of the color.
        
        Returns:
            float: The green component of the color.
        """
        return self.g

    def get_blue(self) -> float:
        """
        Returns the blue component of the color.
        
        Returns:
            float: The blue component of the color.
        """
        return self.b

    def get_alpha(self) -> float:
        """
        Returns the alpha (opacity) component of the color.
        
        Returns:
            float: The alpha component of the color.
        """
        return self.a

    def __repr__(self) -> str:
        """
        Returns the color as a formatted string for easy inspection.
        
        Returns:
            str: A string representing the color in a formatted way.
        """
        return self.get_formatted_string()


class UnrealAssetPath:
    """
    A class for managing Unreal Engine asset paths and references.

    Attributes:
        normalized_path (str): The normalized asset path with forward slashes.
        asset_reference (str): The full asset reference in the format "/path/to/asset.AssetName".

    Methods:
        normalize_path(path: str) -> str: Normalizes the provided path by replacing backslashes with forward slashes and trimming any surrounding slashes.
        to_asset_reference() -> str: Converts the normalized path into an asset reference in the format "/path/to/asset.AssetName".
        from_asset_reference() -> str: Extracts and returns the asset path from the asset reference (removes the asset name).
        __repr__() -> str: Returns the asset reference as a string representation.
    """
    
    def __init__(self, path: str):
        """
        Initializes the UnrealAssetPath with the given asset path.

        Args:
            path (str): The path to the asset, which will be normalized and converted into an asset reference.
        """
        self.normalized_path = self.normalize_path(path)
        self.asset_reference = self.to_asset_reference()

    def normalize_path(self, path: str) -> str:
        """
        Normalizes the provided asset path by replacing backslashes with forward slashes and trimming surrounding slashes.

        Args:
            path (str): The asset path to normalize.
        
        Returns:
            str: The normalized path with forward slashes and no surrounding slashes.
        """
        path = path.replace("\\", "/").strip("/")
        return f"/{path}"

    def to_asset_reference(self) -> str:
        """
        Converts the normalized path into an asset reference in the format "/path/to/asset.AssetName".

        Returns:
            str: The asset reference including both the normalized path and asset name.
        """
        asset_name = self.normalized_path.split("/")[-1]
        return f"{self.normalized_path}.{asset_name}"

    def from_asset_reference(self) -> str:
        """
        Extracts and returns the asset path from the asset reference (removes the asset name).

        Returns:
            str: The asset path without the asset name (e.g., "/path/to/asset").
        """
        if '.' in self.asset_reference:
            path, _ = self.asset_reference.rsplit('.', 1)
            return path
        return self.asset_reference

    def __repr__(self) -> str:
        """
        Returns the asset reference as a string representation.

        Returns:
            str: The asset reference in string format.
        """
        return self.asset_reference


class UnrealCollectionType(Enum):
    STATIC = 'Static'


@dataclass
class UnrealCollection:
    file_system_path: Path
    file_version: int
    file_type: UnrealCollectionType
    parent_guid: UnrealGuid
    guid: UnrealGuid
    color: UnrealCollectionColor


def are_any_collections_in_use(collections_directory: Path) -> bool:
    return get_number_of_collections(collections_directory) > 0


def get_number_of_collections(collections_directory: Path) -> int:
    return len(get_collections(collections_directory))


def get_collections_directory(uproject_directory: Path) -> Path:
    collections_directory = os.path.normpath(f'{uproject_directory}/Saved/Collections')
    os.makedirs(collections_directory, exist_ok=True)
    return collections_directory


def get_collections(collections_directory: Path) -> list[UnrealCollection]:
    return file_io.filter_by_extension(file_io.get_files_in_dir(collections_directory), '.collection')


def get_parent_collection(collection: UnrealCollection) -> UnrealCollection:
    parent_collection_file = None
    parent_guid = get_parent_guid(collection)
    if parent_guid and not parent_guid == get_blank_unreal_guid():
        all_collection_files = get_collections(get_collections_directory(utilities.get_uproject_dir()))
        for collection_file in all_collection_files:
            if get_guid(collection_file) == parent_guid:
                parent_collection_file = collection_file
                break
    return parent_collection_file


def get_file_version(collection: UnrealCollection) -> int:
    config_lines = file_io.get_all_lines_in_config(collection)
    config_line_prefix = 'FileVersion:'

    for line in config_lines:
        if line.startswith(config_line_prefix):
            return int(line.replace(config_line_prefix, ''))
    
    config_error = f'There was no "{config_line_prefix}" line in the following config "{collection}"'
    raise RuntimeError(config_error)


def get_type(collection: UnrealCollection) -> UnrealCollectionType:
    config_lines = file_io.get_all_lines_in_config(collection)
    config_line_prefix = 'Type:'

    for line in config_lines:
        if line.startswith(config_line_prefix):
            return line.replace(config_line_prefix, '')
    
    config_error = f'There is no "{config_line_prefix}" line in the following config "{collection}"'
    raise RuntimeError(config_error)


def get_guid(collection: UnrealCollection) -> UnrealGuid:
    config_lines = file_io.get_all_lines_in_config(collection)
    config_line_prefix = 'Guid:'

    for line in config_lines:
        if line.startswith(config_line_prefix):
            return line.replace(config_line_prefix, '')
    
    config_error = f'There is no "{config_line_prefix}" line in the following config "{collection}"'
    raise RuntimeError(config_error)


def get_parent_guid(collection: UnrealCollection) -> UnrealGuid:
    config_lines = file_io.get_all_lines_in_config(collection)
    config_line_prefix = 'ParentGuid:'

    for line in config_lines:
        if line.startswith(config_line_prefix):
            return line.replace(config_line_prefix, '')
    
    config_error = f'There is no "{config_line_prefix}" line in the following config "{collection}"'
    raise RuntimeError(config_error)


def get_collection_color(collection: UnrealCollection) -> UnrealCollectionColor:
    config_lines = file_io.get_all_lines_in_config(collection)
    config_line_prefix = 'Color:'

    for line in config_lines:
        if line.startswith(config_line_prefix):
            return line.replace(config_line_prefix, '')
    
    config_error = f'There is no "{config_line_prefix}" line in the following config "{collection}"'
    raise RuntimeError(config_error)


def add_paths_to_collection(collection: UnrealCollection, unreal_asset_paths: list[UnrealAssetPath]):
    for path in unreal_asset_paths:
        add_path_to_collection(collection, path)


def remove_paths_from_collection(collection: UnrealCollection, paths: list[UnrealAssetPath]):
    for path in paths:
        remove_path_from_collection(collection, path)


def rename_collection(collection: UnrealCollection, new_name: str):
    src_path = collection.file_system_path
    dst_path = os.path.normpath(f'{os.path.dirname(src_path)}/{new_name}.collection')
    if not os.path.isfile(src_path):
        not_found_error = f'The following collection file to be renamed was not found "{src_path}"'
        raise FileNotFoundError(not_found_error)
    if os.path.isfile(dst_path):
        dupe_name_error = f'The following collection already exists, so you cannot rename one to that "{dst_path}".'
        raise FileExistsError(dupe_name_error)
    shutil.move(src_path, dst_path)


def delete_collection(collection: UnrealCollection):
    collection_path = collection.file_system_path
    if os.path.isfile(collection_path):
        os.remove(collection_path)
    else:
        not_found_error = f'The following collection file to be deleted was not found "{collection_path}"'
        raise FileNotFoundError(not_found_error)
        

def get_all_non_key_lines(collection: UnrealCollection) -> list[str]:
    config_lines = file_io.get_all_lines_in_config(collection)
    removal_start_sub_strings = [
        'FileVersion:',
        'Type:',
        'Guid:',
        'ParentGuid:',
        'Color:'
    ]
    return [config_line for config_line in config_lines if not any(config_line.startswith(sub_string) for sub_string in removal_start_sub_strings)]


def get_blank_unreal_guid() -> UnrealGuid:
    return UnrealGuid(uid='00000000-0000-0000-0000-000000000000')


def set_collection_parent_collection(parent_collection: UnrealCollection, child_collection: UnrealCollection):
    return


def add_child_collection_to_parent_collection(child_collection: UnrealCollection, parent_collection: UnrealCollection):
    return


def add_child_collections_to_parent_collection(child_collections: list[UnrealCollection], parent_collection: UnrealCollection):
    return


def remove_child_collection_from_parent_collection(child_collection: UnrealCollection, parent_collection: UnrealCollection):
    return


def remove_child_collections_from_parent_collection(child_collections: list[UnrealCollection], parent_collection: UnrealCollection):
    return


def create_collection(
    guid: UnrealGuid, 
    parent_guid: UnrealGuid, 
    color: UnrealCollectionColor, 
    content_paths: list[UnrealAssetPath], 
    file_version: int, 
    type: UnrealCollectionType
):
    return


def enable_collection(collection: UnrealCollection):
    return


def disable_collection(collection: UnrealCollection):
    return


def set_collection_guid(collection: UnrealCollection, guid: UnrealGuid):
    return


def set_collection_parent_guid(collection: UnrealCollection, guid: UnrealGuid):
    return


def set_collection_color(r_color: float, g_color: float, b_color: float, a_color: float):
    return


def add_path_to_collection(collection: UnrealCollection, path: UnrealAssetPath):
    return


def get_collection_content_paths(collection: UnrealCollection) -> list[UnrealAssetPath]:
    return


def get_child_collections(collection: UnrealCollection) -> list[UnrealCollection]:
    return


def remove_path_from_collection(collection: UnrealCollection, path: UnrealAssetPath):
    return


def set_collection_type(collection_type: UnrealCollectionType):
    return


def set_collection_file_version(file_version: int):
    return


def add_collection_to_mod_entry(collection: UnrealCollection, mod_name: str, settings_json: Path):
    return


def remove_collection_from_mod_entry(collection: UnrealCollection, mod_name: str, settings_json: Path):
    return


def add_collections_to_mod_entry(collections: list[UnrealCollection], mod_name: str, settings_json: Path):
    return


def remove_collections_from_mod_entry(collections: list[UnrealCollection], mod_name: str, settings_json: Path):
    return


def get_collections_from_mod_entry(collections: list[UnrealCollection], mod_name: str, settings_json: Path):
    return


def process_guid(guid):
    # If a string is passed, convert it to an UnrealGuid instance, for cli usage
    if isinstance(guid, str):
        guid = UnrealGuid(guid)
