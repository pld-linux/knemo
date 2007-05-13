Summary:	The KDE Network Monitor
Summary(pl.UTF-8):	Monitor sieci dla KDE
Name:		knemo
Version:	0.4.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kde-apps.org/CONTENT/content-files/12956-%{name}-%{version}.tar.bz2
# Source0-md5:	daaeeca789f3d4d7616f7856b29b7db7
URL:		http://kde-apps.org/content/show.php?content=12956
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KNemo offers a network monitor similar to the one found in Windows.
For every network interface it displays an icon in the systray.

IMPORTANT: KNemo is not an executable but an KDED service. Therefore
it has to be started using Control Center/KDE Components/Service
Manager.

%description -l pl.UTF-8
KNemo jest monitorem sieci podobnym do tego spod Windows. Dla każdego
interfejsu wyświetla ikonkę w zasobniku systemowym.

WAŻNE: KNemo nie jest programem wykonywalnym, ale serwisem KDED,
dlatego musi być uruchomiony za pomocą Centrum Sterowania/Składniki
KDE/Menedżer Usług.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_knemo.la
%attr(755,root,root) %{_libdir}/kde3/kcm_knemo.so
%{_libdir}/kde3/kded_knemod.la
%attr(755,root,root) %{_libdir}/kde3/kded_knemod.so
%{_datadir}/apps/knemo
%{_datadir}/services/kded/knemod.desktop
%{_desktopdir}/kde/kcm_knemo.desktop
%{_iconsdir}/*/*/actions/*.png
%{_iconsdir}/crystalsvg/*/apps/knemo.png
