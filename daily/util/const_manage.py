#!/usr/bin/env python
# encoding: utf-8
'''
@Author  : pentiumCM
@Email   : 842679178@qq.com
@Software: PyCharm
@File    : const_manage.py
@Time    : 2019/11/29 19:22
@desc	 : 项目常量管理方式 --类的方式
'''

import sys


class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("Can not change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError("const name %s is not all upper" % name)
        self.__dict__[name] = value


sys.modules[__name__] = _const()
