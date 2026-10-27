import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import os
import sys
luminashell = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if luminashell not in sys.path:
    sys.path.insert(0, luminashell)
import config
from Folder import Folder

class View(Gtk.Window):
    def __init__(self):
        super().__init__(title="Finder")

        directory = Folder("/")

        self.set_border_width(10)
        self.set_default_size(800, 600)

        self.set_app_paintable(True)
        self.set_resizable(False)
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual:
            self.set_visual(visual)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("css/transparentStylesheet.css")
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
        self.add(self.scrolled_window)

        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(10)
        self.grid.set_column_spacing(10)
        self.grid.set_name("mainBox")

        for item in directory.list():
            item_path = os.path.join(directory.path, item)
            name = item
            pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
                "media/icons/folder_icon.ico",
                width=config.icon_size,
                height=config.icon_size,
                preserve_aspect_ratio=True
            )

            button_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

            image = Gtk.Image.new_from_pixbuf(pixbuf)
            label = Gtk.Label(label=name)

            button = Gtk.Button()
            button.add(image)
            button_box.add(button)
            button_box.add(label)
            button.connect("clicked", lambda: self.change_directory(item_path))

            self.grid.attach(button_box, len(self.grid.get_children()) % 8, len(self.grid.get_children()) // 8, 1, 1)

        self.scrolled_window.add(self.grid)
        self.show_all()
    def change_directory(self, path):
        directory = Folder(path)
        

View()
Gtk.main()