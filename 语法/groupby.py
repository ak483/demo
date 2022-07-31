# coding=utf-8
import pandas as pd



if __name__ == '__main__':


    df = pd.DataFrame({
        "class": ["bird", "bird", "mammal", "mammal", "mammal"],
        "order": ["Falconiformes", "Psittaciformes", "Carnivora", "Primates", "Carnivora"],
        "max_speed": [389.0, 24.0, 80.2, 785, 58]
    }, index=["falcon", "parrot", "lion", "monkey", "leopard"])


    print(df)

    print(df.groupby("class").groups)  # 返回字典，key是group label，value是axis labels（index）
    print(df.groupby(["class", "order"]).groups)



