import json
from pathlib import Path

from tempo_core import file_io


def get_unreal_engine_version(engine_path: Path) -> str:
    version_file_path = Path(f"{engine_path}/Engine/Build/Build.version")
    file_io.check_path_exists(version_file_path)
    with Path.open(version_file_path) as f:
        version_info = json.load(f)
        unreal_engine_major_version = version_info.get("MajorVersion", 0)
        unreal_engine_minor_version = version_info.get("MinorVersion", 0)
        return f"{unreal_engine_major_version}.{unreal_engine_minor_version}"
