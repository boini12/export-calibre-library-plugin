from .export import export_books

from calibre.gui2.actions import InterfaceAction
from calibre_plugins.export_calibre_books.main import ExportDialog

class InterfacePlugin(InterfaceAction):
    name = "Export Calibre Books"

    # Do not define a keyboard shortcut
    action_spec = ('Export Calibre Books', None, 
                   'Export all books from the Calibre library to specified locations', None)
    
    def genesis(self):
        '''
        This method is called when the plugin is instantiated.
        '''
        icon = get_icons('images/icon.png', 'Export Calibre Books Plugin')
        
        self.qaction.setIcon(icon)
        self.qaction.triggered.connect(self.show_dialog)

    def show_dialog(self):
        base_plugin_object = self.interface_action_base_plugin
        do_user_config = base_plugin_object.do_user_config

        d = ExportDialog(self.gui, self.qaction.icon(), do_user_config)
        d.show()

    def apply_settings(self):
        '''
        Apply settings changed in the configuration dialog
        '''
        pass

    def shutting_down(self):
        '''
        This method is called when Calibre is quitting.
        '''
        db = self.gui.current_db.new_api
        current_db = self.gui.current_db
        export_books(db, current_db)
