function get_shouzhi() {
    ZhejiangIncome = [{
        name: "增值税",
        value: 2239.3
    }, {
        name: "企业所得税",
        value: 964.3
    }, {
        name: "个人所得税",
        value: 442.9
    }, {
        name: "房产税",
        value: 216.9
    }, {
        name: "契税",
        value: 429.2
    }, {
        name: "非税收入",
        value: 899.9
    }];

    ZhejiangOutcome = [{
        name: "公共安全",
        value: 509.7
    }, {
        name: "教育",
        value: 1336.5
    }, {
        name: "科学技术",
        value: 307.6
    }, {
        name: "文化体育与传媒",
        value: 132.6
    }, {
        name: "社会保障和就业",
        value: 813.4
    }, {
        name: "医疗卫生与计划生育",
        value: 552.2
    }, {
        name: "节能环保",
        value: 150.2
    }, {
        name: "城乡社区",
        value: 1010.2
    }, {
        name: "农林水",
        value: 583.7
    }, {
        name: "交通运输",
        value: 354.3
    }, {
        name: "住房保障",
        value: 169.7
    },];

    NingboOutcome = [{
        name: "一般公共服务",
        value: 114.9
    }, {
        name: "公共安全",
        value: 73.8
    }, {
        name: "教育",
        value: 169.1
    }, {
        name: "科学技术",
        value: 63.7
    }, {
        name: "文化体育与传媒",
        value: 23.3
    }, {
        name: "社会保障和就业",
        value: 147.4
    }, {
        name: "医疗卫生与计划生育",
        value: 78.7
    }, {
        name: "节能环保",
        value: 23.1
    }, {
        name: "城乡社区",
        value: 277.7
    }, {
        name: "农林水",
        value: 54.4
    }, {
        name: "交通运输",
        value: 30.9
    }, {
        name: "住房保障",
        value: 32.8
    },];
    NingboIncome = [{
        name: "增值税",
        value: 466.0
    }, {
        name: "企业所得税",
        value: 209.7
    }, {
        name: "个人所得税",
        value: 102.3
    }, {
        name: "非税收入",
        value: 170.7

    }];
    ZhejiangIncomeItem = []
    for(var $i = 0; $i < ZhejiangIncome.length; $i ++) {
        ZhejiangIncomeItem[$i] = ZhejiangIncome[$i].name
    }

    ZhejiangOutcomeItem = []
    for(var $i = 0; $i < ZhejiangOutcome.length; $i ++) {
        ZhejiangOutcomeItem[$i] = ZhejiangOutcome[$i].name
    }
    ZhejiangOutcome.item = ZhejiangOutcomeItem
    
    NingboIncomeItem = []
    for(var $i = 0; $i < NingboIncome.length; $i ++) {
        NingboIncomeItem[$i] = NingboIncome[$i].name
    }
    
    NingboOutcomeItem = []
    for(var $i = 0; $i < ZhejiangIncome.length; $i ++) {
        NingboOutcomeItem[$i] = NingboOutcome[$i].name
    }
    
    return {
        "ZhejiangIncome" : ZhejiangIncome,
        "ZhejiangIncomeItem" : ZhejiangIncomeItem,
        "ZhejiangOutcome": ZhejiangOutcome,
        "ZhejiangOutcomeItem": ZhejiangOutcomeItem,
        "NingboIncome" : NingboIncome,
        "NingboIncomeItem" : NingboIncomeItem,
        "NingboOutcome": NingboOutcome,
        "NingboItem": NingboOutcomeItem,
    }       
}
