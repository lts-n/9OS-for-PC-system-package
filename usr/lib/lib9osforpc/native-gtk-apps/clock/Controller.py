import sys
import os

luminashell = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if luminashell not in sys.path:
    sys.path.insert(0, luminashell)

from NotificationView import NotificationView
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.showtimer_button.connect("clicked", self.on_timer_button_clicked)

        GLib.timeout_add(1000, self.update_clock)

        self.timer_id = None  

    def update_clock(self):
        current_time = self.model.get_current_time()
        current_date = self.model.get_current_date()
        self.view.timelabel.set_text(current_time)
        self.view.datelabel.set_text(current_date)
        return True

    def on_timer_button_clicked(self, button):
        dialog = Gtk.Dialog(title="Set Timer", parent=self.view, flags=0)
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        )

        box = dialog.get_content_area()
        box.set_spacing(10)

        self.hours_entry = Gtk.SpinButton()
        self.hours_entry.set_range(0, 99)
        self.hours_entry.set_value(0)
        self.hours_entry.set_increments(1, 10)
        self.hours_entry.set_numeric(True)

        self.minutes_entry = Gtk.SpinButton()
        self.minutes_entry.set_range(0, 59)
        self.minutes_entry.set_value(0)
        self.minutes_entry.set_increments(1, 10)
        self.minutes_entry.set_numeric(True)

        self.seconds_entry = Gtk.SpinButton()
        self.seconds_entry.set_range(0, 59)
        self.seconds_entry.set_value(0)
        self.seconds_entry.set_increments(1, 10)
        self.seconds_entry.set_numeric(True)

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        hbox.pack_start(Gtk.Label(label="Hours:"), False, False, 0)
        hbox.pack_start(self.hours_entry, False, False, 0)
        hbox.pack_start(Gtk.Label(label="Minutes:"), False, False, 0)
        hbox.pack_start(self.minutes_entry, False, False, 0)
        hbox.pack_start(Gtk.Label(label="Seconds:"), False, False, 0)
        hbox.pack_start(self.seconds_entry, False, False, 0)

        box.add(hbox)
        dialog.show_all()

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            hours = self.hours_entry.get_value_as_int()
            minutes = self.minutes_entry.get_value_as_int()
            seconds = self.seconds_entry.get_value_as_int()
            total_seconds = hours * 3600 + minutes * 60 + seconds
            if total_seconds > 0:
                self.start_timer(total_seconds)
        dialog.destroy()

    def start_timer(self, total_seconds):
        if self.timer_id:
            GLib.source_remove(self.timer_id)  
        def countdown():
            nonlocal total_seconds
            if total_seconds <= 0:
                self.view.timelabel.set_text("Time's up!")
                notification = NotificationView("Timer's up!")
                self.timer_id = None
                return False  
            else:
                h = total_seconds // 3600
                m = (total_seconds % 3600) // 60
                s = total_seconds % 60
                self.view.timelabel.set_text(f"{h:02}:{m:02}:{s:02}")
                total_seconds -= 1
                return True  

        self.timer_id = GLib.timeout_add(1000, countdown)
