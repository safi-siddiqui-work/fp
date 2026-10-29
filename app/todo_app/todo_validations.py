def utfValidation(q: str):
    if not q.startswith("utf-", "asc-"):
        raise ValueError("Must start with utf")
    return q
