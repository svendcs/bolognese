def update_dictionary(defaults, *dicts):
    a = {}
    for k, v in defaults.items():
        a[k] = v

    for d in dicts:
        for k, v in d.items():
            if v is None:
                continue
            if k in a:
                a[k] = v
    return a

