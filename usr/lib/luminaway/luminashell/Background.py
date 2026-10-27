import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, Gdk, GtkLayerShell
from Screen import Screen

screen_object = Screen(0)

class Background(Gtk.Window):
    def __init__(self):
        super().__init__(title="focus_disabled_window")

        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.BACKGROUND)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)

        self.set_default_size(screen_object.width(), screen_object.height())

        self.set_decorated(False)
        self.set_resizable(False)

        style_provider = Gtk.CssProvider()
        style_provider.load_from_path("css/backgroundStylesheet.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

win = Background()
win.show_all()