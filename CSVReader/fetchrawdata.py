def fetchrawdata(data, str):
    d = []
    for row in data.data:
        d.append(int(row[str]))
    return d


