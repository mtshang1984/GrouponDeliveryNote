
# 简介：
GrouponDeliveryNote程序由小涛开发，主要用于协助团长自动整理快团团订单，生成小区内派送单，便于团长或志愿者送货和小区居民收货。另外本程序考虑嘉怡水岸小区的特点，进行专门的优化。

# 运行环境要求：

* 支持Linux、windows操作系统。Windows操作系统需高于win7 x64 SP1，如果为win7，需要安装windows的代号为KB2533623的64位版本的补丁，视情安装.netFrameWork。Linux系统可直接运行python源码。


# Windows下使用方法：

* 1、下载[本程序](https://github.com/mtshang1984/GrouponDeliveryNote/releases)最新版本，并解压至某一目录下，GrouponDeliveryNote.exe开始运行 <br>

* 2、将快团团订单文件拖拽至对话框界面，按需选择“输出时隐藏手机号”、“排序方式”和“表题顺序”等选项后，单击“开始转换”按钮，即可生成派送单。
    * 派送单样式有四种类型，分别参见
      * 按商品-楼号-房号排序：见“[20220525浮生若梦水果套餐派送单（含手机号）（按商品-楼号-房号排序）.docx](https://github.com/mtshang1984/GrouponDeliveryNote/blob/main/20220525%E6%B5%AE%E7%94%9F%E8%8B%A5%E6%A2%A6%E6%B0%B4%E6%9E%9C%E5%A5%97%E9%A4%90%E6%B4%BE%E9%80%81%E5%8D%95%EF%BC%88%E5%90%AB%E6%89%8B%E6%9C%BA%E5%8F%B7%EF%BC%89%EF%BC%88%E6%8C%89%E5%95%86%E5%93%81-%E6%A5%BC%E5%8F%B7-%E6%88%BF%E5%8F%B7%E6%8E%92%E5%BA%8F%EF%BC%89.docx?raw=true)”。楼栋的单据之间增加分隔线以方便裁剪。
      * 按楼号-商品-房号排序：见“[20220525浮生若梦水果套餐派送单（含手机号）（按楼号-商品-房号排序）.docx](https://github.com/mtshang1984/GrouponDeliveryNote/blob/main/20220525%E6%B5%AE%E7%94%9F%E8%8B%A5%E6%A2%A6%E6%B0%B4%E6%9E%9C%E5%A5%97%E9%A4%90%E6%B4%BE%E9%80%81%E5%8D%95%EF%BC%88%E5%90%AB%E6%89%8B%E6%9C%BA%E5%8F%B7%EF%BC%89%EF%BC%88%E6%8C%89%E6%A5%BC%E5%8F%B7-%E5%95%86%E5%93%81-%E6%88%BF%E5%8F%B7%E6%8E%92%E5%BA%8F%EF%BC%89.docx?raw=true)”。
      * 按楼号-房号-商品排序：见“[20220525浮生若梦水果套餐派送单（含手机号）（按楼号-房号-商品排序）.docx](https://github.com/mtshang1984/GrouponDeliveryNote/blob/main/20220525%E6%B5%AE%E7%94%9F%E8%8B%A5%E6%A2%A6%E6%B0%B4%E6%9E%9C%E5%A5%97%E9%A4%90%E6%B4%BE%E9%80%81%E5%8D%95%EF%BC%88%E5%90%AB%E6%89%8B%E6%9C%BA%E5%8F%B7%EF%BC%89%EF%BC%88%E6%8C%89%E6%A5%BC%E5%8F%B7-%E6%88%BF%E5%8F%B7-%E5%95%86%E5%93%81%E6%8E%92%E5%BA%8F%EF%BC%89.docx?raw=true)”。
      * 按每户每件商品一个标签：见“[20220525浮生若梦水果套餐派送单（含手机号）（打印标签）.docx](https://github.com/mtshang1984/GrouponDeliveryNote/blob/main/20220525%E6%B5%AE%E7%94%9F%E8%8B%A5%E6%A2%A6%E6%B0%B4%E6%9E%9C%E5%A5%97%E9%A4%90%E6%B4%BE%E9%80%81%E5%8D%95%EF%BC%88%E5%90%AB%E6%89%8B%E6%9C%BA%E5%8F%B7%EF%BC%89%EF%BC%88%E6%89%93%E5%8D%B0%E6%A0%87%E7%AD%BE%EF%BC%89.docx?raw=true)”。

     

# 用户界面
![image](https://user-images.githubusercontent.com/12483423/171040934-51af0a7b-69dd-438e-ba1b-2501501ee7c8.png)
# 派送单样式
   * 纸条式
  
<img src="https://user-images.githubusercontent.com/12483423/171041233-6c6ef2c2-0968-4147-9ebe-f119e9cc469e.png" width="500">
   * 标签式
   
<img src="https://user-images.githubusercontent.com/12483423/171044584-9bceec1e-2ee8-4902-9e55-a05d17ed4e8d.png" width="500">

# 赞助说明
GrouponDeliveryNote软件使用完全免费。如果您觉得软件好用，欢迎您赞助作者以用于后续维护和升级费用。

<img src="https://user-images.githubusercontent.com/12483423/171045523-f934eedf-cd49-41d6-843a-abe44d08be8d.jpg" width="300">    <img src="https://user-images.githubusercontent.com/12483423/171045535-42920654-4186-4e31-814f-30393d127ed6.jpg" width="300">


# 版本更新：
* 2022.05.31日发布本程序开源版V1.2版： <br>
    * 增加了商品标签打印功能，优化了启动界面，增加了对快团团普通团购订单的支持。改善了对快团团原订单的解析稳定性
* 2022.05.29日发布本程序开源版V1.1版： <br>
    * 增加了图形界面使用方式，并改善了对快团团原订单的解析稳定性
* 2022.05.26日发布本程序开源版V1.0版： <br>

# 协议声明
使用本程序代码需遵循Apache License 2.0协议
