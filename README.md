
# 简介：
GrouponDeliveryNote程序主要用于协助团长自动整理快团团订单，生成小区内派送单，便于团长或志愿者送货和小区居民收货。另外本程序考虑嘉怡水岸小区的特点，进行专门的优化。

# 运行环境要求：

* 1、支持Linux、windows操作系统。Windows操作系统需高于win7 x64 SP1，如果为win7，需要安装windows的代号为KB2533623的64位版本的补丁，视情安装.netFrameWork。

* 2、python3.8.6 64位以上运行环境，并安装numpy、pandas、python-docx、xlrd等python库。

# 使用方法：
* 1、先确认是否安装完成python，如果未安装可以百度搜索“anaconda安装教程”参考安装 <br>
* 2、下载本程序并复制至某一目录下，打开input.json <br>
参考下面的说明按需进行设置：<br>
```
设置案例一：
{
    "order_file_name": "20220525浮生水果套餐.xlsx"
}

设置案例二

{
    "groupon_owner":"浮生",
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
    "order_file_name": "20220524-浮生蔬菜水果套餐派送单.xlsx",
    "deliverynote_file_name": "20220524-浮生蔬菜水果套餐订单派送单.docx",
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

* 2、进入命令行下，切换程序所在目录下，输入python GrouponDeliveryNote.py运行，即可生成派送单。


# 版本更新：
* 2022.05.26日发布本程序开源版V1.0版： <br>