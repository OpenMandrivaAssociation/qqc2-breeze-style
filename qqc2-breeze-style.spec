%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: qqc2-breeze-style
Version: 5.25.1
Release: 1
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/%{name}-%{version}.tar.xz
Summary: Breeze style for QtQuickComponents 2
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5QuickTemplates2)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(X11)
BuildRequires: cmake(PkgConfig)
BuildRequires: cmake(Qt5X11Extras)
BuildRequires: pkgconfig(x11)

%description
Breeze style for QtQuickComponents 2.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/cmake/KF5QQC2BreezeStyle
%{_libdir}/qt5/plugins/kf5/kirigami/org.kde.breeze.so
%{_libdir}/qt5/qml/QtQuick/Controls.2/org.kde.breeze
%{_libdir}/qt5/qml/org/kde/breeze
%{_libdir}/qt5/qml/org/kde/kirigami.2/styles/org.kde.breeze
