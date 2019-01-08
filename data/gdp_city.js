function get_gdb_city()
{
    Ningbo = {
        "district": ['鄞州区', '慈溪市', '北仑区', '海曙区', '余姚市', '镇海区', '奉化区', '宁海县', '象山县', '江北区'],
        "gdp": [
            { value: 1513.91, name: '鄞州区' },
            { value: 1487.75, name: '慈溪市' },
            { value: 1405.50, name: '北仑区' },
            { value: 1164.50, name: '海曙区' },
            { value: 1023.23, name: '余姚市' },
            { value: 908.70, name: '镇海区' },
            { value: 549.93, name: '奉化区' },
            { value: 542.20, name: '宁海县' },
            { value: 498.91, name: '象山县' },
            { value: 441.40, name: '江北区' },
        ]
    };
    Zhejiang = {
        "district":['杭州', '宁波', '温州', '绍兴', '台州', '嘉兴', '金华', '湖州', '衢州', '丽水', '舟山'],
        "gdp":[
            { value: 12556.2, name: '杭州' },
            { value: 9846.9, name: '宁波' },
            { value: 5453.2, name: '温州' },
            { value: 5108.0, name: '绍兴' },
            { value: 4388.2, name: '台州' },
            { value: 4355.2, name: '嘉兴' },
            { value: 3870.2, name: '金华' },
            { value: 2476.1, name: '湖州' },
            { value: 1380.0, name: '衢州' },
            { value: 1298.2, name: '丽水' },
            { value: 1219.0, name: '舟山' }
        ]
    };
   
    return [Ningbo, Zhejiang]
}