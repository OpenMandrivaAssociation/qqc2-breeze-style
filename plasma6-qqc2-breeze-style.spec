%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240223
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: plasma6-qqc2-breeze-style
Version: 6.1.3
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/qqc2-breeze-style/-/archive/%{gitbranch}/qqc2-breeze-style-%{gitbranchd}.tar.bz2#/qqc2-breeze-style-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/qqc2-breeze-style-%{version}.tar.xz
%endif
Summary: Breeze style for QtQuickComponents 2
URL: http://kde.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6QuickTemplates2)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6QuickCharts)
BuildRequires: cmake(X11)
BuildRequires: cmake(PkgConfig)
BuildRequires: pkgconfig(x11)

%description
Breeze style for QtQuickComponents 2.

%prep
%autosetup -p1 -n qqc2-breeze-style-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/cmake/QQC2BreezeStyle
%{_qtdir}/plugins/kf6/kirigami/platform/org.kde.breeze.so
%{_qtdir}/qml/org/kde/breeze
