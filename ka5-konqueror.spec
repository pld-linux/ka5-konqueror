#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		konqueror
Summary:	konqueror
Name:		ka5-%{kaname}
Version:	23.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	bee82a72047fda2bfbf0898c75d82a8c
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
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konqueror is KDE's Webbrowser and swiss-army-knife for any kind of
file-management and file previewing.. Features. Webbrowsing using
KHTML or KDEWebKit as rendering engines; File management using most of
Dolphin's features (including version-control, service menus and the
basic UI)

%description -l pl.UTF-8
Konqueror jest przeglądarką www KDE i szwajcarskim scyzorykiem do
każdego rodzaju zarządzania plikami i ich podglądem. Cechy:
przeglądanie www przy użyciu KHTML lub KDEWebKit jako silników
renderowania; zarządzanie plikami używając większości
możliwości Dolphina (łącznie z kontrolą wersji, menu i
podstawowym UI).


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
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{el,ko,sr,zh_CN}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/konqy_preload.desktop
/etc/xdg/translaterc
%attr(755,root,root) %{_bindir}/fsview
%attr(755,root,root) %{_bindir}/kfmclient
%attr(755,root,root) %{_bindir}/konqueror
%attr(755,root,root) %{_libdir}/libKF5Konq.so.5.*.*
%ghost %{_libdir}/libKF5Konq.so.6
%attr(755,root,root) %{_libdir}/libkdeinit5_kfmclient.so
%attr(755,root,root) %{_libdir}/libkdeinit5_konqueror.so
%attr(755,root,root) %{_libdir}/libkwebenginepart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/akregatorkonqfeedicon.so
%attr(755,root,root) %{_libdir}/qt5/plugins/autorefresh.so
%attr(755,root,root) %{_libdir}/qt5/plugins/babelfishplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kfileitemaction/akregatorplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/webenginepart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtmlsettingsplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtmlttsplugin.so
# TODO proper package
%dir %{_datadir}/akregator/pics
%{_datadir}/akregator/pics/feed.png
%{_desktopdir}/kfmclient.desktop
%{_desktopdir}/kfmclient_dir.desktop
%{_desktopdir}/kfmclient_html.desktop
%{_desktopdir}/kfmclient_war.desktop
%{_desktopdir}/konqbrowser.desktop
%{_datadir}/config.kcfg/konqueror.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.Main.xml
%{_datadir}/dbus-1/interfaces/org.kde.Konqueror.MainWindow.xml
%dir %{_datadir}/kcmcss
%{_datadir}/kcmcss/template.css
%dir %{_datadir}/kcontrol
%dir %{_datadir}/kcontrol/pics
%{_datadir}/kcontrol/pics/onlyone.png
%{_datadir}/kcontrol/pics/overlapping.png
%dir %{_datadir}/kf5/kbookmark
%{_datadir}/kf5/kbookmark/directory_bookmarkbar.desktop
%{_datadir}/konqueror
%{_datadir}/kservices5/fsview_part.desktop
%{_datadir}/kservices5/org.kde.konqueror.desktop
%{_datadir}/kservices5/webenginepart.desktop
%dir %{_datadir}/kxmlgui5/webenginepart
%{_datadir}/kxmlgui5/webenginepart/webenginepart.rc
%{_datadir}/metainfo/org.kde.konqueror.appdata.xml
%dir %{_datadir}/webenginepart
%{_datadir}/webenginepart/error.html
%{_datadir}/qlogging-categories5/akregatorplugin.categories
%{_datadir}/qlogging-categories5/konqueror.categories
%{_iconsdir}/hicolor/128x128/apps/konqueror.png
%{_iconsdir}/hicolor/128x128/apps/webengine.png
%{_iconsdir}/hicolor/16x16/actions/babelfish.png
%{_iconsdir}/hicolor/16x16/actions/imagegallery.png
%{_iconsdir}/hicolor/16x16/apps/konqueror.png
%{_iconsdir}/hicolor/16x16/apps/webengine.png
%{_iconsdir}/hicolor/22x22/actions/babelfish.png
%{_iconsdir}/hicolor/22x22/actions/imagegallery.png
%{_iconsdir}/hicolor/22x22/apps/fsview.png
%{_iconsdir}/hicolor/22x22/apps/konqueror.png
%{_iconsdir}/hicolor/22x22/apps/webengine.png
%{_iconsdir}/hicolor/32x32/apps/fsview.png
%{_iconsdir}/hicolor/32x32/apps/konqueror.png
%{_iconsdir}/hicolor/32x32/apps/webengine.png
%{_iconsdir}/hicolor/48x48/apps/konqueror.png
%{_iconsdir}/hicolor/48x48/apps/webengine.png
%{_iconsdir}/hicolor/64x64/apps/konqueror.png
%{_iconsdir}/hicolor/64x64/apps/webengine.png

/etc/xdg/konqsidebartngrc
%attr(755,root,root) %{_bindir}/kcreatewebarchive
%attr(755,root,root) %{_libdir}/libkonqsidebarplugin.so.*.*.*
%ghost %{_libdir}/libkonqsidebarplugin.so.5
%attr(755,root,root) %{_libdir}/libkonquerorprivate.so.*.*.*
%ghost %{_libdir}/libkonquerorprivate.so.5
%attr(755,root,root) %{_libdir}/qt5/plugins/konqsidebar_bookmarks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqsidebar_history.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqsidebar_places.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqsidebar_tree.so
%attr(755,root,root) %{_libdir}/qt5/plugins/uachangerplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webarchiverplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webarchivethumbnail.so
%{_datadir}/config.kcfg/kcreatewebarchive.kcfg
%{_iconsdir}/hicolor/16x16/actions/webarchiver.png
%{_iconsdir}/hicolor/22x22/actions/webarchiver.png
%{_datadir}/kconf_update/webenginepart.upd
%dir %{_datadir}/konqsidebartng/entries
%{_datadir}/konqsidebartng/entries/bookmarks.desktop
%{_datadir}/konqsidebartng/entries/fonts.desktop
%{_datadir}/konqsidebartng/entries/history.desktop
%{_datadir}/konqsidebartng/entries/home.desktop
%{_datadir}/konqsidebartng/entries/places.desktop
%{_datadir}/konqsidebartng/entries/remote.desktop
%{_datadir}/konqsidebartng/entries/root.desktop
%{_datadir}/konqsidebartng/entries/services.desktop
%dir %{_datadir}/konqsidebartng/plugins
%{_datadir}/konqsidebartng/plugins/konqsidebar_bookmarks.desktop
%{_datadir}/konqsidebartng/plugins/konqsidebar_history.desktop
%{_datadir}/konqsidebartng/plugins/konqsidebar_places.desktop
%{_datadir}/konqsidebartng/plugins/konqsidebar_tree.desktop
%{_datadir}/kservices5/konq_sidebartng.desktop
%{_datadir}/kservices5/webarchivethumbnail.desktop
%dir %{_datadir}/kxmlgui5/fsview
%{_datadir}/kxmlgui5/fsview/fsview_part.rc
%{_datadir}/qlogging-categories5/fsview.categories
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/fsviewpart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/konq_sidebar.so
%dir %{_libdir}/qt5/plugins/konqueror_kcms
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/kcm_bookmarks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/kcm_history.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/kcm_konq.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/kcm_performance.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/khtml_appearance.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/khtml_behavior.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/khtml_filter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/khtml_general.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/khtml_java_js.so
%dir %{_libdir}/qt5/plugins/dolphinpart
%dir %{_libdir}/qt5/plugins/dolphinpart/kpartplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/dolphinpart/kpartplugins/kimgallery.so
%attr(755,root,root) %{_libdir}/qt5/plugins/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%dir %{_libdir}/qt5/plugins/khtml
%dir %{_libdir}/qt5/plugins/khtml/kpartplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/khtml/kpartplugins/akregatorkonqfeediconkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtml/kpartplugins/autorefreshkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtml/kpartplugins/babelfishpluginkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtml/kpartplugins/khtmlsettingspluginkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtml/kpartplugins/khtmlttspluginkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtml/kpartplugins/konqueror_kget_browser_integrationkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtml/kpartplugins/uachangerpluginkhtml_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/khtml/kpartplugins/webarchiverpluginkhtml_kpartplugins.so
%dir %{_libdir}/qt5/plugins/konqueror
%dir %{_libdir}/qt5/plugins/konqueror/kpartplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror/kpartplugins/searchbarplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kget_browser_integration.so
%dir %{_libdir}/qt5/plugins/kwebkitpart
%dir %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins/akregatorkonqfeediconkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins/autorefreshkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins/babelfishpluginkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins/khtmlsettingspluginkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins/khtmlttspluginkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins/konqueror_kget_browser_integrationkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins/uachangerpluginkwebkitpart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwebkitpart/kpartplugins/webarchiverpluginkwebkitpart_kpartplugins.so
%dir %{_libdir}/qt5/plugins/webenginepart
%dir %{_libdir}/qt5/plugins/webenginepart/kpartplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/webenginepart/kpartplugins/akregatorkonqfeediconwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webenginepart/kpartplugins/autorefreshwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webenginepart/kpartplugins/babelfishpluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webenginepart/kpartplugins/khtmlsettingspluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webenginepart/kpartplugins/khtmlttspluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webenginepart/kpartplugins/konqueror_kget_browser_integrationwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webenginepart/kpartplugins/uachangerpluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/webenginepart/kpartplugins/webarchiverpluginwebenginepart_kpartplugins.so
%attr(755,root,root) %{_libdir}/qt5/plugins/dolphinpart/kpartplugins/dirfilterplugin.so
%{_desktopdir}/org.kde.konqueror.desktop
%attr(755,root,root) %{_libdir}/qt5/plugins/konqueror_kcms/khtml_cache.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/konq_events.h
%{_includedir}/KF5/konq_historyentry.h
%{_includedir}/KF5/konq_historyprovider.h
%{_includedir}/KF5/konq_popupmenu.h
%{_includedir}/KF5/konq_version.h
%{_includedir}/KF5/libkonq_export.h
%{_libdir}/cmake/KF5Konq
%{_libdir}/libKF5Konq.so
%{_includedir}/konqsidebarplugin.h
%{_libdir}/libkonqsidebarplugin.so
%{_includedir}/KF5/konq_kpart_plugin.h

