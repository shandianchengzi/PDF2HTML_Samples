## 前言

对比一下常用的 PDF 转 HTML/XML 的工具。

## 对比列表
问：pdf转xml或html的开源python工具有哪些？

在Python中，有几个开源工具可用于将PDF文件转换为XML或HTML格式。以下是其中一些：

1. pdfminer: Warning: Starting from version 20191010, PDFMiner supports Python 3 only. For Python 2 support, check out pdfminer.six. https://pypi.org/project/pdfminer/
2. pdfminer3k：据说是 pdfminer 的 Python3 版本，不清楚和 pdfminer.six 有什么区别。
3. PyPDF2: 这是一个纯Python库，用于处理PDF文件。虽然主要用于创建、阅读和修改PDF文件，但您也可以使用它来提取文本内容，并将其转换为XML或HTML格式。
4. pdf2xml: 这是一个命令行工具，可以将PDF文件转换为XML格式。虽然它不是Python库，但您可以通过Python的subprocess模块来调用该工具，并处理生成的XML文件。
5. pdf2htmlEX: 这是另一个命令行工具，用于将PDF文件转换为HTML格式。您可以通过Python的subprocess模块来调用该工具，并处理生成的HTML文件。https://blog.csdn.net/gitblog_00074/article/details/136775457
6. PyMuPDF+tqdm https://blog.csdn.net/qq_28505809/article/details/124147552
7. PDFQuery https://www.freecodecamp.org/chinese/news/extract-data-from-pdf-files-with-python
8. Spire.PDF https://blog.csdn.net/eiceblue/article/details/135988859, https://www.e-iceblue.com/Tutorials/Python/Spire.PDF-for-Python/Program-Guide/Conversion/Python-Convert-PDF-to-HTML.html
9.  pdfkit: Adobe 提到了这个库，但是有人说是 iOS 专用的，StackOverflow 上只找到这个：https://stackoverflow.com/questions/75757120/convert-pdf-to-html-using-python-and-pdfkit
10. pdftotree: 本软件包是我们开发自己的模块以替代 Adobe Acrobat 的成果。目前有几种将 pdf 转换为 html 的开源工具，但这些工具无法保留表格中的单元格结构。我们在这个项目中的目标是开发一个工具，提取 pdf 文档中的文本、数字和表格，并以易于使用的格式返回。https://pypi.org/project/pdftotree/
11. depdf: An ultimate pdf file disintegration tool. DePDF is designed to extract tables and paragraphs into structured markup language [eg. html] from embedding pdf pages. You can also use it to convert page/pdf to html. Built on top of pdfplumber. https://pypi.org/project/depdf/0.1.1/
12. poppdf: A python (3.6+) module that wraps poppler's pdftoimage, pdftohtml and pdftotext to extract informations from PDF. https://pypi.org/project/poppdf/

如果还有其他工具也可以尝试测试并添加进来。

❌pandoc：【已测，失败】`pandoc input.pdf -o output.html` 失败，pandoc 不接受 pdf 这个输入。详见 [【记录】Pandoc｜Linux安装最新Pandoc](https://blog.csdn.net/qq_46106285/article/details/138094313)。
✅⭐pdfminer.six: 【这个工具是专供 Python2 的，详见 https://pypi.org/project/pdfminer/】这是一个PDF文档解析器，可以用于提取文本、元数据以及页面布局信息。您可以使用pdfminer.six来提取PDF中的文本内容，并将其转换为XML或HTML格式。https://products.documentprocessing.com/zh/conversion/python/pdfminer.six 多参考一些文档。

✅⭐⭐⭐⭐pdf2htmlEX：除了大纲有点问题，其他都很好。它还提供了很多转换参数https://github.com/coolwanglu/pdf2htmlEX/wiki/Command-Line-Options

✅⭐PyMuPDF+tqdm：和pdfminer.six转换结果类似

✅⭐PDFQuery：不好，和pdfminer.six转换结果类似

✅⭐⭐⭐Spire.PDF：还行，就是转换参数太少，并且试用会有水印，最多只能转化10页

❌pdftotree：https://pypi.org/project/pdftotree/中说是将PDF转换成hOCR，测试也只生成了三个空文件，这个工具应该不能用于转html

## 测评过程

1. 运行本仓库根目录下的 `tools.py` 文件，新建测试目录和测试文件：
    ```bash
    python3 tools.py new pdfminer.six       # 新建 pdfminer.six 工具测试目录 `python_samples/test_pdfminer_six`
    python3 tools.py new pdfminer.six html  # 新建 pdfminer.six 工具的转换为 HTML 的测试文件 `python_samples/test_pdfminer_six/to_html.py`
    ```
2. 测试新工具的时候只需要重写新生成的测试文件的 `convert_pdf_to_{format}` 这个函数的内容，其他的我全部写好了。
   1. 写测试函数的时候，如果参考了网络上的内容，在测试文件的上方填写一下 `# Reference: ` 链接。
   2. 如果一个工具有多种写法，选结果最好的一种生成在 `output` 下。其他的已经写好的也不用删掉，可以注释了放一边。
   3. 如果写的时候调用了除了工具名以外的其他第三方库，添加到 `requirements.txt` 中，以便之后我们同步更新时可以通过 `pip install -r requirements.txt` 装好对方的依赖。
3. 写好函数之后，测试的方法：
   ```bash
   python3 tools.py test pdfminer.six       # 测试 pdfminer.six 工具下的所有格式转换文件
   python3 tools.py test pdfminer.six html  # 测试 pdfminer.six 工具的转换为 HTML 的测试文件
   ```

具体测试过程是调用 `python_sampls/test_framework.py`。
工具完整功能详见 `tools.py` 文件。

测试输出：输出的文件在当前测评的工具的文件夹下，并被命名为 `to_{format}_{pdf_name}.{format}`。例如 pdfminer.six 工具样例的输出，放到 `python_samples/test_pdfminer_six/outputs` 。

## 测评目的（如何评估效果）

1. 能分清 PDF 章节
2. 具备嵌套标签（就是格式化之后能看出来有**树状** DOM 元素的效果）
3. 统计一下各个工具的社区活跃度（开源的看 Star 数量和最后更新的时间）


## 测评结果

1. 修改 `README.md`，用符号简单标注一下工具好不好用。可用的符号：❌✅⭐✨。
   1. 完全用不了就打叉❌
   2. 用得了就✅
   3. 推荐指数⭐⭐⭐⭐⭐
   4. 如果你觉得这个工具很nb就✨
2. 详细说明可写在 `results/{工具名称}.md` 下。

## TODO

后续可以给它加上 GPT 自动根据描述/文章写测试用例的功能。

现在需要测的不是特别多，你先熟悉一下流程，先人工问问网页 GPT 吧。