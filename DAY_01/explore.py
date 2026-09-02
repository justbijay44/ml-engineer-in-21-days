import csv
import operator

def is_numerical_col(values: str) -> bool:
    try:
        float(values[0])
        return True
    
    except Exception:
        return False 

def word_frequency(values: str):
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1

    unique_values = list(freq)
    most_freq = max(freq.items(), key=lambda x: x[1])

    return len(unique_values), most_freq

def load_data(path: str):
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)

        rows = list(reader)
        fields = reader.fieldnames

    return rows, fields

def describe(rows, fields):
    cols = {}
    for field in fields:
        cols[field] = [row[field] for row in rows if row[field]]

    describe_data = []
    for field in cols:
        if is_numerical_col(cols[field]):
            cols[field] = [float(data) for data in cols[field]]
            describe_data.append(f"{field}: Max: {max(cols[field])} | Min: {min(cols[field])} | Mean: {(sum(cols[field]) / len(cols[field])):.2f}")

        else:
            unique, most_freq = word_frequency(cols[field])
            describe_data.append(f"{field}: Unique: {unique} | Most frequent with count: {most_freq[0]}({most_freq[1]})")
    return '\n'.join(describe_data)

def filter_rows(rows, field, op, value):
    ops = {
        ">": operator.gt,
        "<": operator.lt,
        "==": operator.eq,
    }

    filtered_rows = []
    for row in rows:
        if row[field]:
            try:
                val = float(row[field])
                if ops[op](val, value):
                    filtered_rows.append(row)
            except ValueError:
                if ops[op](row[field], value):
                    filtered_rows.append(row)

    return filtered_rows

if __name__ == "__main__":
    rows, fields = load_data("data/titanic.csv")

    results = filter_rows(rows, "Age", ">", 30)
    print(f"Filtered Results: {len(results)} of {len(rows)}\n")
    for result in results:
        print(f"{result['Name']}(Age: {result['Age']})")