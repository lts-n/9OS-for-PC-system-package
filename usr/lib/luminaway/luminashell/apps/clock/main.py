from View import View
from Model import Model
from Controller import Controller
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def main():
    model = Model()
    view = View()
    controller = Controller(view, model)
    view.connect("destroy", Gtk.main_quit)
    Gtk.main()

if __name__ == "__main__":
    main()