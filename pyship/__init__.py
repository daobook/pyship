""" pyship - ship python apps """

__application_name__ = "pyship"

python_interpreter_exes = {True: "pythonw.exe", False: "python.exe"}  # True is GUI, False is CLI

APP_DIR_NAME = "app"

from .__version__ import __version__, __author__
from .logging import PyshipLog, get_logger, log_process_output
from .pyship_print import pyship_print
from .os_util import is_windows, mkdirs, rmdir, copy_tree, get_target_os
from .exe_return_codes import restart_return_code, can_not_find_file_return_code, ok_return_code, error_return_code
from .subprocess_run import subprocess_run
from .module_info import ModuleInfo
from .target_app_info import TargetAppInfo
from .nsis import run_nsis
from .file_download import file_download, extract
from .create_launcher import create_launcher
from .pyshipy import create_base_pyshipy, version_from_pyshipy_zip
from .pyship import PyShip, install_target_app
from .updater.updater import Updater
from .updater.aws import UpdaterAwsS3
from .updater.local import UpdaterLocal
from .main import main
