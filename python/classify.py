import sys
import getopt
import pickle
import pandas as pd
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码

# 第1题
def line_chart_1(kind):
    if kind == 'pub':
        fr = open('data_Publicity_num.pkl', 'rb')
        kind = 'Publicity'
    else:
        fr = open('data_Apply_num.pkl', 'rb')
        kind = 'Apply'
    data = pickle.load(fr)
    fr.close()
    data.plot(figsize=(16, 12), title='专利' + kind + '数量折线图')
    plt.show()

# 第3题
def pie_plot(com, y_from='1980', y_to='2017', cls=''):
    fr = open('data_for_radio.pkl', 'rb')
    data = pickle.load(fr)
    fr.close()
    fr = open('index_company.pkl', 'rb')
    indx = pickle.load(fr)
    fr.close()

    target = com
    loc = pd.Series([False] * data.shape[0])
    for col in indx.columns:
        loc = loc | (indx[col] == target)
    content = data[loc]

    year_from = y_from
    year_to = y_to
    target_start = cls
    content = content[(content[7] >= year_from) & (content[7] <= year_to)]
    content_1 = content[4].str.split(';', expand=True)
    loc = pd.Series([False] * content.shape[0], index=content.index)
    for col in content_1.columns:
        loc = loc | (content_1[col].str.startswith(target_start))

    fig = plt.figure(figsize=(16, 12))  # 调节图形大小
    ax = fig.add_subplot(111)
    # labels = [u'发明',u'实用',u'外观'] #定义标签
    labels = []
    sizes = []
    for i in range(1, 4):
        tmp = content[loc][1][content[loc][1] == i].count()
        sizes.append(tmp)
        labels.append(str(tmp))
    colors = ['red', 'yellowgreen', 'lightskyblue']  # 每块颜色定义
    explode = (0, 0.1, 0)  # 将某一块分割出来，值越大分割出的间隙越大
    ax.set_title(target + ' ' + year_from + '~' + year_to +
                 ' ' + target_start, fontsize=22)  # 图表标题
    patches, text1, text2 = ax.pie(sizes,
                                   explode=explode,
                                   labels=labels,
                                   labeldistance=1.06,  # 图例距圆心半径倍距离
                                   colors=colors,
                                   autopct='%3.2f%%',  # 数值保留固定小数位
                                   shadow=False,  # 无阴影设置
                                   startangle=90,  # 逆时针起始角度设置
                                   pctdistance=0.6)  # 数值距圆心半径倍数距离
    ax.legend(patches, ['发明', '实用', '外观'], loc='best')
    # patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部的文本
    # x，y轴刻度设置一致，保证饼图为圆形
    ax.axis('equal')
    plt.show()

# 第5题
def line_chart_2(com, y_from=1980, y_to=2017):
    fr = open('ratio_for_inventor.pkl', 'rb')
    data = pickle.load(fr)
    fr.close()
    fr = open('index_company.pkl', 'rb')
    indx = pickle.load(fr)
    fr.close()

    target = com
    loc = pd.Series([False] * data.shape[0])
    for col in indx.columns:
        loc = loc | (indx[col] == target)
    content = data[loc]

    year_from = y_from
    year_to = y_to
    content = content[(content[7] >= year_from) & (content[7] <= year_to)]
    num_inv = pd.DataFrame(columns=['year', '发明人数'])
    time = set(content[7])

    for year in time:
        content_1 = content[content[7] == year][
            6].str.split(';', expand=True).values.flatten()
        tmp = set(content_1)
        tmp.discard(None)
        tmp1 = {'year': year}
        tmp1['发明人数'] = tmp.__len__()
        num_inv = num_inv.append(tmp1, ignore_index=True)

    num_inv.index = pd.DatetimeIndex(num_inv['year']).to_period('y')
    num_inv.drop('year', axis=1, inplace=True)

    num_inv = num_inv.sort_index(axis=0)
    num_inv.plot(figsize=(16, 12), title=target + ' ' + year_from + '~' + year_to)
    plt.show()

# 第4题
def bar_chart(com, y_from='1980', y_to='2017', kind='1'):
    fr = open('data_for_radio.pkl', 'rb')
    data = pickle.load(fr)
    fr.close()
    fr = open('index_company.pkl', 'rb')
    indx = pickle.load(fr)
    fr.close()

    target = com
    loc = pd.Series([False] * data.shape[0])
    for col in indx.columns:
        loc = loc | (indx[col] == target)
    content = data[loc]
    year_from = y_from
    year_to = y_to
    kind_show = kind
    content = content[(content[7] >= year_from) & (content[7] <= year_to)]

    content_1 = content[4].str.split(
        ';', expand=True).join(content[1], rsuffix='_cla')

    content_1.loc[:, [0, '1_cla']]
    class_code = pd.DataFrame(columns=['code', 'class'])
    for i in range(content_1.shape[1] - 1):
        tmp = content_1.loc[:, [i, '1_cla']].dropna()
        tmp.columns = ['code', 'class']
        class_code = class_code.append(tmp, ignore_index=True)

    class_code = class_code[class_code[
        'code'].str.match('^[A-Za-z0-9]')]  # 去除不规则的行
    class_code['code'] = class_code['code'].str.split('(', expand=True)
    if kind_show == '1':  # 大组
        class_code['code'] = class_code['code'].str.split('/', expand=True)
    uni_code = class_code['code'].unique()
    result = pd.DataFrame(columns=[1, 2, 'class', 3])
    for i in range(uni_code.shape[0]):
        tmp = class_code[class_code['code'] == uni_code[i]]
        tmp = tmp['class'].value_counts()
        tmp['class'] = uni_code[i]
        result = result.append(tmp, ignore_index=True)
    result = result.iloc[:, :min(3, result.shape[1])]
    result = result.fillna(0)

    result = result.set_index('class')
    result.columns = ['发明', '实用']
    tmp = u'小组'
    if kind_show == '1':
        tmp = u'大组'
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码
    result.plot.barh(figsize=(16, 12), stacked=True, title=target + ' ' +
                     year_from + '~' + year_to + ' ' + tmp)
    plt.show()

# 第6题
def bar_chart_1(com, y_from='1980', y_to='2017', cls=''):
    fr = open('data_for_radio.pkl', 'rb')
    data = pickle.load(fr)
    fr.close()
    fr = open('index_company.pkl', 'rb')
    indx = pickle.load(fr)
    fr.close()

    target = com
    loc = pd.Series([False] * data.shape[0])
    for col in indx.columns:
        loc = loc | (indx[col] == target)
    content = data[loc]

    year_from = y_from
    year_to = y_to
    target_start = cls
    content = content[(content[7] >= year_from) & (content[7] <= year_to)]
    content_1 = content[4].str.split(';', expand=True)
    loc = pd.Series([False] * content.shape[0], index=content.index)
    f = pd.Series([False] * content.shape[0], index=content.index)
    res_cla = pd.Series(index=content.index)
    for col in content_1.columns:  # 识别类型开头
        temp = content_1[col].str.startswith(target_start)
        loc = loc | temp
        temp = temp | f
        res_cla[temp] = content_1[temp][col]
    res_cla = res_cla.str.split('(', expand=True)[0]

    cols = res_cla[res_cla.notnull()].unique()
    result_count = pd.DataFrame()
    for i in range(cols.shape[0]):
        tmp = content[res_cla == cols[i]][1].value_counts()[:2]
        tmp.name = cols[i]
        result_count = result_count.append(tmp)
    result_count = result_count.fillna(0)
    result_count.columns = [u'发明', u'实用']

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文乱码
    result_count.plot.barh(figsize=(16, 12), stacked=True, title=target +
                           ' ' + year_from + '~' + year_to + ' ' + target_start)
    plt.show()


def help():
    print("Maybe you need some help!")
    print(
        "-w or --whichexam= :the examination to display. Choose in [one,two,thr,fou,fiv,six]\n-c or --company= :the company to display.\n-s or --start= :choose the year to start with\n-e or --end= :the year to end with\n-k or --kind= :the kind to display\n-h or --help")
    sys.exit()
# if __name__ == '__main__':
opts, args = getopt.getopt(sys.argv[1:], 'w:c:s:e:k:h', [
                           "whichexam=", "company=", "start=", "end=", "kind=", "help"])
which_exam = ''
company = '浙江大学'
start_year = '1980'
end_year = '2017'
kind_output = ''

for opt, value in opts:
    if opt in("-w", "--whichexam"):
        which_exam = value
        # 如果有传参，则重新赋值。
    elif opt in("-c", "--company"):
        company = value
    elif opt in("-s", "--start"):
        start_year = value
    elif opt in("-e", "--end"):
        end_year = value
    elif opt in("-k", "--kind"):
        kind_output = value
    elif opt in("-h", "--help"):
        help()
    else:
        help()

if which_exam == '':
    print('Wrong Input. Please try again with help.')
else:
    if which_exam == 'one':
        print('Figure the first examination out!')
        line_chart_1('app')
    elif which_exam == 'two':
        print('Figure the second examination out!')
        line_chart_1('pub')
    elif which_exam == 'thr':
        print('Figure the third examination out!\nPlease waiting for 15 seconds...')
        pie_plot(company, start_year, end_year, kind_output)
    elif which_exam == 'fou':
        print('Figure the forth examination out!\nPlease waiting for 15 seconds...')
        bar_chart(company, start_year, end_year, kind_output)
    elif which_exam == 'fiv':
        print('Figure the fifth examination out!\nPlease waiting for 15 seconds...')
        line_chart_2(company, start_year, end_year)
    elif which_exam == 'six':
        print('Figure the extra examination out!\nPlease waiting for 15 seconds...')
        bar_chart_1(company, start_year, end_year, kind_output)


# print(arguments[1])
# if len(arguments) < 2:
#     print("python3 classify.py -one\npython3 classify.py -three 浙江大学 1990 1999 H\npython3 classify.py -four 浙江大学 1990 1999 1\npython3 classify.py -five 浙江大学 1990 1999\npython3 classify.py -six 浙江大学 1990 1999 H")
# else:
#     if arguments[1] == '-one':
#         print('figure line chart 1 out!\nPlease waiting for 15 seconds...')
#         line_chart_1()
#     elif arguments[1] == '-three':
#         print('figure pie plot out!\nPlease waiting for 15 seconds...')
#         if arguments.__len__() == 3:
#             pie_plot(arguments[2])
#         elif arguments.__len__() == 4:
#             pie_plot(arguments[2], arguments[3])
#         elif arguments.__len__() == 5:
#             pie_plot(arguments[2], arguments[3], arguments[4])
#         elif arguments.__len__() == 6:
#             pie_plot(arguments[2], arguments[3], arguments[4], arguments[5])
#     elif arguments[1] == '-four':
#         print('figure bar chart 1 out!\nPlease waiting for 15 seconds...')
#         bar_chart(arguments[2], arguments[3], arguments[4], arguments[5])
#     elif arguments[1] == '-five':
#         print('figure line chart 2 out!\nPlease waiting for 15 seconds...')
#         line_chart_2(arguments[2], arguments[3], arguments[4])
#     else:
#         print('figure bar chart 2 out!\nPlease waiting for 15 seconds...')
#         bar_chart_1(arguments[2], arguments[3], arguments[4], arguments[5])
#     print('plot successfully!')


# print ('参数个数为:', len(sys.argv), '个参数。')
# print ('参数列表:', str(sys.argv))
