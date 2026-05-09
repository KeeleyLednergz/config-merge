import json, os, copy

def deep_merge(base, override):
    result = copy.deepcopy(base)
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = copy.deepcopy(v)
    return result

def load_config(filepath):
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

def merge_configs(*filepaths, env_prefix="CFG_"):
    result = {}
    for fp in filepaths:
        if os.path.isfile(fp):
            result = deep_merge(result, load_config(fp))
    for key, val in os.environ.items():
        if key.startswith(env_prefix):
            parts = key[len(env_prefix):].lower().split("__")
            node = result
            for p in parts[:-1]:
                node = node.setdefault(p, {})
            node[parts[-1]] = val
    return result
