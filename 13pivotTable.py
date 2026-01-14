'''
透视表格: 把扁平的原始表格，按「行维度」和「列维度」重新分组，对指定数值列做统计计算（求和、均值、计数等），让数据从「零散记录」变成「结构化汇总表」，方便快速发现数据间的关联规律。
'''
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return pd.pivot_table(weather, values='temperature', index='month', columns='city')