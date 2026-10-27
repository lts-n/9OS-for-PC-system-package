from xdg.DesktopEntry import DesktopEntry 
from subprocess import run, PIPE
from gi.repository import Gtk, GdkPixbuf
from gi.repository import Gio

class Dock:
    def __init__(self):
        self.dock_files = {
            
        }
    def returndock(self):
        return self.dock_files
    
    def _getDefault(self, mime_type):
        app_info = Gio.AppInfo.get_default_for_type(mime_type, False)
        if app_info:
            return app_info.get_executable()
        return None