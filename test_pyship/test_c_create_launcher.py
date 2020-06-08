from pathlib import Path
import os

from ismain import is_main

from pyship import create_launcher, TargetAppInfo, mkdirs
from test_pyship import TST_APP_PROJECT_DIR, TST_APP_FROZEN_DIR, TST_APP_NAME_0_0_1, TST_APP_LAUNCHER_EXE_PATH


def test_create_launcher():

    target_app_info = TargetAppInfo(Path(TST_APP_PROJECT_DIR))
    test_app_icon_path = Path(TST_APP_PROJECT_DIR, f"{TST_APP_NAME_0_0_1}.ico")

    try:
        # first time with no user provided icon - will exit with the icon put back
        os.unlink(test_app_icon_path)
    except FileNotFoundError:
        pass

    for _ in range(0, 2):
        mkdirs(TST_APP_FROZEN_DIR, remove_first=True)
        create_launcher(target_app_info, TST_APP_FROZEN_DIR)
        assert(TST_APP_LAUNCHER_EXE_PATH.exists())


if is_main():
    test_create_launcher()
