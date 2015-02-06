Summary:	A Linux Desktop similar to GNOME2 based on gnome-shell technology
Name:		cinnamon
Version:	1.6.7
Release:	2
License:	GPLv2+
Url:		https://github.com/linuxmint/Cinnamon/tags
Group:		Graphical desktop/GNOME
Source0:	%{name}-%{version}.tar.gz
# -- PATCH-FIX-OPENSUSE cinnamon-fix-session-file.patch nmarques@opensuse.org
#    easy fix: we have 'gnome-session-check-accelerated' in _libexecdir
#Patch0:	cinnamon-fix-session-file.patch

BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	pkgconfig(clutter-glx-1.0)
BuildRequires:	pkgconfig(clutter-x11-1.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(folks)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gjs-internals-1.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gnome-bluetooth-1.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-base-0.10)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libcroco-0.6)
BuildRequires:	pkgconfig(libgnome-menu-3.0)
BuildRequires:	pkgconfig(libedataserverui-3.0)
BuildRequires:	pkgconfig(libmuffin)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(telepathy-logger-0.2)

Suggests:	%{name}-browser-plugins = %{version}
Requires:	gnome-session
Requires:	muffin
# -- used by cinnamon-settings
Requires:	gnome-python-gconf

%description
Cinnamon is a Linux Desktop which provides advanced innovative features
and a traditional user experience.
The underlying technology is forked from gnome-shell and the Desktop
layout is similar to GNOME2. The emphasis is put on making users feel
at home and providing them with an easy to use and confortable Desktop
experience.

%package browser-plugins
Summary:	Browser plugins for the Cinnamon Desktop
Group:		Graphical desktop/GNOME

%description browser-plugins
Cinnamon is a Linux Desktop which provides advanced innovative features
and a traditional user experience.

This package provides the browser plugins for Cinnamon.

%prep
%setup -qn Cinnamon-%{version}
%apply_patches

# true debian style /usr/lib is hardcoded
sed -i -e 's|/usr/lib|%{_datadir}|g' \
	files/generate_desktop_files \
	files/usr/share/gnome-session/sessions/cinnamon.session \
	files/usr/lib/cinnamon-settings/cinnamon-settings.py \
	files/usr/lib/cinnamon-menu-editor/Alacarte/config.py \
	files/usr/lib/cinnamon-menu-editor/Alacarte/MainWindow.py \
	files/usr/bin/cinnamon-settings \
	files/usr/bin/cinnamon-menu-editor

%build
export BROWSER_PLUGIN_DIR=%{_libdir}/browser-plugins
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--enable-compile-warnings=yes \
	--disable-static \
	--disable-rpath \
	--enable-introspection=yes \
	--with-ca-certificates=%{_sysconfdir}/ssl/ca-bundle.pem

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std
find %{buildroot}%{_libdir} -type f -name "*.la" -delete -print
%find_lang %{name}

# hmmm
rm -f %{buildroot}%{_datadir}/gnome-session/sessions/cinnamon.session.0000~

# MD
mv %{buildroot}/%{_prefix}/lib/cinnamon-menu-editor \
	%{buildroot}/%{_prefix}/lib/cinnamon-settings \
	%{buildroot}%{_datadir}	

%files -f %{name}.lang
%doc COPYING README
%config %{_sysconfdir}/xdg/menus/cinnamon-applications.menu
%config %{_sysconfdir}/xdg/menus/cinnamon-settings.menu
%{_bindir}/cinnamon
%{_bindir}/cinnamon2d
%{_bindir}/cinnamon-launcher
%{_bindir}/cinnamon-extension-tool
%{_bindir}/cinnamon-menu-editor
%{_bindir}/cinnamon-settings
%{_bindir}/gnome-session-cinnamon
%{_bindir}/gnome-session-cinnamon2d
%{_libdir}/cinnamon/
%{_datadir}/cinnamon/applets
%{_datadir}/cinnamon/js
%{_datadir}/cinnamon/search_providers
%{_datadir}/cinnamon/shaders
%{_datadir}/cinnamon/theme
%{_datadir}/cinnamon-menu-editor/
%{_datadir}/cinnamon-settings/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/desktop-*
%{_datadir}/glib-2.0/schemas/org.cinnamon.gschema.xml
%{_datadir}/gnome-session/sessions/cinnamon.session
%{_datadir}/gnome-session/sessions/cinnamon2d.session
%{_datadir}/xsessions/cinnamon.desktop
%{_datadir}/xsessions/cinnamon2d.desktop
%{_mandir}/man1/*

%files browser-plugins
%{_libdir}/browser-plugins/*.so

