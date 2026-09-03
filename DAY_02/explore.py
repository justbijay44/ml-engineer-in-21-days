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
    try:
        value = float(value)
    except:
        pass

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

def sort_rows(rows, field, reverse=False):
    rows = [row for row in rows if row[field]]

    after_sort = sorted(
        rows, 
        key=lambda x: float(x[field]) 
                    if is_numerical_col(x[field]) else x[field], 
        reverse=reverse
        )
    return after_sort

def bar_chart(rows, group_field, value_field):
    group_freq = {}

    for row in rows:
        group_freq[row[group_field]] = group_freq.get(row[group_field], 0) + 1

    group = list(group_freq)

    survived_by_group = {}
    for g in group:
        survived_by_group[g] = sum(1 for row in rows if row[group_field] == g and row[value_field] == "1")

    survived_by_group = sorted(survived_by_group.items(), key=lambda x: x[1], reverse=True)

    return '\n'.join(
        f"Pclass: {f'{key} ({val})':<7} {(val // 5) * '#'} " 
        for key, val in survived_by_group
        )

if __name__ == "__main__":
    rows, fields = load_data("data/titanic.csv")

    # results = filter_rows(rows, "Age", ">", 30)
    # print(f"Filtered Results: {len(results)} of {len(rows)}\n")
    # for result in results:
    #     print(f"{result['Name']}(Age: {result['Age']})")

    # print(sort_rows(rows, "Age"))
    # print(sort_rows(rows, "Sex"))

    # print(bar_chart(rows, "Pclass", "Survived"))

    import sys
    function_names = {
        "filter": filter_rows, 
        "sort": sort_rows, 
        "describe": describe, 
        "bar_chart": bar_chart
    }
    func_name = function_names[sys.argv[1]]
    args = sys.argv[2:]

    print(func_name(rows, *args))