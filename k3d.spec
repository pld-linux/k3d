Summary:	K-3D
Summary(pl):	K-3D
Name:		k3d
Version:	0.1.18.1
Release:	1
License:	GPL
Group:		X11/Graphics
Group(pl):	X11/Grafika
Source0:	http://www.k-3d.com/downloads/%{name}-%{version}-src.tar.bz2
#Patch0:	%{name}
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	BMRT >= 2.5
Requires:	OpenGL
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description

%description -l pl

%prep
%setup -q -n projects

#%patch

%build
./configure --prefix=%{_prefix}
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
install -d $RPM_BUILD_ROOT%{_datadir}/k3d/plugins/bitmaplib

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install
# install bitmaplib
install k3d/bitmaplib/*.{k3dlib,gtkml,xp,html,jpg,png} \
	$RPM_BUILD_ROOT%{_datadir}/k3d/plugins/bitmaplib/
install k3d/bitmaplib/netpbm.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
