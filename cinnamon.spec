Name:           cinnamon
Version:        4.0.9
Release: 1
Summary:        Window management and application launching for Cinnamon

Group:          Graphical desktop/Cinnamon
# cinnamon-menu-editor is LGPLv2+
License:        GPLv2+ and LGPLv2+
URL:            http://cinnamon.linuxmint.com
# To generate tarball

Source0:        Cinnamon-%{version}.tar.gz
Source3:        polkit-cinnamon-authentication-agent-1.desktop
# fix power applet using version by robin92
# https://github.com/linuxmint/Cinnamon/issues/3068
#Source7:        power-applet.js

# from fedora
#Patch0:         background.patch
#Patch1:         autostart.patch
Patch1:		webkit_dep.patch
%global clutter_version 1.7.5
%global gobject_introspection_version 0.10.1
%global muffin_version 1.9.1
%global eds_version 2.91.6
%global json_glib_version 0.13.2
%global polkit_version 0.100

BuildRequires:  pkgconfig(clutter-x11-1.0) >= %{clutter_version}
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:	pkgconfig(libnm)
BuildRequires:  pkgconfig(libnm-glib)
BuildRequires:  pkgconfig(libnm-util)
BuildRequires:  pkgconfig(polkit-agent-1) >= %{polkit_version}
BuildRequires:  pkgconfig(gudev-1.0)
# for screencast recorder functionality
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  intltool
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcroco-0.6) >= 0.6.2
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libnm-glib-vpn)
BuildRequires:  pkgconfig(libstartup-notification-1.0)

# for barriers
BuildRequires:  pkgconfig(xfixes) >= 5.0
# used in unused BigThemeImage
BuildRequires:  librsvg2-devel
BuildRequires:  pkgconfig(libmuffin) >= %{muffin_version}
BuildRequires:  pulseaudio-devel
# Bootstrap requirements
BuildRequires: gtk-doc 
BuildRequires: gnome-common

BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(xorg-wacom)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(cjs-internals-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(cinnamon-desktop) >= 2.0.4
BuildRequires:  pkgconfig(libcinnamon-menu-3.0)

#required for applet fix
BuildRequires:  patchelf
BuildRequires:  chrpath

Requires:       cinnamon-menus
# wrapper script uses to restart old GNOME session if run --replace
# from the command line
Requires:       gobject-introspection >= %{gobject_introspection_version}
Requires:	gnome-terminal
# needed for loading SVG's via gdk-pixbuf
#Requires:       librsvg2%{?_isa}
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
Requires:	python-cairo
Requires:       python-gi
Requires:       python-dbus
Requires:       python-lxml
Requires:       python-imaging
Requires:       python-pam
Requires:       python-pexpect
Requires:       python-pillow
Requires:	python2-imaging
Requires:	python2-gi
Requires:       cinnamon-control-center
Requires:       cinnamon-screensaver
Requires:       cinnamon-translations
# fix 10916
Requires:       gnome-themes-standard
# fix cinnamon startup crashes
Requires:       typelib(fontconfig)
Requires:       nemo

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

Requires:	typelib(Keybinder) = 3.0
Requires:	libgnomekbd-common

# cinnamon handles notifications natively, no notification-daemon needed
Provides:       virtual-notification-daemon
# and ditto for polkit authorisation dialogs
Provides:       polkit-agent

%description
Cinnamon is a Linux desktop which provides advanced
 innovative features and a traditional user experience.

The desktop layout is similar to Gnome 2. 
The underlying technology is forked from Gnome Shell.
The emphasis is put on making users feel at home and providing
 them with an easy to use and comfortable desktop experience.

%prep
%setup -q -n Cinnamon-%{version}
%apply_patches

# have cinnamon use mageia app system
grep -r -l cinnamon-applications.menu files%{_datadir} files%{_bindir}  src | \
xargs sed -i -e 's@cinnamon-applications@applications@g' 

# files replaced with mageia files
rm -rf files%{_sysconfdir}/xdg
rm -f files%{_datadir}/desktop-directories/cinnamon-{menu-applications,utility,utility-accessibility,development,education,game,graphics,network,audio-video,office,system-tools,other}.directory

rm -f configure
rm -rf debian/

NOCONFIGURE=1 ./autogen.sh

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=deprecated-declarations"

%configure2_5x \
--disable-static \
--disable-rpath \
--enable-compile-warnings=yes \
--enable-introspection=yes
%make V=1

%install
%makeinstall_std

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
chrpath -d %{buildroot}%{_bindir}/cinnamon
patchelf --force-rpath --set-rpath %{_libdir}/cinnamon %{buildroot}%{_bindir}/cinnamon
chrpath -l %{buildroot}%{_bindir}/cinnamon


%find_lang %{name} || touch %{name}.lang

%files -f %{name}.lang
%doc COPYING README.rst
%{_bindir}/*
%{_datadir}/desktop-directories/cinnamon-*.directory
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/*/*/*.svg
%{_datadir}/polkit-1/actions/org.cinnamon.settings-users.policy
%{_datadir}/cinnamon/
%{_datadir}/cinnamon-*/
%{_datadir}/gtk-doc/html/cinnamon*
%{_datadir}/dbus-1/services/org.Cinnamon.*.service
%{_datadir}/xsessions/*
%{_libdir}/cinnamon/
%{_libexecdir}/cinnamon/
%{_mandir}/man1/*.1.*


