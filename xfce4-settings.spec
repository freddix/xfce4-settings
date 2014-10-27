%define		xfce_version	4.11.0

Summary:	Xfce settings
Name:		xfce4-settings
Version:	4.11.3
Release:	2
License:	GPL v2, LGPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/xfce/xfce4-settings/4.11/%{name}-%{version}.tar.bz2
# Source0-md5:	dfd78eb223607a2b37e3863da2b923fd
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	exo-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4kbd-devel >= %{xfce_version}
BuildRequires:	libxfce4ui-devel >= %{xfce_version}
BuildRequires:	libxklavier-devel
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	startup-notification-devel
BuildRequires:	xfce4-dev-tools >= %{xfce_version}
BuildRequires:	xfconf-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	libxfce4kbd >= %{xfce_version}
Requires:	xfconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce desktop environment settings.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules		\
	--enable-pluggable-dialogs	\
	--enable-sound-settings
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/xfce4/settings
%attr(755,root,root) %{_libdir}/xfce4/settings/appearance-install-theme
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/devices/*.png
%{_sysconfdir}/xdg/autostart/*.desktop
%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%{_sysconfdir}/xdg/menus/xfce-settings-manager.menu

