Summary:	K-3D - 3D modeling, animation, and rendering system
Summary(pl):	K-3D - system modelowania, animacji i renderingu 3D
Name:		k3d
Version:	0.1.18.1
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.k-3d.com/downloads/%{name}-%{version}-src.tar.bz2
BuildRequires:	OpenGL-devel
BuildRequires:	gtk+-devel >= 1.2.8
BuildRequires:	BMRT >= 2.5
Requires:	OpenGL
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
K-3D is the free 3D modeling, animation, and rendering system.

%description -l pl
K-3D jest darmowym systemem do modelowania, animacji i renderowania
3D.

%prep
%setup -q -n projects

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
