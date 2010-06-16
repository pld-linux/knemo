
%define		kdever	4.4.4
%define		qtver	4.6.2

Summary:	The KDE Network Monitor
Summary(pl.UTF-8):	Monitor sieci dla KDE
Name:		knemo
Version:	0.6.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kde-apps.org/CONTENT/content-files/12956-%{name}-%{version}.tar.bz2
# Source0-md5:	ee21176b15a0ee947d5f3c6dbfa568e4
URL:		http://kde-apps.org/content/show.php?content=12956
BuildRequires:  automoc4 >= 0.9.88
BuildRequires:  cmake >= 2.8.0
BuildRequires:  kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:  kde4-kdelibs-devel >= %{kdever}
BuildRequires:  qt4-build >= %{qtver}
BuildRequires:  qt4-qmake >= %{qtver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNemo offers a network monitor similar to the one found in Windows.
For every network interface it displays an icon in the systray.

IMPORTANT: To start KNemo go to the Control Center/Internet &
Network/Network Monitor. There is an option at the top of the dialog
saying "Use KNemo to monitor your interfaces". Activate it and KNemo
should start with KDE.

%description -l pl.UTF-8
KNemo jest monitorem sieci podobnym do tego spod Windows. Dla każdego
interfejsu wyświetla ikonkę w zasobniku systemowym.

WAŻNE: Aby uruchomić KNemo należy przejść do Centrum
Sterowania/Internet i sieć/Monitor sieci. Na górze okna znajduje się
opcja "Use KNemo to monitor your interfaces". Po włączeniu jej KNemo
powinno się uruchamiać podczas startu KDE.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knemo
%attr(755,root,root) %{_libdir}/kde4/kcm_knemo.so
%{_desktopdir}/kde4/knemo.desktop
%{_datadir}/apps/knemo
%{_datadir}/autostart/knemo.desktop
%{_iconsdir}/hicolor/*x*/apps/knemo.png
%{_iconsdir}/hicolor/*x*/status/knemo*.png
%{_datadir}/kde4/services/kcm_knemo.desktop
