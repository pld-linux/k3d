Summary:	K-3D - 3D modeling, animation, and rendering system
Summary(pl):	K-3D - system modelowania, animacji i renderingu 3D
Name:		k3d
Version:	0.4.3.0
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/k3d/%{name}-%{version}.tbz2
# Source0-md5:	bf45904827a6a37b601ffaa963695a14
Source1:	%{name}.desktop
Patch0:		%{name}-user_reference_path.patch
Patch1:		%{name}-new_pnm.patch
URL:		http://k3d.sourceforge.net/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	graphviz
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	libsigc++1-devel
BuildRequires:	libtool
Requires:	OpenGL
Requires:	renderman-engine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
K-3D is a 3D modeling, animation, and rendering system for GNU/Linux &
Win32. Features include creation and editing of geometry in multiple
realtime OpenGL solid, shaded, and texture-mapped views; unlimited
undos and redos; complete extensibility at runtime through third-party
plugins; animated procedural geometric effects; all parameters
animatable through a consistent control-spline based interface;
rendering pipeline to Renderman Interface compliant rendering engines;
optimization for use with the BMRT rendering engine, which features
raytracing, radiosity rendering, true displacement, and user
programmable shaders; and support for background and batch rendering.

%description -l pl
K-3D jest systemem modelowania, animacji i renderowania 3D,
przeznaczonym dla platform GNU/Linux i Win32. Mo¿liwo¶ci obejmuj±
tworzenie i edycjê geometrii w wielu dzia³aj±cych w czasie
rzeczywistym widokach bry³owych, cieniowanych i teksturowanych OpenGL;
nieograniczone undo i redo; pe³na rozszerzalno¶æ w czasie dzia³ania
poprzez zewnêtrzne wtyczki; animowane proceduralne efekty geometryczne;
wszystkie parametry animowalne poprzez spójny interfejs oparty na
sterowaniu splajnami; renderowanie poprzez silniki zgodne z
interfejsem Rendermana; optymalizacjê do u¿ywania z silnikiem
renderuj±cym BMRT, obs³uguj±cym raytracing, radiosity, prawdziwe
przemieszczenia i cieniowanie programowalne przez u¿ytkownika;
obs³ugê renderowania w tle i wsadowego.

%package devel
Summary:        K-3D plugin and extension development kit
Summary(pl):    Pliki potrzebne do budowania modu³ów i rozszerzeñ dla K-3D
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:	ImageMagick-c++-devel
Requires:	gtk+-devel >= 1.2.8
Requires:	libsigc++1-devel

%description devel
Header files for writing K-3D plugins and extensions.

%description devel -l pl
Pliki nag³ówkowe do tworzenia wtyczek i rozszerzeñ dla K-3D.

%prep
%setup -q
%patch0 -p1
%patch1

mv -f k3dui/application_window.cpp k3dui/application_window.cpp.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/*.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO user_reference
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.conf
%{_datadir}/%{name}/dialogtemplates
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/shaders
%{_datadir}/%{name}/tutorials
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/%{name}/lib*.la
%{_includedir}/%{name}
