from pathlib import Path

TST_APP_NAME = "tstpyshipapp"
TST_APP_ROOT_DIR = Path("test_pyship", TST_APP_NAME)
TST_APP_DIST_DIR = Path(TST_APP_ROOT_DIR, "dist")
TST_APP_FROZEN_DIR = Path(TST_APP_ROOT_DIR, "app", "win64", TST_APP_NAME)
TST_APP_LAUNCHER_EXE_PATH = Path(TST_APP_FROZEN_DIR, TST_APP_NAME, f"{TST_APP_NAME}.exe")
TST_APP_CACHE = Path(TST_APP_ROOT_DIR, "cache")
