# -*- coding: utf-8 -*-
import os

def run(**args):   # �i�����i�ܼƶq���ޭz
   print "[*] In dirlister module."
   files = os.listdir(".")  # �ثe�ɮק��U�Ҧ��ɮ�
   
   return str(files)
   