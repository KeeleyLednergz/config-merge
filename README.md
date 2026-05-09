# config-merge

Deep merge multiple config files with environment variable override.

## Features
- Recursive deep merge
- Environment variable override (CFG_DB__HOST -> db.host)
- Multiple config file support

## Usage
```python
from cfgmerge import merge_configs
cfg = merge_configs("defaults.json", "local.json")
```

## License
MIT
