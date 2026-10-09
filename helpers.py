from typing import Dict, Any

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    '''
    Recursively flattens a nested dictionary.

    Useful for preparing hierarchical data for tabular display or
    CSV export in command-line interfaces.
    '''
    items = []
    for k, v in d.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                list_key = f'{new_key}{sep}{i}'
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, list_key, sep=sep).items())
                else:
                    items.append((list_key, item))
        else:
            items.append((new_key, v))
    return dict(items)

def clean_dict_values(d: Dict[str, Any], remove_none: bool = True) -> Dict[str, Any]:
    '''
    Cleans dictionary values by removing None values and stripping
    whitespace from string values.
    '''
    cleaned = {}
    for k, v in d.items():
        if remove_none and v is None:
            continue
        if isinstance(v, str):
            cleaned[k] = v.strip()
        elif isinstance(v, dict):
            cleaned[k] = clean_dict_values(v, remove_none)
        else:
            cleaned[k] = v
    return cleaned