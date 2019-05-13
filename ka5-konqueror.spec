%define		kdeappsver	19.04.1
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		konqueror
Summary:	konqueror
Name:		ka5-%{kaname}
Version:	19.04.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	812da7884e0b92f45c1ee16c7d86fcf6
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Positioning-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5WebChannel-devel >= 5.11.1
BuildRequires:	Qt5WebEngine-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kbookmarks-devel >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdelibs4support-devel >= %{kframever}
BuildRequires:	kf5-khtml-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	tidy-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konqueror is KDE's Webbrowser and swiss-army-knife for any kind of
file-management and file previewing.. Features. Webbrowsing using
KHTML or KDEWebKit as rendering engines; File management using most of
Dolphin's features (including version-control, service menus and the
basic UI)

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{el,sr}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/akregatorplugin.categories
/etc/xdg/autostart/konqy_preload.desktop
/etc/xdg/konqueror.categories
/etc/xdg/translaterc
%attr(755,root,root) %{_bindir}/fsview
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_libdir}/libKF5Konq.so.5.*.*
%attr(755,root,root) %{_libdir}/libKF5Konq.so.6
%attr(755,root,root) %{_libdir}/libkdeinit5_kfmclient.so
%attr(755,root,root) %{_libdir}/libkdeinit5_konqueror.so
%attr(755,root,root) %ghost %{_libdir}/libkonquerorprivate.so.5
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so.5.*.*
%attr(755,root,root) %{_libdir}/libkwebenginepart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregatorkonqfeedicon.so
%attr(755,root,root) %{_libdir}/qt5/plugins/autorefresh.so
%attr(755,root,root) %{_libdir}/qt5/plugins/babelfishplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/dirfilterplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/domtreeviewerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/fsviewpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_bookmarks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_konq.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_konqhtml.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_performance.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kfileitemaction/akregatorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/webenginepart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtmlsettingsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtmlttsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kimgallery.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konq_aboutpage.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konq_shellcmdplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/minitoolsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/rellinksplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/searchbarplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/validatorsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webarchiverplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webarchivethumbnail.so
# TODO proper package
%dir %{_datadir}/akregator/pics
%{_datadir}/akregator/pics/feed.png
%{_desktopdir}/kfmclient.desktop
%{_desktopdir}/kfmclient_dir.desktop
%{_desktopdir}/kfmclient_html.desktop
%{_desktopdir}/kfmclient_war.desktop
%{_desktopdir}/konqbrowser.desktop
%{_datadir}/config.kcfg/konqueror.kcfg
%{_datadir}/config.kcfg/validators.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.Main.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.MainWindow.xml
%dir %{_datadir}/dolphinpart
%dir %{_datadir}/dolphinpart/kpartplugins
%{_datadir}/dolphinpart/kpartplugins/dirfilterplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/dirfilterplugin.rc
%{_datadir}/dolphinpart/kpartplugins/kimgalleryplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/kimgalleryplugin.rc
%{_datadir}/dolphinpart/kpartplugins/kshellcmdplugin.desktop
%{_datadir}/dolphinpart/kpartplugins/kshellcmdplugin.rc
%dir %{_datadir}/domtreeviewer
%{_datadir}/domtreeviewer/domtreeviewerui.rc
%dir %{_datadir}/fsview
%{_datadir}/fsview/fsview_part.rc
%{_iconsdir}/hicolor/128x128/apps/konqueror.png
%{_iconsdir}/hicolor/128x128/apps/webengine.png
%{_iconsdir}/hicolor/16x16/actions/babelfish.png
%{_iconsdir}/hicolor/16x16/actions/cssvalidator.png
%{_iconsdir}/hicolor/16x16/actions/htmlvalidator.png
%{_iconsdir}/hicolor/16x16/actions/imagegallery.png
%{_iconsdir}/hicolor/16x16/actions/validators.png
%{_iconsdir}/hicolor/16x16/actions/webarchiver.png
%{_iconsdir}/hicolor/16x16/apps/konqueror.png
%{_iconsdir}/hicolor/16x16/apps/webengine.png
%{_iconsdir}/hicolor/22x22/actions/babelfish.png
%{_iconsdir}/hicolor/22x22/actions/cssvalidator.png
%{_iconsdir}/hicolor/22x22/actions/htmlvalidator.png
%{_iconsdir}/hicolor/22x22/actions/imagegallery.png
%{_iconsdir}/hicolor/22x22/actions/validators.png
%{_iconsdir}/hicolor/22x22/actions/webarchiver.png
%{_iconsdir}/hicolor/22x22/apps/fsview.png
%{_iconsdir}/hicolor/22x22/apps/konqueror.png
%{_iconsdir}/hicolor/22x22/apps/webengine.png
%{_iconsdir}/hicolor/32x32/actions/htmlvalidator.png
%{_iconsdir}/hicolor/32x32/actions/validators.png
%{_iconsdir}/hicolor/32x32/apps/fsview.png
%{_iconsdir}/hicolor/32x32/apps/konqueror.png
%{_iconsdir}/hicolor/32x32/apps/webengine.png
%{_iconsdir}/hicolor/48x48/actions/htmlvalidator.png
%{_iconsdir}/hicolor/48x48/actions/validators.png
%{_iconsdir}/hicolor/48x48/apps/konqueror.png
%{_iconsdir}/hicolor/48x48/apps/webengine.png
%{_iconsdir}/hicolor/64x64/actions/htmlvalidator.png
%{_iconsdir}/hicolor/64x64/actions/validators.png
%{_iconsdir}/hicolor/64x64/apps/konqueror.png
%{_iconsdir}/hicolor/64x64/apps/webengine.png
%{_iconsdir}/hicolor/scalable/actions/htmlvalidator.svgz
%{_iconsdir}/hicolor/scalable/actions/validators.svgz
%dir %{_datadir}/kcmcss
%{_datadir}/kcmcss/template.css
%{_datadir}/kcontrol/pics/onlyone.png
%{_datadir}/kcontrol/pics/overlapping.png
%dir %{_datadir}/kf5/kbookmark
%{_datadir}/kf5/kbookmark/directory_bookmarkbar.desktop
%{_datadir}/khtml
%{_datadir}/konqueror
%{_datadir}/kservices5/akregator_konqplugin.desktop
%{_datadir}/kservices5/bookmarks.desktop
%{_datadir}/kservices5/filebehavior.desktop
%{_datadir}/kservices5/fsview_part.desktop
%{_datadir}/kservices5/kcmkonqyperformance.desktop
%{_datadir}/kservices5/kcmperformance.desktop
%{_datadir}/kservices5/khtml_appearance.desktop
%{_datadir}/kservices5/khtml_behavior.desktop
%{_datadir}/kservices5/khtml_filter.desktop
%{_datadir}/kservices5/khtml_general.desktop
%{_datadir}/kservices5/khtml_java_js.desktop
%{_datadir}/kservices5/konq_aboutpage.desktop
%{_datadir}/kservices5/org.kde.konqueror.desktop
%{_datadir}/kservices5/webarchivethumbnail.desktop
%{_datadir}/kservices5/webenginepart.desktop
%{_datadir}/kservicetypes5/konqaboutpage.desktop
%{_datadir}/kwebkitpart
%dir %{_datadir}/kxmlgui5/webenginepart
%{_datadir}/kxmlgui5/webenginepart/webenginepart.rc
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%dir %{_datadir}/webenginepart
%{_datadir}/webenginepart/error.html
%dir %{_datadir}/webenginepart/kpartplugins
%{_datadir}/webenginepart/kpartplugins/akregator_konqfeedicon.desktop
%{_datadir}/webenginepart/kpartplugins/akregator_konqfeedicon.rc
%{_datadir}/webenginepart/kpartplugins/autorefresh.desktop
%{_datadir}/webenginepart/kpartplugins/autorefresh.rc
%{_datadir}/webenginepart/kpartplugins/khtmlsettingsplugin.desktop
%{_datadir}/webenginepart/kpartplugins/khtmlsettingsplugin.rc
%{_datadir}/webenginepart/kpartplugins/khtmltts.desktop
%{_datadir}/webenginepart/kpartplugins/khtmltts.rc
%{_datadir}/webenginepart/kpartplugins/plugin_babelfish.rc
%{_datadir}/webenginepart/kpartplugins/plugin_translator.desktop
%{_datadir}/webenginepart/kpartplugins/plugin_validators.desktop
%{_datadir}/webenginepart/kpartplugins/plugin_validators.rc

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/konq_events.h
%{_includedir}/KF5/konq_historyentry.h
%{_includedir}/KF5/konq_historyprovider.h
%{_includedir}/KF5/konq_popupmenu.h
%{_includedir}/KF5/konq_version.h
%{_includedir}/KF5/libkonq_export.h
%{_libdir}/cmake/KF5Konq
%attr(755,root,root) %{_libdir}/libKF5Konq.so
