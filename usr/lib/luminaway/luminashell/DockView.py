import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
from Dock import Dock
from subprocess import Popen, PIPE
import config

dock_object = Dock()
def run(path):
    if path.endswith(".py"):
        com = Popen(f"python3 {path}", shell=True)
    else:
        Popen(path, shell=True)

class DockView(Gtk.Box):
    def __init__(self):
        super().__init__(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=12
        )

        self.set_name("dock")
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("css/dockviewStylesheet.css")
        
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        self.set_halign(Gtk.Align.CENTER)
        self.set_valign(Gtk.Align.CENTER)

        apps = dock_object.returndock()

        for app in apps:
            try:
                path = apps[app]["path"]
                btn = Gtk.Button()
                btn.set_name("dock-button")
                image = Gtk.Image.new_from_file(apps[app]["icon"])
                pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(apps[app]["icon"], config.icon_size, config.icon_size)
                image.set_from_pixbuf(pixbuf)
                btn.set_image(image)
                btn.connect(
                    "clicked",
                    lambda *_ , p=path: run(p)
                )
                self.pack_start(btn, False, False, 0)
            except: pass