# Environment Variables

Tempo supports a number of environment variables for configuring engine paths, tool versions, caching, networking, and other behavior.

## Unreal Engine

### `UNREAL_ENGINE_DIRECTORY_MAJOR_MINOR`

Specifies the Unreal Engine installation directory for a specific major and minor version.

For example:

```text
UNREAL_ENGINE_DIRECTORY_5_7
```

### `TEMPO_UNREAL_ENGINE_DIRECTORY_MAJOR_MINOR`

Tempo-specific equivalent of `UNREAL_ENGINE_DIRECTORY_MAJOR_MINOR`.

For example:

```text
TEMPO_UNREAL_ENGINE_DIRECTORY_5_7
```

### `UNREAL_ENGINE_MAJOR_VERSION`

Specifies the Unreal Engine major version.

```text
UNREAL_ENGINE_MAJOR_VERSION=5
```

### `UNREAL_ENGINE_MINOR_VERSION`

Specifies the Unreal Engine minor version.

```text
UNREAL_ENGINE_MINOR_VERSION=7
```

### `TEMPO_UNREAL_ENGINE_MAJOR_VERSION`

Tempo-specific Unreal Engine major version.

```text
TEMPO_UNREAL_ENGINE_MAJOR_VERSION=5
```

### `TEMPO_UNREAL_ENGINE_MINOR_VERSION`

Tempo-specific Unreal Engine minor version.

```text
TEMPO_UNREAL_ENGINE_MINOR_VERSION=7
```

---

## Tempo

### `TEMPO_PERSISTENT_MODS_DIRECTORY`

Specifies the directory where Tempo should store persistent mod data

```text
TEMPO_PERSISTENT_MODS_DIRECTORY=C:\Tempo\Mods
```

### `TEMPO_DUMP_PATTERNSLEUTH_VERSION`

Specifies the version of PatternSleuth used by Tempo when dumping or inspecting Unreal Engine data.

```text
TEMPO_DUMP_PATTERNSLEUTH_VERSION=1.2.3
```

### `TEMPO_REPAK_PACK_VERSION`

Specifies the version of the repak package format to use.

```text
TEMPO_REPAK_PACK_VERSION=4
```

### `TEMPO_REPAK_COMPRESSION_TYPE`

Specifies the compression type used when creating repak archives.

```text
TEMPO_REPAK_COMPRESSION_TYPE=Zlib
```

---

## PatternSleuth

### `PATTERNSLEUTH_RES_EngineVersion`

Specifies the Unreal Engine version used by PatternSleuth resource data.

```text
PATTERNSLEUTH_RES_EngineVersion=5.7
```

---

## Network / Online Mode

### `TEMPO_FORCE_ONLINE`

Forces Tempo and supported tools to operate in online mode.

```text
TEMPO_FORCE_ONLINE=1
```

### `TEMPO_FORCE_OFFLINE`

Forces Tempo and supported tools to operate in offline mode.

```text
TEMPO_FORCE_OFFLINE=1
```

> `TEMPO_FORCE_ONLINE` and `TEMPO_FORCE_OFFLINE` should not normally be enabled at the same time.

---

## GitHub

### `GITHUB_TOKEN`

Provides a GitHub authentication token for operations that require access to the GitHub API.

```text
GITHUB_TOKEN=...
```

> Avoid committing authentication tokens to source control.

---

## Tool Caching

The following variables use `TOOLNAME` as a placeholder for the name of the relevant tool.

### `TOOLNAME_NO_CACHE`

Disables caching for the tool.

```text
TOOLNAME_NO_CACHE=1
```

### `TOOLNAME_CACHE_DIR`

Specifies the directory used for the tool's cache.

```text
TOOLNAME_CACHE_DIR=C:\Tempo\Cache
```

### `TOOLNAME_CACHE_FORCE_ONLINE`

Forces the tool to use online resources when resolving cached resources.

```text
TOOLNAME_CACHE_FORCE_ONLINE=1
```

### `TOOLNAME_CACHE_FORCE_OFFLINE`

Forces the tool to operate using locally cached resources.

```text
TOOLNAME_CACHE_FORCE_OFFLINE=1
```

### `TEMPO_TOOLNAME_RELEASE_TAG`

Forces the tool to use a specific release tag for a specific tool.

```text
TEMPO_TOOLNAME_RELEASE_TAG=1.3
```

### `TEMPO_TOOLNAME_DIR`

Forces the tool to use a specific dir for the installation of a tool.

```text
TEMPO_TOOLNAME_RELEASE_TAG=C:\Tempo\Tools\ToolName
```

---

## Quick Reference

| Variable | Purpose |
|---|---|
| `TEMPO_PERSISTENT_MODS_DIRECTORY` | Persistent mod storage directory |
| `UNREAL_ENGINE_MAJOR_VERSION` | Unreal Engine major version |
| `UNREAL_ENGINE_MINOR_VERSION` | Unreal Engine minor version |
| `TEMPO_UNREAL_ENGINE_MAJOR_VERSION` | Tempo Unreal Engine major version |
| `TEMPO_UNREAL_ENGINE_MINOR_VERSION` | Tempo Unreal Engine minor version |
| `UNREAL_ENGINE_DIRECTORY_MAJOR_MINOR` | Unreal Engine installation directory |
| `TEMPO_UNREAL_ENGINE_DIRECTORY_MAJOR_MINOR` | Tempo Unreal Engine installation directory |
| `TEMPO_DUMP_PATTERNSLEUTH_VERSION` | PatternSleuth version |
| `PATTERNSLEUTH_RES_EngineVersion` | PatternSleuth engine version |
| `TEMPO_REPAK_PACK_VERSION` | repak package version |
| `TEMPO_REPAK_COMPRESSION_TYPE` | repak compression type |
| `GITHUB_TOKEN` | GitHub API authentication |
| `TEMPO_FORCE_ONLINE` | Force online operation |
| `TEMPO_FORCE_OFFLINE` | Force offline operation |
| `TOOLNAME_NO_CACHE` | Disable tool caching |
| `TOOLNAME_CACHE_DIR` | Tool cache directory |
| `TOOLNAME_CACHE_FORCE_ONLINE` | Force cache operations online |
| `TOOLNAME_CACHE_FORCE_OFFLINE` | Force cache operations offline |