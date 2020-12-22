#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 15:31
import os
import pytest


def method_name():
    report_path = os.path.join(os.path.dirname(__file__), 'report')
    report_file = os.path.join(report_path)
    args = ['-vsq', f'--alluredir={report_file}']
    pytest.main(args)
    cmd = 'allure generate --clean %s -o %s' % ('report\html', 'report')
    os.system(cmd)

if __name__ == '__main__':
    method_name()

