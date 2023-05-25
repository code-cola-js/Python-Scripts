import pandas as pd
import numpy as np

#全年每月数据存放在单独的excel表中
for i in np.arange(1,13):
    data4 = pd.DataFrame()

    a = "{}月销售业绩".format(i)
    b = a + '.xlsx'
    writer = pd.ExcelWriter(b, engine='xlsxwriter')
    data4.to_excel(writer, 'Sheet1',index=0)
    writer.save()
