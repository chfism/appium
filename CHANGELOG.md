# CHANGES IN 2017-12-13
- [FIX] adb_tap 关键字多机并行报错
- [EDIT] 优化page层代码
- [ADD] 测试通过后本地记录日志，截图功能已经关闭，可以自行打开


# CHANGES IN 2017-12-12
- [FIX] 升级为1.7.1版本后，多设备android并行报错，加上systemport,关于ios多设备并行未适配，更多资料参考[parallel_tests](https://appium.readthedocs.io/en/stable/en/appium-setup/parallel_tests/)
- [ADD] 每个设备的用例成功和失败统计 


# CHANGES IN 2017-12-08
- [FIX] 捕捉appium.common.exceptions.NoSuchContextException切换webview异常
- [FIX] 捕捉appium selenium.common.exceptions.WebDriverException
- [ADD] 测试报告对每个手机对用例运行情况
 
# CHANGES IN 2017-12-04
- [FIX]  page函数检查点冲突

# CHANGES IN 2017-11-30
- [ADD] 适配IOS自动化，IOS的关键字驱动还没有进行详细测试，待优化
- [FIX] windows下，安卓adb不稳定，出现报错

# CHANGES IN 2017-11-24
- [ADD] 适配windows平台


# CHANGES IN 2017-11-21
- [ADD] 异常监控日志扩展传递 

# CHANGES IN 2017-11-20
- [FIX] 重连机制下的测试报告显示日志不正常 

# CHANGES IN 2017-11-17
- [FIX] get_content_desc 得到值后，检查点不对比

# CHANGES IN 2017-11-16
- [ADD] 每个用例默认支持失败重跑，可关闭此配置
- [ADD] 新增失败重连的日志记录

# CHANGES IN 2017-11-15
- [ADD]  关键字contentDescription
- [EDIT] BaseOperate.operate函数，去掉大量if,改用dict lambda的方式模拟switch case
- [ADD]  用例操作步的骤统一使用operate_type关键字
- [ADD]  webview切换不成功判定为失败
- [EDIT] 修改主文档
- [ADD] 新增测试用例关键字说明文档
- [ADD] 新增使用说明文档 


# CHANGES IN 2017-11-10
- 优化UnitTest
    - [ADD] 从之前的setUp,tearDown,改成了setUpClass,tearDownClass
    - [ADD] 为了配合setUpClass用例关联问题，加入了driver.launch_app配置

# CHANGES IN 2017-10-28
- 优化PageObject
    - [ADD] 检查点关键字contrary：相反检查点，传1表示如果检查元素存在就说明失败，如删除后，此元素依然存在
    - [ADD] 检查点关键字toast: 表示提示框检查点
    - [ADD] 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
    - [ADD] 检查点关键字check: 自定义检查结果
    - [ADD] 检查点关键字excepts: 如果为1，表示操作出现异常情况检查点为成功。如：删除成功了，此数据不存在则为真

# CHANGES IN 2017-9-25
-  [FIX] adb install安装和卸载uiautomator2的server和debug安装包，解决直接用uiautomator2连接服务器超时

# CHANGES IN 2017-9-20
-  [ADD] 单独封装了Page的方法，给其他用例的Page调用 

# CHANGES 
 整个框架的封装完成
-  [ADD]  Base层管理常用方法
-  [ADD]  PageObject层管处理页面逻辑
-  [TestCase] 测试用例调用，调用Page层，传入yaml用例
-  [yaml] 测试用例编写层，基于关键字驱动，主要包含
    - testinfo. 用例介绍
    - testcase. 用例操作步骤，用例操作步骤
    - check. 检查点
-  [Runner] 入口
-  [Log] 记录每台设备多运行日志，含截图
- [Report] 自动生成excel测试报告
