import os
import pytest

MODULES_PATH = './modules'

def get_submodules(module):
    pkg_name = module.replace('scikit-surgery', 'sksurgery')

    submodules_path = os.path.join(MODULES_PATH, module, pkg_name)

    # Get all files recursively (https://stackoverflow.com/questions/19309667/recursive-os-listdir)
    all_files = \
        [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(submodules_path)) for f in fn]

    # We just want e.g. algorithms.averagequaternions.py rather than
    # scikit-surgerycore/sksurgerycore/algorithms/averagequaternions.py
    all_files = [f.replace(submodules_path, "") for f in all_files if f.endswith('.py')]

    # Get rid of __init__.py, _version.py
    submodules = [f for f in all_files if '__init__.py' not in f]
    submodules = [f for f in submodules if '_version.py' not in f]

    # strip .py ending
    submodules = [f.rstrip('.py') for f in submodules]

    # Convert to module notation
    submodules = [f.replace('\\', '.') for f in submodules]

    return submodules

def check_documentation(module_name, submodule_list):
        module_documentation_file = os.path.join(MODULES_PATH, module_name, 'doc', 'module_ref.rst')

        with open(module_documentation_file, 'r') as f:
            documentation = f.read()

        for submodule in submodule_list:
            print(f'Checking {submodule} is in {module_documentation_file}')
            assert submodule in documentation

def test_all_submodules_documented():
    modules = os.listdir(MODULES_PATH)

    for module in modules:
        submodules = get_submodules(module)
        check_documentation(module, submodules)


