from doit.cmd_base import ModuleTaskLoader
from .parser import config_from_args

class WrapitLoader(ModuleTaskLoader):
    """Loader class that does the loading of tasks"""
    def __init__(self, args, mod_dict):
        super(WrapitLoader, self).__init__(mod_dict)
        self.args = args

    def load_tasks(self, cmd, params, args):
        task_list, doit_config = super(WrapitLoader, self).load_tasks(cmd, params, args)
        
        if doit_config == {}:
            doit_config = config_from_args(self.args)

        for i in range(len(task_list)):
            task_list[i].options = vars(self.args)

        return task_list, doit_config

