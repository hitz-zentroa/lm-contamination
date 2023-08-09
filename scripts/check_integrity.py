import json


def fix_na(data):
    def find_na(data):
        return {
            "_".join([inst['dataset'], split]) 
            for inst in data 
            for split in ['train_split', 'dev_split', 'test_split'] 
            if inst[split] == "n/a"
        }
    
    na = find_na(data)
    for inst in data:
        for split in ['train_split', 'dev_split', 'test_split']:
            if f"{inst['dataset']}_{split}" in na:
                if inst[split] and inst[split] != "n/a":
                    raise ValueError("Non n/a value found on a n/a split!" + str(inst))
                inst[split] = "n/a"
    
    return data

def fix_percentage_precision(data):
    for inst in data:
        for split in ['train_percent', 'dev_percent', 'test_percent']:
            if inst[split]:
                inst[split] = float(f"{inst[split]:.1f}")
    return data

def main():
    with open("data.json", 'rt') as f:
        data = json.load(f)

    # Fix missing n/a values
    data = fix_na(data)
    # Fix percentage precision
    data = fix_percentage_precision(data)

    
    with open("data.json", 'wt', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()