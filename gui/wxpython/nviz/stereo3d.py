"""
@package nviz.stereo3d

@brief The person's depth limits for the 3D view in stereo, and the shortcut to
the display settings

Stereo KWin (Sparky Stereo OS) keeps one pair of depth limits for each screen,
set in its 3D Depth settings: how far behind the screen and how far in front
of it anything may appear.  libstereo-declare hands them to the window of the
3D view in the pixels of its own picture; the view never scales them.

(C) 2026 by the GRASS Development Team

This program is free software under the GNU General Public License
(>=v2). Read the file COPYING that comes with GRASS for details.
"""

import ctypes
import ctypes.util
import errno
import subprocess

DELIVERED = 0
NOT_OFFERED = 1
NOT_DELIVERED = 2
NOT_READABLE = 3


class _Limits(ctypes.Structure):
    _fields_ = [("sunk", ctypes.c_double), ("popped", ctypes.c_double)]


_libraries = {}


def _library(name, soname):
    if name not in _libraries:
        try:
            _libraries[name] = ctypes.CDLL(soname)
        except OSError:
            _libraries[name] = None
    return _libraries[name]


def CurrentWindow():
    """The X11 display and window the current GL context draws to (the one the
    desktop sees declared), or (None, 0)"""
    gl = _library("GL", ctypes.util.find_library("GL") or "libGL.so.1")
    if gl is None:
        return None, 0
    gl.glXGetCurrentDisplay.restype = ctypes.c_void_p
    gl.glXGetCurrentDrawable.restype = ctypes.c_ulong
    return gl.glXGetCurrentDisplay(), gl.glXGetCurrentDrawable()


def ReadDepthLimits(display, window, width):
    """Read the depth limits of the window in pixels of a picture width pixels
    wide shown at that width.

    :return: (state, sunk, popped); the values are 0 unless state is DELIVERED
    """
    declare = _library("stereo-declare", "libstereo-declare.so.1")
    if declare is None or not display or not window or width <= 0:
        return NOT_READABLE, 0.0, 0.0
    function = declare.stereo_depth_x11_get_buffer_limits
    function.argtypes = [
        ctypes.c_void_p,
        ctypes.c_ulong,
        ctypes.c_double,
        ctypes.c_double,
        ctypes.POINTER(_Limits),
    ]
    function.restype = ctypes.c_int
    limits = _Limits()
    result = function(display, window, float(width), float(width), ctypes.byref(limits))
    if result == 0:
        return DELIVERED, limits.sunk, limits.popped
    if result == -errno.ENODATA:
        return NOT_DELIVERED, 0.0, 0.0
    if result == -errno.ENOTSUP:
        return NOT_OFFERED, 0.0, 0.0
    return NOT_READABLE, 0.0, 0.0


def OpenDisplaySettings():
    """Open the display settings, where each screen's 3D mode, output and eye
    order are chosen.

    :return: True if they were started
    """
    for argv in (["systemsettings", "kcm_kscreen"], ["kcmshell6", "kcm_kscreen"]):
        try:
            subprocess.Popen(argv)
        except OSError:
            continue
        return True
    return False
