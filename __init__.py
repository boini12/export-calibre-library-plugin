from calibre.customize import InterfaceActionBase

class ExportCalibreBooksAction(InterfaceActionBase):
    name = "Automatic Export Calibre Books"
    description = "Export all books from the Calibre library to specified locations"
    supported_platforms = ['osx']
    author = 'ibohr'
    version = (1, 0, 0)
    minimum_calibre_version = (0, 7, 53)

    actual_plugin = 'calibre_plugins.export_calibre_books.ui:InterfacePlugin'

    def is_customizable(self) -> bool:
        '''
        True to enable customization via
        Preferences->Plugins
        '''
        return True
    
    def config_widget(self):
        '''
        Return an instance of the configuration widget for this plugin
        '''
        # from calibre_plugins.export_calibre_books.config import ConfigWidget
        # return ConfigWidget()

        # Placeholder until config widget is implemented
        return "Configuration widget not implemented yet", "Please implement the configuration widget."
    

    def save_settings(self, config_widget):
        '''
        Save settings from the configuration widget
        '''
        # Implement saving settings from config_widget
        pass