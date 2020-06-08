from pathlib import Path
from semver import VersionInfo

from pyship import rmdir, mkdirs, subprocess_run, get_logger, __application_name__

TST_APP_NAME = "tstpyshipapp"
TST_APP_VERSION = VersionInfo(0, 0, 1)
TST_APP_PROJECT_DIR = Path("test_pyship", TST_APP_NAME)
TST_APP_DIST_DIR = Path(TST_APP_PROJECT_DIR, "dist")
TST_APP_FROZEN_PARENT = Path(TST_APP_PROJECT_DIR, "frozen")
TST_APP_FROZEN_DIR = Path(TST_APP_FROZEN_PARENT, TST_APP_NAME)
TST_APP_LAUNCHER_EXE_PATH = Path(TST_APP_FROZEN_DIR, TST_APP_NAME, f"{TST_APP_NAME}.exe")
TST_APP_CACHE = Path(TST_APP_PROJECT_DIR, "cache")

log = get_logger(__application_name__)


def write_test_app_version(version: VersionInfo):
    module_dir = Path(TST_APP_PROJECT_DIR, TST_APP_NAME)
    rmdir(Path(module_dir, "__pycache__"))  # to be safe ...
    with open(Path(module_dir, "__version__.py"), "w") as f:
        f.write("\n".join([f"# automatically generated by {__name__}", f'__version__ = "{str(version)}"', ""]))


def test_app_flit_build():
    mkdirs(TST_APP_DIST_DIR, remove_first=True)
    flit_exe_path = Path("venv", "Scripts", "flit.exe")
    pyproject_path = Path(TST_APP_PROJECT_DIR, "pyproject.toml")
    if not flit_exe_path.exists():
        log.error(f"{flit_exe_path} does not exist")
    elif not pyproject_path.exists():
        log.error(f"{pyproject_path} does not exist")
    else:
        # use flit to build the target app into a distributable package in the "dist" directory
        subprocess_run([str(flit_exe_path), "-f", str(pyproject_path), "build"], stdout_log=print)
