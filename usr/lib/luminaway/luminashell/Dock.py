from xdg.DesktopEntry import DesktopEntry 
from subprocess import run, PIPE
from gi.repository import Gtk, GdkPixbuf
from gi.repository import Gio

class Dock:
    def __init__(self):
        self.dock_files = {
            "Finder": {
                "path": "apps/finder/View.py",
                "icon": "media/icons/finder_icon.png"
            },
            "Launchpad": {
                "path": "apps/launchpad/View.py",
                "icon": "media/icons/launchpad_icon.png"
            },
            "Web Browser": {
                "path": "chromium",
                "icon": "media/icons/browser_icon.png"
            },
            "Settings": {
                "path": "apps/settings/View.py",
                "icon": "media/icons/settings_icon.png"
            },
            "Music Player": {
                "path": self._getDefault("audio/mpeg"),
                "icon": "media/icons/music_icon.png"
            },
            "Video Player": {
                "path": self._getDefault("video/mp4"),
                "icon": "media/icons/video_icon.png"
            },
            "Image Viewer": {
                "path": self._getDefault("image/jpeg"),
                "icon": "media/icons/photo_icon.png"
            },
            "Clock": {
                "path": "apps/clock/main.py",
                "icon": "media/icons/clock_icon.png"
            }
        }
    def returndock(self):
        return self.dock_files
    
    def _getDefault(self, mime_type):
        app_info = Gio.AppInfo.get_default_for_type(mime_type, False)
        if app_info:
            return app_info.get_executable()
        return None