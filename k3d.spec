Summary:	K-3D - 3D modeling, animation, and rendering system
Summary(pl.UTF-8):   K-3D - system modelowania, animacji i renderingu 3D
Name:		k3d
Version:	0.6.7.0
Release:	0.2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/k3d/%{name}-%{version}-src.tar.bz2
# Source0-md5:	0031402206dab46b563d149eac2324db
Source1:	%{name}.desktop
Patch0:		%{name}-lib64-fix.patch
URL:		http://k3d.sourceforge.net/
BuildRequires:	ImageMagick-c++-devel >= 1:6.2.4.0
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-any-devel >= 1.33
BuildRequires:	boost-array-devel >= 1.33
BuildRequires:	boost-bind-devel >= 1.33
BuildRequires:	boost-date_time-devel >= 1.33
BuildRequires:	boost-filesystem-devel >= 1.33
BuildRequires:	boost-regex-devel >= 1.33
BuildRequires:	boost-spirit-devel >= 1.33
BuildRequires:	freetype-devel
BuildRequires:	glibmm-devel
BuildRequires:	graphviz
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	gtkmm-devel
BuildRequires:	gts-devel
Buildrequires:	libgnome-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
Buildrequires:	plib-devel
%ifarch %{x8664}
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=285364
BuildRequires:	libstdc++-devel >= 5:3.4.0
%endif
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

%description -l pl.UTF-8
K-3D jest systemem modelowania, animacji i renderowania 3D,
przeznaczonym dla platform GNU/Linux i Win32. Możliwości obejmują
tworzenie i edycję geometrii w wielu działających w czasie
rzeczywistym widokach bryłowych, cieniowanych i teksturowanych OpenGL;
nieograniczone undo i redo; pełna rozszerzalność w czasie działania
poprzez zewnętrzne wtyczki; animowane proceduralne efekty geometryczne;
wszystkie parametry animowalne poprzez spójny interfejs oparty na
sterowaniu splajnami; renderowanie poprzez silniki zgodne z
interfejsem Rendermana; optymalizację do używania z silnikiem
renderującym BMRT, obsługującym raytracing, radiosity, prawdziwe
przemieszczenia i cieniowanie programowalne przez użytkownika;
obsługę renderowania w tle i wsadowego.

%package devel
Summary:	K-3D plugin and extension development kit
Summary(pl.UTF-8):   Pliki potrzebne do budowania modułów i rozszerzeń dla K-3D
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick-c++-devel
Requires:	gtk+-devel >= 1.2.8
Requires:	libsigc++1-devel

%description devel
Header files for writing K-3D plugins and extensions.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek i rozszerzeń dla K-3D.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-libxml2 \
	--with-external-boost \
	--with-freetype2 \
	--with-gnome \
	--with-graphviz \
	--with-gts \
	--with-imagemagick \
	--with-jpeg \
	--with-python \
	--with-nls \
	--with-openexr \
	--with-plib \
	--with-png \
	--without-qt \
	--with-svg-icons \
	--with-tiff

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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/%{name}/lib*.la
%{_includedir}/%{name}
