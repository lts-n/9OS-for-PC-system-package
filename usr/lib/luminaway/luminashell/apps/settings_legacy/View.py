import gi 
gi.require_version("Gtk", "3.0") 
gi.require_version("Gdk", "3.0") 
gi.require_version("GtkLayerShell", "0.1") 
from gi.repository import Gtk, Gdk, GdkPixbuf, GtkLayerShell 
import os 
import sys 
from subprocess import Popen 
luminashell = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")) 
if luminashell not in sys.path: sys.path.insert(0, luminashell) 
import config 
from Config import Config
from AudioVolume import AudioVolume

audiovolume = AudioVolume()

class View(Gtk.Window):
    def __init__(self):
        super().__init__(title="Settings")

        self.set_border_width(10)
        self.set_default_size(600, 400)
        self.set_resizable(False)
        self.set_app_paintable(True)

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

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scrolled.set_name("mainBox")
        self.add(scrolled)

        container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        scrolled.add(container)

        title = Gtk.Label(label="Settings")
        container.pack_start(title, False, False, 0)

        listbox = Gtk.ListBox()
        container.pack_start(listbox, True, True, 0)

        def create_scale_row(label_text, value, lower, upper, step):
            row = Gtk.ListBoxRow()
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
            row.add(box)

            label = Gtk.Label(label=label_text, xalign=0)
            box.pack_start(label, True, True, 0)

            adjustment = Gtk.Adjustment(value, lower, upper, step, 10, 0)
            scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjustment)
            scale.set_digits(0)
            scale.set_hexpand(True)
            box.pack_start(scale, True, True, 0)

            return row, scale  

        iconsize_row, self.iconsize_scale = create_scale_row("Icon Size", 64, 1, 128, 1)
        audiovolume_row, self.audiovolume_scale = create_scale_row("Audio Volume", audiovolume.get_volume(), 0, 100, 1)

        listbox.add(iconsize_row)
        listbox.add(audiovolume_row)

        self.apply_button = Gtk.Button(label="Apply")
        self.apply_button.set_hexpand(True)
        container.pack_start(self.apply_button, False, False, 0)

        self.show_all()


win = View()
win.connect("destroy", Gtk.main_quit)
Gtk.main()