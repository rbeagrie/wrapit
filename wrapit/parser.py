from doit.cmd_run import Run
import sys

doit_options = [
    {
        "option_string": "--doit-db-file", 
        "name": "dep_file", 
        "kwargs": {
            "default": ".doit.db", 
            "help": "file used to save successful runs"
        }
    }, 
    {
        "option_string": "--doit-backend", 
        "name": "backend", 
        "kwargs": {
            "default": "dbm", 
            "choices": Run().get_backends().keys(),
            "help": "Select dependency file backend. [default: %(default)s]"
        }
    }, 
    {
        "option_string": "--doit-check-file-uptodate", 
        "name": "check_file_uptodate", 
        "kwargs": {
            "default": "md5", 
            "choices": ["md5", "timestamp"],
            "help": "Choose how to check if files have been modified.\nAvailable options:\n  'md5': use the md5sum\n  'timestamp': use the timestamp\n"
        }
    }, 
    {
        "option_string": "--doit-dir", 
        "name": "cwdPath", 
        "kwargs": {
            "default": None, 
            "help": "set path to be used as cwd directory"
        }
    }, 
    {
        "option_string": "--doit-always-execute", 
        "name": "always", 
        "kwargs": {
            "action": 'store_true',
            "help": "always execute tasks even if up-to-date",
        }
    }, 
    {
        "option_string": "--doit-continue", 
        "name": "continue", 
        "kwargs": {
            "action": 'store_true',
            "help": "continue executing tasks even after a failure"
        }
    }, 
    {
        "option_string": "--doit-verbosity", 
        "name": "verbosity", 
        "kwargs": {
            "default": 1,
            "choices": range(3),
            "type": int,
            "help": "0 capture (do not print) stdout/stderr from task.\n1 capture stdout only.\n2 do not capture anything (print everything immediately)."
        }
    }, 
    {
        "option_string": "--doit-reporter", 
        "name": "reporter", 
        "kwargs": {
            "default": "console", 
            "choices": Run().get_reporters().keys(),
            "help": "Choose output reporter."
        }
    }, 
    {
        "option_string": "--doit-output-file", 
        "name": "outfile", 
        "kwargs": {
            "nargs": "?",
            "default": sys.stdout,
            "help": "write output into file [default: stdout]"
        }
    }, 
    {
        "option_string": "--doit-process", 
        "name": "num_process", 
        "kwargs": {
            "default": 0,
            "type": int,
            "help": "number of subprocesses (0 = serial processing)"
        }
    }, 
    {
        "option_string": "--doit-parallel-type", 
        "name": "par_type", 
        "kwargs": {
            "default": "process", 
            "choices": ['process', 'thread'],
            "help": "Tasks can be executed in parallel in different ways:\n'process': uses python multiprocessing module\n'thread': uses threads"
        }
    }, 
    {
        "option_string": "--doit-pdb", 
        "name": "pdb", 
        "kwargs": {
            "action": 'store_true',
            "help": "get into PDB (python debugger) post-mortem in case of unhandled exception"
        }
    }, 
    {
        "option_string": "--doit-single", 
        "name": "single", 
        "kwargs": {
            "action": 'store_true',
            "help": "Execute only specified tasks ignoring their task_dep [default: %(default)s]"
        }
    }, 
    {
        "option_string": "--doit-auto-delayed-regex", 
        "name": "auto_delayed_regex", 
        "kwargs": {
            "action": 'store_true',
            "help": "Uses the default regex '.*' for every delayed task loader for which no regex was explicitly defined"
        }
    }
]

def add_doit_options(parser, options_to_add=None):

    if options_to_add is None:
        options_to_add = [doit_opt['name'] for doit_opt in doit_options]

    for doit_opt in doit_options:

        if doit_opt['name'] in options_to_add:
            parser.add_argument(doit_opt['option_string'],
                                dest=doit_opt['name'],
                                **doit_opt['kwargs'])

def config_from_args(args):
    config = {}

    for doit_opt in doit_options:

        opt_name = doit_opt['name']

        if hasattr(args, opt_name):

            config[opt_name] = getattr(args, opt_name)

    return config
