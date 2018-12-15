# coding=utf-8
"""
Eğer Smart mirrorun base pathi sistem pathine eklenmemişse eklensin
bu dosya bunun bulunduğu konumdaki modüller  import edilirken çalışır!!!
smartmırrorv2 ana yola çıkan ilk folder da kalıyoruz ki patha SMARTMIRRORV2 eklensin
"""

from os.path import dirname
import sys

# base path varma işlemi her init dosyası için farklılık gösterebilir onu iyi ayarlamak lazım
current_folder = dirname(dirname(__file__))
base_path = current_folder

is_set_path = False
for path in sys.path:
    if path == base_path:
        is_set_path = True

if not is_set_path:
    sys.path.append(base_path)