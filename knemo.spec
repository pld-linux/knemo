Summary:	The KDE Network Monitor
Summary(pl):	Monitor sieci dla KDE
Name:		knemo
Version:	0.1.10
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://kde-apps.org/content/files/12956-%{name}-%{version}.tar.bz2
# Source0-md5:	e9bd015a053648513aa9b5dc53ccb9ba
URL:		http://kde-apps.org/content/show.php?content=12956
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	kdelibs-devel

%description
KNemo offers a network monitor similar to the one found in Windows.
For every network interface it displays an icon in the systray.

IMPORTANT: KNemo is not an executable but an KDED service. Therefore
it has to be started using Control Center/KDE Components/Service
Manager.

%description -l pl
KNemo jest monitorem sieci podobnym do tego spod Windows. Dla ka¿dego
interfejsu wy¶wietla ikonkê w zasobniku systemowym.

WA¯NE: KNemo nie jest programem wykonywalnym, ale serwisem KDED,
dlatego musi byæ uruchomiony za pomoc± Centrum Sterowania/Sk³adniki
KDE/Mened¿er Us³ug.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_knemo.la
%{_libdir}/kde3/kcm_knemo.so
%{_libdir}/kde3/kded_knemod.la
%{_libdir}/kde3/kded_knemod.so
%{_datadir}/applnk/Settings/Network/kcm_knemo.desktop
%{_datadir}/services/kded/knemod.desktop
%{_datadir}/icons/*/*/actions/*.png
%{_datadir}/apps/knemo/eventsrc
%{_datadir}/locale/*/LC_MESSAGES/*
