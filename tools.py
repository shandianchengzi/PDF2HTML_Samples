'''
python3 tools.py [action] [tool_name] [output_format]

# 功能1: 新建
# 测试的时候在 `python_samples` 下新建一个工具测试文件夹，文件夹的名字以 `test_` 开头，并把特殊字符全换成 `_`。
# 测试文件命名规则为 `to_` + `output_format` + `.py`。
action == new: 
1. python3 tools.py new pdfminer.six        : make new tool test directory, input: tool name. output: tool directory path.
2. python3 tools.py new pdfminer.six html   : make new tool test file, input: tool name, output_format. output: tool test file path.

# 功能2: 测试
action == test:
1. python3 tools.py test pdfminer.six       : test all the tools, input: tool name. output: None.
2. python3 tools.py test pdfminer.six html  : test one tool, input: tool name, output_format. output: None.
'''

import os
import argparse

file_dir = os.path.realpath(os.path.dirname(__file__))
os.chdir(file_dir)

def make_new_tool_test_directory(tool_name):
    # make new tool test directory
    tool_test_dir = os.path.join(file_dir, f"./python_samples/test_{tool_name}")
    os.makedirs(tool_test_dir, exist_ok=True)
    return tool_test_dir

def make_new_tool_test_file(tool_name, output_format):
    # make new tool test file
    tool_test_file = os.path.join(file_dir, f"./python_samples/test_{tool_name}/to_{output_format}.py")
    # check if tool test file already exists
    if os.path.exists(tool_test_file) and os.path.getsize(tool_test_file) > 0: # if not empty, return
        return tool_test_file
    with open(tool_test_file, 'w', encoding='utf-8') as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write("# Reference: <FILL IN IF YOU HAVE A REFERENCE>\n")
        f.write("\n")
        f.write("need_pip_install = True # If this tool is not installed by the pip, let it be False.")
        f.write(f"def convert_pdf_to_{output_format}(pdf_file_path, output_file_path):\n")
        f.write("    '''\n")
        f.write(f"    \"convert_pdf_to_{output_format}\" is used to convert a PDF file to an {output_format} file.\n")
        f.write("    :param pdf_file_path: str: The file path of the PDF file to be converted.\n")
        f.write(f"    :param output_file_path: str: The file path to save the converted {output_format} file.\n")
        f.write("    :return: None\n")
        f.write("    '''\n")
        f.write("    # Write your code here\n")
        f.write("    pass\n")
    print(f"Succesfully created new tool test file: {tool_test_file}")
    return tool_test_file

def make_new_results_document(tool_name, raw_tool_name):
    # make new results document
    results_doc = os.path.join(file_dir, f"./results/{tool_name}.md")
    if os.path.exists(results_doc) and os.path.getsize(results_doc) > 0: # if not empty, return
        return results_doc
    with open(results_doc, 'w', encoding='utf-8') as f:
        f.write(f'''[toc]
> Github 阅读：[https://github.com/shandianchengzi/PDF2HTML_Samples/blob/main/results/{tool_name}.md](https://github.com/shandianchengzi/PDF2HTML_Samples/blob/main/results/{tool_name}.md)  
> CSDN 阅读：[](https://blog.csdn.net/qq_46106285/article/details/待补充)  

> 参考：[]()  

# {raw_tool_name} 使用体验与评估

## 1 安装指南

要使用 {raw_tool_name}，您可以通过 Python 的包管理工具 pip 进行安装。在命令行中执行以下命令：

```bash
pip install {raw_tool_name}
```

## 2 测试代码

为了帮助您更好地理解 {raw_tool_name} 的用法，我提供了一个测试代码示例。您可以在以下 GitHub 仓库中找到相关代码和样本文件：[https://github.com/shandianchengzi/PDF2HTML_Samples/tree/main/python_samples/{tool_name}](https://github.com/shandianchengzi/PDF2HTML_Samples/tree/main/python_samples/{tool_name})

## 3 测试结果

### 3.1 转 HTML 的结果

### 3.2 转 XML 的结果

## 总体评价：✅⭐

        ''')
    print(f"Succesfully created new results document: {results_doc}")
    return results_doc

def get_tool_module(tool_name, output_format):
    module = f"python_samples.test_{tool_name}.to_{output_format}"
    import_str = f"from {module} import convert_pdf_to_{output_format}, need_pip_install"
    func_str = f"convert_pdf_to_{output_format}"
    return import_str, func_str

def arg_parse():
    parser = argparse.ArgumentParser(description='Make new tool test directory or file')
    # action
    action_parser = parser.add_subparsers(dest='action', help='Action to perform')
    action_parser.required = True
    new_parser = action_parser.add_parser('new', help='Make new tool test directory or file')
    new_parser.add_argument('tool_name', type=str, help='Tool name')
    # optional arguments
    new_parser.add_argument('output_format', type=str, nargs='?', default=None, help='Output format')

    # test
    test_parser = action_parser.add_parser('test', help='Test the tool')
    test_parser.add_argument('tool_name', type=str, help='Tool name')
    test_parser.add_argument('output_format', type=str, nargs='?', default=None, help='Output format')
    return parser.parse_args()

if __name__ == "__main__":
    args = arg_parse()
    if args.action == 'new':
        # replace special characters in tool name
        tool_name = args.tool_name.replace(".", "_").replace("-", "_").replace(" ", "_")
        tool_test_dir = make_new_tool_test_directory(tool_name)
        if args.output_format is None:
            print(f"Your tool test directory: {tool_test_dir}")
        else:
            tool_test_file = make_new_tool_test_file(tool_name, args.output_format)
            print(f"Your tool test file: {tool_test_file}")
        # make new results document
        results_doc = make_new_results_document(tool_name, args.tool_name)
        print(f"Your tool test results document: {results_doc}")
    elif args.action == 'test':
        from python_samples.test_framework import test_func
        # test the tool all the format
        tool_name = args.tool_name.replace(".", "_").replace("-", "_").replace(" ", "_")
        if args.output_format is None:
            # get all the to_*.py files
            tool_test_dir = os.path.join(file_dir, f"./python_samples/test_{tool_name}")
            tool_test_formats = [f[3:-3] for f in os.listdir(tool_test_dir) if f.startswith("to_") and f.endswith(".py")]
            for tool_test_format in tool_test_formats:
                import_str, func = get_tool_module(tool_name, tool_test_format)
                need_pip_install = True
                exec(import_str)
                if need_pip_install:
                    # pip install the tool if not installed
                    os.system(f"pip install {args.tool_name}")
                exec(f"test_func({func})")
        else:
            import_str, func = get_tool_module(tool_name, args.output_format)
            exec(import_str)
            exec(f"test_func({func})")
    else:
        raise ValueError(f"Invalid action: {args.action}")