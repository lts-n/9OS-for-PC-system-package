import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from Model import Model 

class View(Gtk.Window):
    def __init__(self):
        super().__init__(title="Clock App")
        self.set_border_width(10)
        self.set_default_size(200, 150)

        self.set_app_paintable(True)
        self.set_resizable(False)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_path("css/transparentStylesheet.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.box)
        self.box.set_name("mainBox")

        self.timelabel = Gtk.Label(label="00:00:00")
        self.timelabel.set_name("time-label")
        self.box.pack_start(self.timelabel, True, True, 0)

        self.datelabel = Gtk.Label(label="YYYY-MM-DD")
        self.datelabel.set_name("date-label")
        self.box.pack_start(self.datelabel, True, True, 0)

        self.showtimer_button = Gtk.Button(label="Timer")
        self.showtimer_button.set_name("timer-button")
        self.box.pack_start(self.showtimer_button, True, True, 0)

        self.show_all()




