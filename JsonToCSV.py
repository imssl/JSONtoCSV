import pandas as pd, sys
with open(sys.argv[1], encoding='utf-8-sig') as f_input:
    df = pd.read_json(f_input,lines=True)
df.to_csv('output.csv', encoding='utf-8-sig', index=False)