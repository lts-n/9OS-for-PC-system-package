import gi
gi.require_version("Gtk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
from gi.repository import Gtk, GtkLayerShell, Gdk
from DockView import DockView

class DockWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Application Dock")

        GtkLayerShell.init_for_window(self)

        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.TOP)

        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.BOTTOM, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)

        GtkLayerShell.set_exclusive_zone(self, True)

        self.set_decorated(False)
        self.set_resizable(False)

        style_provider = Gtk.CssProvider()
        style_provider.load_from_path("css/dockwindowStylesheet.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        self.add(DockView())
        
win = DockWindow()
win.show_all()