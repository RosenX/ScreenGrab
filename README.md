# 介绍
笔试有摄像头时可以使用该工具进行截屏，保存题目，仅限windows下使用

# 安装方法
## step 1
安装python2.7  __32位__
## step 2
将PYTHON_PATH/Scripts和PYTHON_PATH加入到环境变量中
## step 3
在控制台执行

pip install Pillow-3.4.1-cp27-cp27m-win32.whl

pip install pyHook-1.5.1-cp27-none-win32.whl

pip install pywin32-220.1-cp27-cp27m-win32.whl

## step 4
将PYTHON_PATH/Lib/site-packages/pywin32_system32中pythoncom27.dll和pywintypes27.dll移动到PYTHON_PATH/Lib/win32/lib中
