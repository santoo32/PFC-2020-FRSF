import pandas as pd
import numpy as np

# Simple moving average python implementation
# Input object should have the following structure
product = {
    'time' : [],
    'confidence':[]
}

dictIndex = 0


# Turns object into a data table
# df = pd.DataFrame(product)
# Prints the table 
# print(df)
# Prints the first n lines of the table
# print(df.head(2))


# SMA of 3
# for i in range(0,df.shape[0]-2):
#     df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)

# print(df)


def calculate_sma(score):
    global dictIndex
    
    product['time'].append(dictIndex)
    product['confidence'].append(score)
    
    dictIndex = dictIndex + 1
    
    df = pd.DataFrame(product)

    for i in range(0,df.shape[0]-9):
        df.loc[df.index[i+9],'SMA_10'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+df.iloc[i+4,1]+df.iloc[i+5,1]+df.iloc[i+6,1]+df.iloc[i+7,1]+df.iloc[i+8,1]+df.iloc[i+9,1])/10),1)

    # Prints the table 
    print(df)
    if 'SMA_10' in df.keys():
        return df["SMA_10"].iloc[-1]
    else:
        return 0


    

def clear_sma():
    global dictIndex
    global product

    product.clear()
    product = {
    'time' : [],
    'confidence':[]
    }
    dictIndex = 0
