#!/usr/bin/env python
import os
import sys

if __name__=="--main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE","ask.settings")
	from django.core.management import execute_from_comand_line
	execute_from_comand_line(sys.argv)
