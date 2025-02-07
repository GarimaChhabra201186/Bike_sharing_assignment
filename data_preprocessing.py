print("Preparing data for Exploratory data analysis")

def Binary_mapping(df,mapping_dict):
    for col in df.columns:
        if df[col].dtype == "object" and df[col].nunique()==2:
            df[col] = df[col].map(mapping_dict)
mapping_dict = {"yes":1,"no":0}

df = pd.get_dummies(df, drop_first=True, dtype="int")
