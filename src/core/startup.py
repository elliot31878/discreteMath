
class StartUp:

    def __init__(self):
        super(StartUp, self)

    @staticmethod
    def __start_services__():
        from modules.services.toolsManager.toolsManager import ToolsManager

        ToolsManager()

        from modules.services.consoleapp.presentation import Presentation

        p = Presentation()
        p.show_elements()

    def start_app(self):
        self.__start_services__()