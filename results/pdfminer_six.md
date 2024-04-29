> Github 阅读：[https://github.com/shandianchengzi/PDF2HTML_Samples/blob/main/results/pdfminer.six.md](https://github.com/shandianchengzi/PDF2HTML_Samples/blob/main/results/pdfminer.six.md)  
> CSDN 阅读：[【记录】Python3｜ 将 PDF 转换成 HTML/XML（✅⭐pdfminer.six）](https://blog.csdn.net/qq_46106285/article/details/138095328)

> 参考：[PDF 到 HTML/XML 转换 Python 库 - pdfminer.six 入门](https://products.documentprocessing.com/zh/conversion/python/pdfminer.six)  

## 1 安装

```python
pip install pdfminer.six
```

## 2 测试代码


测试代码可以看仓库：[https://github.com/shandianchengzi/PDF2HTML_Samples/tree/main/python_samples/test_pdfminer_six](https://github.com/shandianchengzi/PDF2HTML_Samples/tree/main/python_samples/test_pdfminer_six)

其目录结构如是：

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/75cb65db0825401494111dc64003deb3.png)

## 3 测试结果

### 3.1 转 html 的结果

<font color='red' size=4>实质就是把每一行转成 span 元素，没有任何节点嵌套等格式。</font>

纯表格页面的结果（看到结果的我都笑了，这什么玩意）：

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/d04f369cf0be499d9a13a0ad5d079336.png)

文字+表格的页面的结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/7b43e6d749f94a88b19b6a5d4a235065.png)

### 3.2 转 xml 的结果

<font color='red' size=4>实质就是把每一个字转成 text 元素，没有任何节点嵌套等格式。</font>

众所周知，xml 文件是无法直接查看的，它只是个方便记录数据的、和 html 长得差不多但是小很多的文件。

文字+表格的页面的结果（直接查看结果，实话说看到这里我就知道凉透了）：

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/3924aaf1db3b4a29af78bc50e370b909.png)

文字+表格的页面的结果（通过在线 XML 元素查看器查看，简直了。。每个节点只是一个字母或者符号）：

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/651ad76babc3462199084f1264ce89e5.png)


## 4 总体评价：✅⭐
能跑，没用。
也很可能是我没找到正确的打开方式。。。

后来发现，这个工具是专供 Python2 的，详见 https://pypi.org/project/pdfminer/

> Warning: Starting from version 20191010, PDFMiner supports Python 3 only. For Python 2 support, check out pdfminer.six. https://pypi.org/project/pdfminer/

怪不得这么难用。。