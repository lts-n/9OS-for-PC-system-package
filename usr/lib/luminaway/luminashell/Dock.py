from xdg.DesktopEntry import DesktopEntry 
from subprocess import run, PIPE
from gi.repository import Gtk, GdkPixbuf
from gi.repository import Gio

gms = "python3 ../../lib9osforpc/webappframework/main.pyw http://guadaware-ms.rf.gd/"
webapp = "python3 ../../lib9osforpc/webappframework/main.pyw http://localhost:8000/"
icons_dir = "../../share/icons/hicolor/128x128/apps/"

class Dock:
    def __init__(self):
        self.dock_files = {
            "Launchpad": {
                "path": f"apps/launchpad/Launchpad.py",
                "icon": f"{icons_dir}9os-launchpad.png",
            },
            "File Manager (Legacy)": {
                "path": "apps/fm/View.py",
                "icon": f"{icons_dir}9os-fmlegacy.png",
            },
            "Safari": {
                "path": f"{webapp}safari",
                "icon": f"{icons_dir}safari.png",
            },
            "Music": {
                "path": f"{webapp}music",
                "icon": f"{icons_dir}9os-music.png",
            },
            "Guadaware Music Store": {
                "path": gms,
                "icon": f"{icons_dir}guadaware-musicstore.png",
            },
            "Gallery": {
                "path": f"{webapp}gallery",
                "icon": f"{icons_dir}9os-gallery.png",
            },
            "Contacts": {
                "path": f"{webapp}contacts",
                "icon": f"{icons_dir}9os-contacts.png",
            },
            "Calculator": {
                "path": f"{webapp}calculator",
                "icon": f"{icons_dir}9os-calculator.png",
            },
            "Clock": {
                "path": f"apps/clock/View.py",
                "icon": f"{icons_dir}9os-clock.png",
            },
            "Settings": {
                "path": f"{webapp}settings",
                "icon": f"{icons_dir}9os-settings.png",
            },
            "Settings (Legacy)": {
                "path": f"apps/settings_legacy/View.py",
                "icon": f"{icons_dir}9os-settings.png",
            },
        }
    def returndock(self):
        return self.dock_files
    
    def _getDefault(self, mime_type):
        app_info = Gio.AppInfo.get_default_for_type(mime_type, False)
        if app_info:
            return app_info.get_executable()
        return None