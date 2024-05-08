[toc]
# PyMuPDF 使用体验与评估

> Github 阅读：[https://github.com/shandianchengzi/PDF2HTML_Samples/blob/main/results/PyMuPDF.md](https://github.com/shandianchengzi/PDF2HTML_Samples/blob/main/results/PyMuPDF.md)  
> CSDN 阅读：[【记录】Python3｜ 将 PDF 转换成 HTML/XML（✅⭐PyMuPDF+tqdm）](https://blog.csdn.net/qq_46106285/article/details/138549152)  

> 参考：
> 1. [【Python | PDF】如何使用Python将PDF转换为HTML页面？](https://blog.csdn.net/qq_28505809/article/details/124147552) 
> 2. [Convert PDF to HTML via PyMuPDF - StackOverFLow](https://stackoverflow.com/questions/71812718/convert-pdf-to-html-via-pymupdf)

## 1 安装指南

要使用 PyMuPDF，还需要配合 tqdm 使用。

您可以通过 Python 的包管理工具 pip 进行安装。在命令行中执行以下命令：

```bash
pip install PyMuPDF
# pip3 install PyMuPDF

pip install tqdm
# pip3 install tqdm
```

## 2 测试代码

为了帮助您更好地理解 PyMuPDF 的用法，我提供了一个测试代码示例。您可以在以下 GitHub 仓库中找到相关代码和样本文件：[https://github.com/shandianchengzi/PDF2HTML_Samples/tree/main/python_samples/test_PyMuPDF](https://github.com/shandianchengzi/PDF2HTML_Samples/tree/main/python_samples/test_PyMuPDF)

其目录结构如是：

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/75cb65db0825401494111dc64003deb3.png)

## 3 测试结果

### 3.1 转 HTML 的结果

结果不是很好，该区分的格式倒是区分出来了。

但是挺乱的，只能说凑合能用，给用户用的话就有点过分。
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/a9a181726e4e4341b3548f02d7d34e62.png)

### 3.2 转 XML 的结果

通过在线 XML 元素查看器查看，如下图所示：
![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/7a009b4733594d91bdf70a203ea23995.png)


不过多评价，和pdfminer.six转换的差不多，不过比pdfminer.six稍微整齐一丁点：
> 具体可看：[【记录】Python3｜ 将 PDF 转换成 HTML/XML（✅⭐pdfminer.six）](https://shandianchengzi.blog.csdn.net/article/details/138095328)

![在这里插入图片描述](https://img-blog.csdnimg.cn/direct/05197c68047a447289456f58c0c72c88.png)


## 总体评价：✅⭐

和pdfminer.six转换结果类似，比pdfminer.six能提取出来的样式多了一丁点。
pdfminer.six的测评过程可以看这篇：[【记录】Python3｜ 将 PDF 转换成 HTML/XML（✅⭐pdfminer.six）](https://shandianchengzi.blog.csdn.net/article/details/138095328)。

截止目前测到的最好用的是 pdf2htmlEX，推荐阅读：[【记录】Python3｜ 将 PDF 转换成 HTML/XML（✅⭐⭐⭐⭐pdf2htmlEX）](https://shandianchengzi.blog.csdn.net/article/details/138356607)