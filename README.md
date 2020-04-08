# vmess-domain-coverter

# vmess-domain-coverter


type vmess domain of v2ray, convert to ip address.


#### 解决V2rayU和Easyconnect同时使用，V2rayU无法正常代理的问题。  [原Issues](https://github.com/yanue/V2rayU/issues/468)


初步确诊为DNS解析冲突，直接改为IP两者都可以正常使用，但因为机场ip不固定，手动更换ip操作会比较频繁，所以写了这段转换代码。


流程：


获取原始的一坨vmess -> base64解码、分割成独立vmess链接 -> 获取vmess中域名，转换成ip -> base64编码、组装成另一坨vmess链接的文件


#### 使用前需要将代码中的subscribe_url和filename修改为你自己的原始订阅地址和文件生成的路径


Mac或linux用户可以直接在生成文件的目录执行命令：


```python
#python2
python -m SimpleHTTPServer
```


```python
#python3
python3 -m http.server 8000
```



运行成功后在订阅地址里填写：[http://127.0.0.1:8000/your-file-name](http://127.0.0.1:8000/your-file-name)


有服务器资源的同学可以将上述脚本设置定时任务，定时获取转换最新订阅地址。
