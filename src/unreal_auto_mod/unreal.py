from enum import Enum


class UnrealIostoreFileExtensions(Enum):
    """
    Enum for the file extensions for files that should end up in iostore utoc and ucas files
    If creating an iostore mod all files with extensions not within this list's corresponding string values 
    will be assumed to be pak assets
    """
    UMAP = 'umap'
    UEXP = 'uexp'
    UPTNL = 'uptnl'
    UBULK = 'ubulk'
    UASSET = 'uasset'
    USHADERBYTECODE = 'ushaderbytecode'


class LoadingPhases(Enum):
    """
    Enum for the loading phases, for descriptor files
    """
    EARLIEST_POSSIBLE = 'earliest_possible'
    POST_CONFIG_INIT = 'post_config_init'
    POST_SPLASH_SCREEN = 'post_splash_screen'
    PRE_EARLY_LOADING_SCREEN = 'pre_early_loading_screen'
    PRE_LOADING_SCREEN = 'pre_loading_screen'
    PRE_DEFAULT = 'pre_default'
    DEFAULT = 'default'
    POST_DEFAULT = 'post_default'
    POST_ENGINE_INIT = 'post_engine_init'
    NONE = 'none'
    MAX = 'max'


class UnrealHostTypes(Enum):
    """
    enum for the unreal host types, for descriptor files
    """
    RUNTIME = 'runtime'
    RUNTIME_NO_COMMANDLET = 'runtime_no_commandlet'
    RUNTIME_AND_PROGRAM = 'runtime_and_program'
    COOKED_ONLY = 'cooked_only'
    UNCOOKED_ONLY = 'uncooked_only'
    DEVELOPER = 'developer'
    DEVELOPER_TOOL = 'developer_tool'
    EDITOR = 'editor'
    EDITOR_NO_COMMANDLET = 'editor_no_commandlet'
    EDITOR_AND_PROGRAM = 'editor_and_program'
    PROGRAM = 'program'
    SERVER_ONLY = 'server_only'
    CLIENT_ONLY = 'client_only'
    CLIENT_ONLY_NO_COMMANDLET = 'client_only_no_commandlet'
    MAX = 'max'


class PackagingDirType(Enum):
    """
    enum for the directory type for packaging, it changes based on ue version
    """
    WINDOWS = 'windows'
    WINDOWS_NO_EDITOR = 'windows_no_editor'