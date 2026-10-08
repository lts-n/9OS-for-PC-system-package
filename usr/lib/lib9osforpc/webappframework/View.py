import html

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.1")

from gi.repository import GLib, Gtk, WebKit2

ERROR_PAGE = """<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><title>Error</title>
<style>
  body { font-family: system-ui, sans-serif; text-align: center; padding-top: 15vh; color: #1c1c1e; }
  p { color: #6c6c70; word-break: break-all; }
  button { padding: .6em 1.4em; font-size: 1em; border: 0; border-radius: 8px;
           color: #fff; background: #0a84ff; cursor: pointer; }
</style>
</head>
<body>
  <h1>No se pudo cargar la pagina</h1>
  <p>__URL__</p>
  <p>__MESSAGE__</p>
  <button onclick="location.reload()">Reintentar</button>
</body>
</html>"""


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, application):
        super().__init__(application=application, default_width=1280, default_height=800)
        self.webview = WebKit2.WebView()
        self.add(self.webview)

    def render(self, model):
        self.set_title(model.window_title)

    def show_error(self, url, message):
        page = ERROR_PAGE.replace("__URL__", html.escape(url or ""))
        page = page.replace("__MESSAGE__", html.escape(message or ""))
        self.webview.load_html(page, "about:blank")


class AppController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        webview = view.webview
        webview.connect("load-changed", self.on_load_changed)
        webview.connect("notify::title", self.on_title_changed)
        webview.connect("load-failed", self.on_load_failed)
        webview.connect("create", self.on_create)

    def start(self):
        self.view.show_all()
        self.view.render(self.model)
        self.view.webview.load_uri(self.model.url)

    def on_load_changed(self, webview, event):
        self.model.loading = event != WebKit2.LoadEvent.FINISHED
        if webview.get_uri():
            self.model.url = webview.get_uri()
        self.view.render(self.model)

    def on_title_changed(self, webview, param):
        self.model.title = webview.get_title() or ""
        self.view.render(self.model)

    def on_load_failed(self, webview, event, url, error):
        if error.matches(GLib.io_error_quark(), GLib.IOErrorEnum.CANCELLED):
            return False
        self.model.loading = False
        self.model.title = ""
        self.view.render(self.model)
        self.view.show_error(url, error.message)
        return True

    def on_create(self, webview, navigation_action):
        uri = navigation_action.get_request().get_uri()
        if uri:
            webview.load_uri(uri)
        return None
