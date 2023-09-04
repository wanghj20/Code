import numpy as np
import pandas as pd

def get_discription(path):
    fund_inform = pd.read_csv(path, encoding='GBK', index_col=0)
    selected_columns = ['F_INFO_WINDCODE', 'F_INFO_FULLNAME', 'F_INFO_SETUPDATE', 'F_INFO_CORP_FUNDMANAGEMENTCOMP']
    fund_inform = fund_inform[selected_columns]
    fund_inform.columns = ['基金代码', '基金名称', '成立日期', '管理人']
        # ... your other code ...

# Convert to string and remove any trailing ".0"
    fund_inform['成立日期'] = fund_inform['成立日期'].astype(str).str.rstrip('.0')

# Now convert to datetime
    fund_inform['成立日期'] = pd.to_datetime(fund_inform['成立日期'], format='%Y%m%d')

    return fund_inform

if __name__ == '__main__':
    # 导入数据
    path = "/Users/wanghejin/desktop/多因子模型/data/wind_database/ChinaMutualFundDescription.csv"
    # 生成数据
    fund_information = get_discription(path)
    # 保存数据
    fund_information.to_pickle("/Users/wanghejin/desktop/多因子模型/data/fund_nav.csv")
    print("基金基本信息数据生成完毕！")