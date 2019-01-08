function get_caizhen() {
    Zhejiang = {
        district: ['杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水',],
        income: [1671.6, 1319.6, 515.2, 488.2, 269.9, 451.3, 366, 117.7, 136.1, 410, 116.2],
        outcome: [-1485.00, -1395.60, -771.6, -488, -342.7, -482.8, -489.1, -299.5, -265, -558.1, -371],
        
    },
    res_zhejaing = []
    for(var $i = 0; $i < Zhejiang.income.length; $i++) {
        res_zhejaing[$i] = (Zhejiang.income[$i] + Zhejiang.outcome[$i]).toFixed(1)   
    }
    Zhejiang.res = res_zhejaing
   
    Ningbo = {
        district: ['海曙区', '江北区', '镇海区', '北仑区', '鄞州区', '奉化区', '余姚市', '慈溪市', '宁海县', '象山县',],
        income: [94.8, 69.4, 71.3, 270.7, 236.7, 44, 95.1, 164.4, 54.9, 36.1],
        outcome: [-75.9, -53, -67.5, -221.2, -169.9, -55.4, -92.9, -151.3, -66.1, -53.6]
    }
    res_ningbo = []
    for(var $i = 0; $i < Ningbo.income.length; $i++) {
        res_ningbo[$i] = (Ningbo.income[$i] + Ningbo.outcome[$i]).toFixed(1)   
    }
    Ningbo.res = res_ningbo
    return [Zhejiang, Ningbo];
}
