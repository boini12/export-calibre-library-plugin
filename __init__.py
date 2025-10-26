from calibre.customize import InterfaceActionBase

class InterfacePluginExport(InterfaceActionBase):
    name = "Automatic Export Calibre Books"
    description = "Export all books from the Calibre library to specified locations"
    supported_platforms = ['osx', 'linux', 'windows']
    author = 'boini12'
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
        from calibre_plugins.export_calibre_books.config import ConfigWidget
        return ConfigWidget()
    

    def save_settings(self, config_widget):
        '''
        Save settings from the configuration widget
        '''
        config_widget.save_settings()

        ac = self.actual_plugin_
        if ac is not None:
            ac.apply_settings()