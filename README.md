
# 简介：
GrouponDeliveryNote程序由小涛开发，主要用于协助团长自动整理快团团订单，生成小区内派送单，便于团长或志愿者送货和小区居民收货。另外本程序考虑嘉怡水岸小区的特点，进行了专门的优化。

# 运行环境要求：

* 支持Linux、windows操作系统。Windows操作系统需高于win7 x64 SP1，如果为win7，需要安装windows的代号为KB2533623的64位版本的补丁，视情安装.netFrameWork。Linux系统可直接运行python源码。


# Windows下使用方法：

* 1、到[本程序Release栏目](https://github.com/mtshang1984/GrouponDeliveryNote/releases)下找到最新版本进行下载，下载后解压至某一目录下，找到GrouponDeliveryNote.exe文件，双击开始运行 <br>

* 2、将快团团订单文件拖拽至对话框界面，按需选择“输出时隐藏手机号”、“排序方式”和“表题顺序”等选项后，单击“开始转换”按钮，即可生成派送单。
    * 派送单样式有六种类型，包括（具体可下载程序源码查看输出样例）：
      * 按商品-楼号-房号排序（楼栋的单据之间增加分隔线以方便裁剪），
      * 按楼号-商品-房号排序，
      * 按楼号-房号-商品排序，
      * 每件商品一个标签，
      * 每户一个标签
      * 每件商品一个标签（适用于标签机直接打印）
     

# 用户界面
<img src="https://user-images.githubusercontent.com/12483423/182912605-4424a8e9-be97-4cda-b275-1f5fc4de4bb5.png" width="700">

                                                                                                                           
# 派送单样式
   * 纸条式
  
<img src="https://user-images.githubusercontent.com/12483423/171041233-6c6ef2c2-0968-4147-9ebe-f119e9cc469e.png" width="800">
   * 标签式
   
<img src="https://user-images.githubusercontent.com/12483423/171044584-9bceec1e-2ee8-4902-9e55-a05d17ed4e8d.png" width="800">

   * 适用标签机的标签
   <img src="https://user-images.githubusercontent.com/12483423/182912789-a7dffa7e-77ae-4a44-8c64-b410900a40e6.png" width="800">


# 赞助说明
GrouponDeliveryNote软件使用完全免费。如果您觉得软件好用，欢迎您赞助作者，以便作者有足够的资源用于软件的后续维护和升级。

<img src="https://user-images.githubusercontent.com/12483423/171045523-f934eedf-cd49-41d6-843a-abe44d08be8d.jpg" width="300">    <img src="https://user-images.githubusercontent.com/12483423/171045535-42920654-4186-4e31-814f-30393d127ed6.jpg" width="300">


# 版本更新：
* 2022.08.05日发布本程序开源版V1.2.2版： <br>
    * 增加了适用于标签机的的标签生成功能；
    * 界面修改为可拉伸设计，适用于不同分辨率的电脑。
* 2022.06.01日发布本程序开源版V1.2.1版： <br>
    * 增加了每户标签打印功能，改善了对快团团原订单的解析稳定性。
* 2022.05.31日发布本程序开源版V1.2版： <br>
    * 增加了商品标签打印功能，优化了启动界面，增加了对快团团普通团购订单的支持。改善了对快团团原订单的解析稳定性
* 2022.05.29日发布本程序开源版V1.1版： <br>
    * 增加了图形界面使用方式，并改善了对快团团原订单的解析稳定性
* 2022.05.26日发布本程序开源版V1.0版： <br>

# 协议声明
使用本程序代码需遵循Apache License 2.0协议
