Summary:	The KDE Network Monitor
Summary(pl):	Monitor sieci dla KDE
Name:		knemo
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.eris23.de/knemo/%{name}-%{version}.tar.bz2
# Source0-md5:	774b7b085e7b2d492bf811d7f89cee6e
URL:		http://kde-apps.org/content/show.php?content=12956
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
cp -f /usr/share/automake/config.sub admin

%configure
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
%{_datadir}/applnk/Settings/Network/kcm_knemo.desktop
%{_datadir}/services/kded/knemod.desktop
%{_iconsdir}/*/*/actions/*.png
%{_iconsdir}/crystalsvg/*/apps/knemo.png
