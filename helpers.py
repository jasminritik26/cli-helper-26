from typing import Any, Dict, List, Union


def flatten_dict(
    nested_dict: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary with dotted key paths."""
    items: List[tuple] = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else str(key)
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            for idx, item in enumerate(value):
                list_key = f"{new_key}[{idx}]"
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, list_key, sep=sep).items())
                else:
                    items.append((list_key, item))
        else:
            items.append((new_key, value))
    return dict(items)


def filter_empty_values(
    data: Union[Dict[str, Any], List[Any]]
) -> Union[Dict[str, Any], List[Any]]:
    """Recursively remove None values and empty structures from input data."""
    if isinstance(data, dict):
        cleaned = {}
        for k, v in data.items():
            filtered = filter_empty_values(v) if isinstance(v, (dict, list)) else v
            if filtered is not None and filtered != "" and filtered != [] and filtered != {}:
                cleaned[k] = filtered
        return cleaned
    elif isinstance(data, list):
        cleaned_list = []
        for item in data:
            filtered = filter_empty_values(item) if isinstance(item, (dict, list)) else item
            if filtered is not None and filtered != "" and filtered != [] and filtered != {}:
                cleaned_list.append(filtered)
        return cleaned_list
    return data


def prepare_data_for_display(
    data: Dict[str, Any], max_len: int = 40
) -> Dict[str, str]:
    """Process structured data into a flat key-value mapping for CLI output."""
    flat_data = flatten_dict(data)
    result = {}
    for key, val in flat_data.items():
        str_val = str(val) if val is not None else ""
        if len(str_val) > max_len:
            str_val = str_val[: max_len - 3] + "..."
        result[key] = str_val
    return result
