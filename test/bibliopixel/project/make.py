import tempfile
from bibliopixel.project import project
from bibliopixel.util import json
from .. mark_tests import SKIP_LONG_TESTS


def make_project(data):
    if isinstance(data, dict):
        desc = data
        name = None

    elif not isinstance(data, str):
        raise ValueError('Cannot understand data %s' % data)

    else:
        if '{' in data:
            fp = tempfile.NamedTemporaryFile(mode='w')
            fp.write(data)
            fp.seek(0)
            name = fp.name
        else:
            name = data

        desc = json.load(name)

    return project.project(desc, root_file=name)


def make(data, run_start=not SKIP_LONG_TESTS):
    project = make_project(data)

    if run_start:
        project.animation.start()

    return project.animation
