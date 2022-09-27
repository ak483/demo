import os
import pandas as pd

#读取所有execl文件并拼接成一个dataframe
def read_excel(path):
    df = pd.DataFrame()
    for file in os.listdir(path):
    	#若对文件名还有其他约束在此处添加，e.g. and file.startswith("升级")
        if file.endswith(".xlsx") :
        	#拼接所有符合要求的excel文件
            df = pd.concat([df, pd.read_excel(path + '\\' + file)],axis=0,ignore_index=True)
    return df


if __name__ == '__main__':

    # path = r"D:\untitled1\demo\mingdongman\日报Excel"
    path = r"D:\untitled1\demo\mingdongman\短视频Excel"
    df = read_excel(path)


    print(df)

    # after_path = r"D:\untitled1\Excel\日报220926.xlsx"
    after_path = r"D:\untitled1\Excel\短视频220926.xlsx"

    c = pd.DataFrame(df)
    c.to_excel(after_path,sheet_name='短视频')