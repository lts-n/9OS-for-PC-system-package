import os
import shutil
from glob import glob

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from xdg.DesktopEntry import DesktopEntry

class Launchpad:
    def __init__(self):
        self.desktop_files = {}

    def _getIconpath(self, icon_name):
        if not icon_name:
            return None
        if os.path.isabs(icon_name) and os.path.exists(icon_name):
            return icon_name

        theme = Gtk.IconTheme.get_default()
        info = theme.lookup_icon(icon_name, 48, 0)
        if info:
            return info.get_filename()
        return None

    def _command_exists(self, command):
        if os.path.isabs(command):
            return os.path.isfile(command) and os.access(command, os.X_OK)
        return shutil.which(command) is not None

    def _is_visible_app(self, entry):
        if entry.getType() != "Application":
            return False
        if entry.getNoDisplay() or entry.getHidden():
            return False
        if not entry.getExec():
            return False

        try_exec = entry.getTryExec()
        if try_exec and not self._command_exists(try_exec):
            return False

        current_desktops = set(
            desktop for desktop in os.environ.get("XDG_CURRENT_DESKTOP", "").split(":") if desktop
        )
        only_show_in = set(entry.getOnlyShowIn())
        not_show_in = set(entry.getNotShowIn())

        if current_desktops and only_show_in and not current_desktops & only_show_in:
            return False
        if current_desktops and not_show_in and current_desktops & not_show_in:
            return False

        return True

    def _desktop_files(self):
        data_home = os.environ.get(
            "XDG_DATA_HOME", os.path.expanduser("~/.local/share")
        )
        data_dirs = os.environ.get(
            "XDG_DATA_DIRS", "/usr/local/share:/usr/share"
        ).split(":")

        seen = set()
        for directory in [data_home] + data_dirs:
            pattern = os.path.join(directory, "applications", "*.desktop")
            for file in sorted(glob(pattern)):
                app_id = os.path.basename(file)
                if app_id in seen:
                    continue
                seen.add(app_id)
                yield file

    def builddict(self):
        self.desktop_files = {}

        for file in self._desktop_files():
            try:
                entry = DesktopEntry(file)
                if not self._is_visible_app(entry):
                    continue

                self.desktop_files[file] = {
                    "name": entry.getName(),
                    "icon": self._getIconpath(entry.getIcon()),
                    "path": file
                }
            except Exception:
                pass

        return dict(
            sorted(
                self.desktop_files.items(),
                key=lambda item: item[1]["name"].casefold()
            )
        )