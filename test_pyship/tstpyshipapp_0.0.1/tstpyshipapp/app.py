import json
import sys

from balsa import Balsa, get_logger

from pyshipupdate import UpdaterAwsS3, restart_return_code, ok_return_code
from pyshipupdate import __version__ as pyshipupdate_version
from pyship import __author__ as pyship_author
from pyship import __version__ as pyship_version

from .__init__ import __application_name__ as name
from .__init__ import __version__ as version

logger_name = f"{name}_{version}"

log = get_logger(logger_name)


def tstpyshipapp():

    verbose = len(sys.argv) > 1 and sys.argv[1].lower() in ["-v", "--verbose"]

    balsa = Balsa(logger_name, pyship_author, verbose=verbose)
    balsa.init_logger()
    log.info(f"{pyshipupdate_version=}")
    log.info(f"{pyship_version=}")
    log.info(f"app {version=}")

    updater = UpdaterAwsS3(name, pyship_author)
    exit_code = restart_return_code if updater.update(version) else ok_return_code
    output = {"name": name, "version": version, "exit_code": exit_code}
    print(json.dumps(output))
    sys.exit(exit_code)
