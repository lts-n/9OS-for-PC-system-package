import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GtkLayerShell, GLib
from Screen import Screen
from time import sleep

screen_object = Screen(0)

class NotificationView(Gtk.Window):
    def __init__(self, notification_text):
        super().__init__(title="Notification")

        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.OVERLAY)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.RIGHT, True)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.LEFT, False)

        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.TOP, 20)
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.RIGHT, 20)

        self.set_size_request(-1, -1)

        self.set_decorated(False)
        self.set_resizable(False)
        self.set_app_paintable(True)

        style_provider = Gtk.CssProvider()
        style_provider.load_from_path("css/notificationStylesheet.css")
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        box.set_name("notification-box")
        self.add(box)

        label = Gtk.Label(label=notification_text)
        label.set_halign(Gtk.Align.CENTER)  
        label.set_valign(Gtk.Align.CENTER)
        label.set_name("notification-label")
        box.pack_start(label, True, True, 0)
        box.set_halign(Gtk.Align.CENTER)
        box.set_valign(Gtk.Align.CENTER)

        self.show_all()

        GLib.timeout_add(5000, self.destroy)

        Gtk.main()
        