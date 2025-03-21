Name:           cinnamon
Version:        6.4.8
Release:        1
Summary:        Window management and application launching for Cinnamon

Group:          Graphical desktop/Cinnamon
# cinnamon-menu-editor is LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            https://cinnamon.linuxmint.com

Source0:        https://github.com/linuxmint/cinnamon/archive/%{version}/%{name}-%{version}.tar.gz
Source3:        polkit-cinnamon-authentication-agent-1.desktop
# fix power applet using version by robin92
# https://github.com/linuxmint/Cinnamon/issues/3068
#Source7:        power-applet.js
#Patch0:         background.patch
# from fedora
Patch1:         autostart.patch
#Patch1:		webkit_dep.patch

%global gobject_introspection_version 0.10.1
%global muffin_version 6.0.0
%global eds_version 2.91.6
%global json_glib_version 0.13.2
%global polkit_version 0.100

BuildRequires: meson
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:	pkgconfig(libnm)
BuildRequires: pkgconfig(polkit-agent-1) >= %{polkit_version}
BuildRequires: pkgconfig(gudev-1.0)
# for screencast recorder functionality
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: intltool
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libcroco-0.6) >= 0.6.2
BuildRequires: pkgconfig(gnome-keyring-1)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(upower-glib)
# for barriers
BuildRequires: pkgconfig(xfixes) >= 5.0
# used in unused BigThemeImage
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: librsvg2-devel
BuildRequires: pkgconfig(libmuffin-0) >= %{muffin_version}
BuildRequires: pulseaudio-devel
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(gstreamer-1.0)
# Bootstrap requirements
BuildRequires: gtk-doc 
BuildRequires: gnome-common
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libwacom)
BuildRequires: pkgconfig(xorg-wacom)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gdk-x11-3.0)
BuildRequires: pkgconfig(gcr-base-3)
BuildRequires: pkgconfig(cjs-1.0)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(cinnamon-desktop) >= 2.0.4
BuildRequires: pkgconfig(libcinnamon-menu-3.0)
BuildRequires: pkgconfig(libgnome-menu-3.0)
#BuildRequires: pkgconfig(mozjs-102)
BuildRequires: egl-devel
BuildRequires: ca-certificates
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(xapp)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(colord)

BuildRequires: typelib(CDesktopEnums)
BuildRequires: python-libsass

#required for applet fix
BuildRequires: patchelf
BuildRequires: chrpath

Recommends:     touchegg

Requires:       accountsservice
Requires:       cinnamon-menus
Requires:       gnome-menus
# wrapper script uses to restart old GNOME session if run --replace
# from the command line
Requires:       gobject-introspection >= %{gobject_introspection_version}
Requires:       gnome-terminal
Requires:       gnome-backgrounds
# needed as it is now split from Clutter
Requires:       json-glib >= %{json_glib_version}
# might be still be needed.
Requires:       muffin >= %{muffin_version}
# Get upower 1.0 api changes
Requires:       upower >= 0.99.0
Requires:       polkit >= 0.100
# needed for session files
# cinnamon-session version fixes location of helper app
Requires:       cinnamon-session
# needed for schemas
Requires:       at-spi2-atk
# needed for on-screen keyboard
Requires:       caribou
# needed for settings
Requires:	      python-cairo
Requires:       python-gi
Requires:       python-dbus
Requires:       python-distro
Requires:       python-gobject3
Requires:       python-lxml
Requires:       python-imaging
Requires:       python-pam
Requires:       python-pexpect
Requires:       python-pytz
Requires:       python-pillow
Requires:       python-requests
Requires:       python-tinycss2
# In unsupported repo
Requires:       python-setproctitle
Requires:       python-xapp
Requires:       python-libsass

# Not yet compiled
#Requires:       mintlocale
#Requires:       google-noto-sans-fonts

Requires:       %{name}-desktop
Requires:       cinnamon-control-center
Requires:       cinnamon-screensaver
Requires:       cinnamon-translations
# fix cinnamon startup crashes
Requires:       typelib(fontconfig)
Requires:       typelib(Soup)
Requires:       typelib(Rsvg)
Requires:	      typelib(xfixes)
Requires:       typelib(TimezoneMap)
Requires:       nemo
Requires:       gsound
Requires:       xapp
Requires:       gnome-backgrounds
Requires:       metacity
Requires:       tint2

# include cjs introspection
Requires:       cjs
# Mate polkit
Requires:       mate-polkit
# requires for keyboard applet
Requires:       gucharmap

# required for network applet
Requires:       networkmanager-applet
#needed for cinnamon-looking-glass
Requires:       python-pyinotify
#needed for cinnamon-json-makepot
Requires:       python-polib

Requires:       wget
Requires:       cups-common
Requires:       gettext
Requires:	typelib(Keybinder) = 3.0
Requires:	libgnomekbd-common

#Few optional app to meet the minimum operational requirements of the environment
Recommends: blueberry
Recommends: pix
Recommends: xed
Recommends: xviewer
Recommends: xreader
Recommends: xplayer

#Recommends: om-mirror-selector


# cinnamon handles notifications natively, no notification-daemon needed
Provides:       virtual-notification-daemon
# and ditto for polkit authorisation dialogs
Provides:       polkit-agent
Provides:       task-cinnamon

%description
Cinnamon is a Linux desktop which provides advanced
 innovative features and a traditional user experience.

The desktop layout is similar to Gnome 2. 
The underlying technology is forked from Gnome Shell.
The emphasis is put on making users feel at home and providing
 them with an easy to use and comfortable desktop experience.

%prep
%setup -q -n cinnamon-%{version}
%autopatch -p1


sed -i -e 's!imports.gi.NMClient!imports_gi_NMClient!g' js/ui/extension.js

# https://github.com/linuxmint/cinnamon/issues/3575#issuecomment-374887122
# Cinnamon has no upstream backgrounds, use GNOME backgrounds instead
sed -i 's|/usr/share/cinnamon-background-properties|/usr/share/gnome-background-properties|' \
    files/usr/share/cinnamon/cinnamon-settings/modules/cs_backgrounds.py


%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=deprecated-declarations"

%meson

%meson_build

%install
%meson_install

# Remove .la file
rm -rf %{buildroot}/%{_libdir}/cinnamon/libcinnamon.la

# install polkik autostart desktop file
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/applications/

desktop-file-validate %{buildroot}%{_datadir}/applications/cinnamon.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/cinnamon2d.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/polkit-cinnamon-authentication-agent-1.desktop

desktop-file-install                                 \
 --add-category="Utility"                            \
 --remove-category="DesktopSettings"                 \
 --remove-key="Encoding"                             \
 --add-only-show-in="GNOME"                          \
 --delete-original                                   \
 --dir=%{buildroot}%{_datadir}/applications       \
 %{buildroot}%{_datadir}/applications/*

# fix rpath for CinnamonJS
# see http://bugzilla.opensuse.org/show_bug.cgi?id=904414
#chrpath -d %{buildroot}%{_bindir}/cinnamon
#patchelf --force-rpath --set-rpath %{_libdir}/cinnamon:%{_libdir}/muffin %{buildroot}%{_bindir}/cinnamon
#chrpath -l %{buildroot}%{_bindir}/cinnamon


%files
%doc COPYING README.rst
%{_bindir}/*
%{_datadir}/desktop-directories/cinnamon-*.directory
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*
%{_datadir}/wayland-sessions/cinnamon-wayland.desktop
#{_datadir}/xdg-desktop-portal/x-cinnamon-portals.conf
%{_iconsdir}/hicolor/*/*/*.svg
%{_iconsdir}/hicolor/*x*/actions/cinnamon-hc*
%{_datadir}/polkit-1/actions/org.cinnamon.settings-users.policy
%{_datadir}/cinnamon/
%{_datadir}/cinnamon-*/
%{_datadir}/dbus-1/services/org.cinnamon.CalendarServer.service
%{_datadir}/dbus-1/services/org.Cinnamon.*.service
%{_datadir}/xdg-desktop-portal/x-cinnamon-portals.conf
%{_datadir}/xsessions/*
%{_libdir}/cinnamon/
#{_libexecdir}/cinnamon/
%{_libexecdir}/cinnamon-hotplug-sniffer
%{_libexecdir}/cinnamon-perf-helper
%{_libexecdir}/cinnamon-calendar-server.py
%{python_sitelib}/cinnamon/
%{_mandir}/man1/*.1.*
#{_datadir}/gir-1.0/Cinnamon-0.1.gir
#{_datadir}/gir-1.0/St-1.0.gir
%{_sysconfdir}/xdg/menus/cinnamon-applications-merged
%{_sysconfdir}/xdg/menus/cinnamon-applications.menu
