if [ -z "${WAYLAND_DISPLAY:-}" ] && [ -z "${DISPLAY:-}" ] && [ "${USER:-}" != "root" ]; then
    if [ "$(tty 2>/dev/null)" = "/dev/tty1" ]; then
        exec luminaway
    fi
fi
