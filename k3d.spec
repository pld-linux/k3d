#TODO
#- pl description
Summary:	K-3D - 3D modeling, animation, and rendering system
Summary(pl):	K-3D - system modelowania, animacji i renderingu 3D
Name:		k3d
Version:	0.4.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-src.tar.bz2
# Source0-md5:	10060990546e2e65ddfbcdf4f34729d4
Source1:	%{name}.desktop
Patch0:		%{name}-am18.patch
Patch1:		%{name}-user_reference_path.patch
URL:		http://k3d.sourceforge.net/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
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
K-3D jest systemem modelowania, animacji i renderowania 3D, przeznaczonym
dla platform GNU/Linux i Win32. 

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
%patch1	-p1

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

mv -f $RPM_BUILD_ROOT%{_datadir}/%{name}/icons/k3d*.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO $RPM_BUILD_ROOT%{_datadir}/%{name}/doc/user_reference
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/%{name}/lib*.so*
%{_datadir}/%{name}/*.conf
%{_datadir}/%{name}/dialogtemplates
%{_datadir}/%{name}/scripts
%{_datadir}/%{name}/shaders
%{_datadir}/%{name}/tutorials
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%dir %{_datadir}/%{name}
%dir %{_libdir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}
