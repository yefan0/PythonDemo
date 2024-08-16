# 微信自动发消息，仅适用于PC版微信3.9.11.17  (下载地址：https://dldir1.qq.com/weixin/Windows/WeChatSetup.exe)
# 微信全版本地址(https://github.com/tom-snow/wechat-windows-versions/releases)
# 具体的使用方式(https://wxauto.loux.cc/docs/intro)
# 原著作是github中id为wxauto的作者，以下仅为应用过程  (原文地址：https://github.com/cluic/wxauto?tab=readme-ov-file)

# 0.  cd reptile_script_demo\wechat_demo

# 1.  pip install wxauto (A new release of pip is available表示安装成功)

# 2.  实现在限制的时间段内生成随机的时间戳发生微信自动向某人发送信息并且能够每天循环一次(功能需求)

# 3.  要求语言python 
#     所用到的库：wxauto,random,radar
#     这里的限制时间段暂时用'08:'+ str(a).zfill(2) + ':05'这样的方式限制，可以使用radar库会有更好的解决方式