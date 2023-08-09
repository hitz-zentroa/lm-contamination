import json

def find_na(data):
    return {
        "_".join([inst['dataset'], split]) 
        for inst in data 
        for split in ['train_split', 'dev_split', 'test_split'] 
        if inst[split] == "n/a"
    }

def main():
    with open("data.json", 'rt') as f:
        data = json.load(f)

    na = find_na(data)
    for inst in data:
        for split in ['train_split', 'dev_split', 'test_split']:
            if f"{inst['dataset']}_{split}" in na:
                if inst[split] and inst[split] != "n/a":
                    raise ValueError("Non n/a value found on a n/a split!" + str(inst))
                inst[split] = "n/a"
    
    with open("data.json", 'wt', encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()