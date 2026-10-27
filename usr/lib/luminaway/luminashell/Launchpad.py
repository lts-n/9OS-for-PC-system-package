from multiprocessing.util import info
from xdg.DesktopEntry import DesktopEntry 
from subprocess import run, PIPE
from gi.repository import Gtk

class Launchpad:
    def __init__(self):
        self.desktop_files = {}
    def _getIconpath(self, icon_name):
        theme = Gtk.IconTheme.get_default()
        info = theme.lookup_icon(icon_name, 48, 0)
        if info:
            return info.get_filename()
        return None
    def builddict(self):
        files = run("file -k /usr/share/applications/*.desktop | cut -d: -f1", shell=True, stdout=PIPE, stderr=PIPE)
        files = files.stdout.decode().splitlines()
    
        for file in files:
            try:
                entry = DesktopEntry(file)
                self.desktop_files[file] = {
                    "name": entry.getName(),
                    "icon": self._getIconpath(entry.getIcon()),
                    "path": file
                }
            except: pass

        return self.desktop_files