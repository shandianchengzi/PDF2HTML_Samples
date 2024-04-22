## 前言

对比一下常用的。

## 对比列表
问：pdf转xml或html的开源python工具有哪些？

在Python中，有几个开源工具可用于将PDF文件转换为XML或HTML格式。以下是其中一些：

1. pdfminer.six: 这是一个PDF文档解析器，可以用于提取文本、元数据以及页面布局信息。您可以使用pdfminer.six来提取PDF中的文本内容，并将其转换为XML或HTML格式。https://products.documentprocessing.com/zh/conversion/python/pdfminer.six 多参考一些文档。
2. pdfminer3k：
3. PyPDF2: 这是一个纯Python库，用于处理PDF文件。虽然主要用于创建、阅读和修改PDF文件，但您也可以使用它来提取文本内容，并将其转换为XML或HTML格式。
4. pdf2xml: 这是一个命令行工具，可以将PDF文件转换为XML格式。虽然它不是Python库，但您可以通过Python的subprocess模块来调用该工具，并处理生成的XML文件。
5. pdf2htmlEX: 这是另一个命令行工具，用于将PDF文件转换为HTML格式。您可以通过Python的subprocess模块来调用该工具，并处理生成的HTML文件。https://blog.csdn.net/gitblog_00074/article/details/136775457
6. PyMuPDF+tqdm https://blog.csdn.net/qq_28505809/article/details/124147552
7. PDFQuery https://www.freecodecamp.org/chinese/news/extract-data-from-pdf-files-with-python
8. Spire.PDF https://blog.csdn.net/eiceblue/article/details/135988859


❌pandoc：已测，失败

## 测评过程

1. 如果一个文件能解决，就在`python_samples`下新建一个python文件；如果解决不了就建一个文件夹。
2. 测评结果放在`output_results`里。如果需要图片说明可以把图片放在`imgs/`文件夹下，也可以自己写一篇 CSDN 博客暂放到那里。