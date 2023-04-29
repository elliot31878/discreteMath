from utils.dirHandler import DirManager
from core.concentrateHandlers.concentrateHandlers import ConcentrateHandlers

from importlib import import_module


class ToolsManager:

    def __init__(self):
        super(ToolsManager, self).__init__()

        self.dir_manager = DirManager()
        self.concentrate_handlers = ConcentrateHandlers()

        self.__init_tools__()

    def __init_tools__(self):
        tools_list_name = [
            tool for tool in self.dir_manager.get_all_directory(
                f"{self.dir_manager.current_dir}/core/plugins/"
            )
        ]

        for tool_name in tools_list_name:
            plugin_module_path = f"core.plugins.{tool_name}.toolsHandler"
            plugin_module = import_module(plugin_module_path)
            plugin = plugin_module.ToolHandler()
            self.concentrate_handlers.inject(plugin)
