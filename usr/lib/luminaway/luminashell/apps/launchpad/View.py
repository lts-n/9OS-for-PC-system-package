import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, Gdk, GdkPixbuf, GtkLayerShell
import os
import sys
from subprocess import Popen
luminashell = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if luminashell not in sys.path:
    sys.path.insert(0, luminashell)
import config
from Launchpad import Launchpad
from Screen import Screen

launchpad_object = Launchpad()
screen_object = Screen(0)

class View(Gtk.Window):
    def __init__(self):
        super().__init__(title="Launchpad")

        self.maximize()
        self.set_border_width(10)

        self.set_app_paintable(True)
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("css/launchpadStylesheet.css")
        Gtk.StyleContext.add_provider_for_screen(
            screen,
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC,
            Gtk.PolicyType.AUTOMATIC
        )
        self.scrolled_window.set_hexpand(True)
        self.scrolled_window.set_vexpand(True)
        self.add(self.scrolled_window)

        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(10)
        self.grid.set_column_spacing(10)
        self.grid.set_name("mainBox")

        self.grid.set_halign(Gtk.Align.CENTER)
        self.grid.set_valign(Gtk.Align.CENTER)

        self.scrolled_window.add(self.grid)

        screen_width = screen_object.width()
        icon_space = config.icon_size + 100
        max_cols = max(1, screen_width // icon_space)

        col = 0
        row = 0

        apps = launchpad_object.builddict()

        for item, data in apps.items():
            path = data.get("path")
            icon = data.get("icon")

            if not path or not icon or not os.path.exists(icon):
                continue

            btn = Gtk.Button()
            btn.set_name("launchpad-button")

            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_size(
                icon, config.icon_size, config.icon_size
            )
            btn.set_image(Gtk.Image.new_from_pixbuf(pixbuf))

            btn.connect("clicked", self.launch_app, path)

            self.grid.attach(btn, col, row, 1, 1)

            col += 1
            if col >= max_cols:
                col = 0
                row += 1

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def launch_app(self, button, desktop_path):
        app_id = os.path.splitext(os.path.basename(desktop_path))[0]
        Popen(["gtk-launch", app_id])
        self.destroy()

View()
Gtk.main()