from Background import Background
from DockWindow import DockWindow
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def main():
    bg = Background()
    bg.show_all()

    dock = DockWindow()
    dock.show_all()

    Gtk.main()

if __name__ == "__main__":
    main()