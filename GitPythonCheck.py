#!/usr/bin/env python
# -*- coding: utf-8 -*

from git.repo import Repo
import sys
import os
import re
import shutil

dict_project = dict()

# 工作目录
project_git_path = './gitPython'

class FileMetric:
	def __init__(self, file_name):
		self.file_name = file_name
		self.line_nos = []	


class ProjectMetric:
	def __init__(self, project_name):
		self.project_name = project_name
		self.files = dict()
		self.num = 0

	def addFile(self, file):
		self.files[file.file_name] = file
		self.num += 1		

	def print_info(self):
		print "--- find from project %s ---" % (self.project_name)
		for key in self.files.keys():
			print key
			print self.files[key].line_nos
		print '\n'	


# 文件逐行匹配, 记录文件名和行数
def analysiFile(project_name, parentdir, filename, pattern):
	line_no = 0
	filePath = parentdir + '/' + filename
	with open(filePath) as fo:
		for line in fo.readlines():
			line_no += 1
			match = pattern.search(line)
			if match:
				if not dict_project[project_name].files.has_key(filename):
					dict_project[project_name].addFile(FileMetric(filename))

				dict_project[project_name].files[filename].line_nos.append(line_no)


def git_file_pattern_find(args):

	if args and len(args) != 3:
		print "parms error: python GitPythonCheck.py [btanch] [regex] [projects]"
		return

	branch =  args[0]
	pattern = re.compile(r'%s' % args[1])
	project_names = args[2].split(',')

	# 打印 输入参数
	print 'find regex: %s from projects: %s branch: %s' % (pattern.pattern, project_names, branch)

	# 目录存在，则级联删除
	if os.path.exists(project_git_path):
		shutil.rmtree(project_git_path)

	for project_name in project_names:
		print 'clone %s %s...' % (project_name, branch)

		Repo.clone_from('https://gitlab.xxx.com/backend/' + project_name + '.git', to_path=project_git_path + '/' + project_name, branch=branch)

		dict_project[project_name] = ProjectMetric(project_name)

		work_path = project_git_path + '/' + project_name
		print 'work_path: %s' % (work_path)

		# 遍历目录下的所有文件
		for parentdir, dirname, filenames in os.walk(work_path):
			for filename in filenames:
				if os.path.splitext(filename)[1] == '.java':
					#分析具体文件
					analysiFile(project_name, parentdir, filename, pattern)

		# 输出查找结果
		dict_project[project_name].print_info()

# 从指定项目 gitLab 指定分支的代码中，查找对应关键字所在的文件 及 行数
# 用法举例：python GitPythonCheck.py dev '\"tts' lesson,home,onboarding
git_file_pattern_find(sys.argv[1:])
