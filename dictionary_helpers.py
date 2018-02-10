def update_dictionary(defaults, *dicts):
    a = {}
    for k, v in defaults.items():
        a[k] = v

    for d in dicts:
        for k, v in d.items():
            if v is None:
                continue
            if k in a:
                if isinstance(a[k], list):
                    a[k].extend(v)
                else:
                    a[k] = v
    return a

