from distutils.core import setup
import py2exe
import sys

#this allows to run it with a simple double click.
sys.argv.append('py2exe')

py2exe_options={
    "includes":["sip"],   #选项中“includes”是需要包含的文件，这里的”sip”是PyQt程序打包时需要添加的，如果不是PyQt程序不需要此项。
    "dll_excludes":["MSVCP90.dll",],  #dll_excludes”是需要排除的dll文件，这里的”MSVCP90.dll”文件，如果不排除的话会报error: MSVCP90.dll: No such file or directory错误。
    "compressed":0,  #compressed”为1，则压缩文件。

    "optimize":2,  #optimize”为优化级别，默认为0。
    "ascii":0,    #ascii”指不自动包含encodings和codecs。
    "bundle_files":1,  #bundle_files”是指将程序打包成单文件（此时除了exe文件外，还会生成一个zip文件。如果不需要zip文件，还需要设置zipfile = None）。1表示pyd和dll文件会被#打包到单文件中，且不能从文件系统中加载python模块；值为2表示pyd和dll文件会被打包到单文件中，但是可以从文件系统中加载python模块。64位的Py2exe不要添加本句。
}
setup(
    name="MacReplace",
    version='1.0',

    #注意，windows = ['pyqtdemo.py',]，这里使用的是windows，即没有命令行窗口出现，如果使用console则表示有命令行窗口出现。
    windows=['testpyui.py',],  #这里是同目录下要生成的程序主文件名
    zipfile=None,
    options={'py2exe':py2exe_options}
    )
