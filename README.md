
# 简介：
GrouponDeliveryNote程序由小涛开发，主要用于协助团长自动整理快团团订单，生成小区内派送单，便于团长或志愿者送货和小区居民收货。另外本程序考虑嘉怡水岸小区的特点，进行专门的优化。

# 运行环境要求：

* 1、支持Linux、windows操作系统。Windows操作系统需高于win7 x64 SP1，如果为win7，需要安装windows的代号为KB2533623的64位版本的补丁，视情安装.netFrameWork。

* 2、python3.8.6 64位以上运行环境，并安装numpy、pandas、python-docx、xlrd等python库。

# 使用方法：
* 1、先确认是否安装完成python，如果未安装可以百度搜索“[anaconda安装教程](https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=anaconda%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B&oq=anaconda%25E5%25AE%2589%25E8%25A3%2585%25E6%2595%2599%25E7%25A8%258B&rsv_pq=b6fc5a4a00004c74&rsv_t=1c5eYwmNwWfA31oioXkUGy0JlHMABF17liscw9H9eeNNOJsbl2DgBE9uv4k&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t)”参考安装 <br>
* 2、下载[本程序](https://github.com/mtshang1984/GrouponDeliveryNote/releases)并复制至某一目录下，打开input.json <br>
参考下面的说明按需进行设置：<br>
```
设置案例一：
{
    "order_file_name": "20220525浮生水果套餐.xlsx"
}

设置案例二

{
    "groupon_owner":"浮生若梦",
    "product_name": [
        [
            "本地叶菜4品种6斤装(6斤)",
            "1-本地叶菜4品种6斤装(6斤)"
        ],
        [
            "青浦练塘茭白(5斤装)",
            "2-青浦练塘茭白(5斤装)"
        ],
        [
            "水果黄瓜（旱黄瓜）(5斤装)",
            "3-水果黄瓜（旱黄瓜）(5斤装)"
        ]
    ],
    "order_file_name": "20220525-浮生若梦蔬菜水果套餐派送单.xlsx",
    "deliverynote_file_name": "20220525-浮生若梦蔬菜水果套餐订单派送单.docx",
    "excel_column_name": {
        "product_name": "商品",
        "wechat_name": "下单人",
        "custom_name": "收货人",
        "phone_number": "联系电话",
        "building_number": "楼号（如10）",
        "room_number": "房号（如606）",
        "quantity": "数量",
        "remarks": "团长备注"
    },
    "max_row_number_per_page": 43,
    "page_margin_cm": {
        "top_margin": 1,
        "bottom_margin": 1,
        "left_margin": 5,
        "right_margin": 1
    },
    "if_hide_phone_number": true
}

```
* 其中  
    * groupon_owner：团长昵称或姓名
    * product_name：快团团订单中商品名称与派送单中商品名称的对应关系
    * order_file_name：订单文件名
    * deliverynote_file_name：派送单文件名
    * excel_column_name：订单excel中各项表题名称
    * max_row_number_per_page：每一页所包含的最大行数
    * page_margin_cm：页边距
    * if_hide_phone_number：是否隐藏手机号码
<br>

* 3、进入命令行下，切换程序所在目录下，输入python GrouponDeliveryNote.py运行，即可生成派送单。
    * 派送单样式参见“[20220525浮生若梦水果套餐派送单.docx]( https://github.com/mtshang1984/GrouponDeliveryNote/blob/main/20220525%E6%B5%AE%E7%94%9F%E8%8B%A5%E6%A2%A6%E6%B0%B4%E6%9E%9C%E5%A5%97%E9%A4%90%E6%B4%BE%E9%80%81%E5%8D%95.docx )”。文件分为两部分，第一部分为订单确认单，先按不同楼栋再按产品排。第二部分为派送单，先按品种再按楼栋排序。楼栋的单据之间增加分隔线以方便裁剪。


# 版本更新：
* 2022.05.26日发布本程序开源版V1.0版： <br>

# 协议声明
使用本程序代码需遵循Apache License 2.0协议
