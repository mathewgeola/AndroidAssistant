"""
pip install androguard -i https://pypi.tuna.tsinghua.edu.cn/simple
"""
import os
from androguard.core import apk
from androguard.core.apk import APK

apk.logger.remove(handler_id=None)

dir_path = os.path.dirname(os.path.abspath(__file__))
os.makedirs(dir_path, exist_ok=True)

for file_name in os.listdir(dir_path):
    file_path = os.path.join(dir_path, file_name)
    if os.path.splitext(file_path)[1] == ".apk":
        apk = APK(os.path.join(dir_path, file_name))
        new_file_name = apk.get_app_name() + "_" + apk.get_androidversion_name() + ".apk"
        if new_file_name != file_name:
            new_file_path = os.path.join(dir_path, new_file_name)
            os.rename(file_path, new_file_path)
            print(f"{file_name} -> {new_file_name}")
