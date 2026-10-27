#!/usr/bin/env python3
import sys
from urllib.parse import urlparse

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

from Model import WebAppModel
from View import AppController, MainWindow

def main(argv):
    if len(argv) < 2:
        print("Incorrect usage")
        return 2
    url = argv[1]
    if not urlparse(url).scheme:
        url = "https://" + url

    application = Gtk.Application(application_id="com.9os.webappframework")
    session = {}

    def on_activate(app):
        if "view" in session:
            session["view"].present()
            return
        view = MainWindow(app)
        session["view"] = view
        session["controller"] = AppController(WebAppModel(url), view)
        session["controller"].start()

    application.connect("activate", on_activate)
    return application.run([argv[0]])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
