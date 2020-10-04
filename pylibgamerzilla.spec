%global __cmake_in_source_build 1

Summary: Python Integration with Gamerzilla Library
Name: pylibgamerzilla
Version: 0.0.1
Release: 4%{?dist}
License: MIT
URL: https://github.com/dulsi/pylibgamerzilla
Source0: http://www.identicalsoftware.com/gamerzilla/%{name}-%{version}.tgz
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: swig
BuildRequires: cmake
BuildRequires: libgamerzilla-devel
BuildRequires: python3-devel

%description
Python interface to the Gamerzilla trophy/achievement system for games.
It allows you display achievements from python games online.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
mkdir -p %{buildroot}/%{python3_sitearch}
mkdir -p %{buildroot}/%{python3_sitelib}
cp %{_builddir}/%{name}-%{version}/_gamerzilla.so %{buildroot}/%{python3_sitearch}/
cp %{_builddir}/%{name}-%{version}/gamerzilla.py %{buildroot}/%{python3_sitelib}/

%files
%license LICENSE
%{python3_sitearch}/_gamerzilla.so
%{python3_sitelib}/gamerzilla.py
%{python3_sitelib}/__pycache__/gamerzilla.cpython-%{python3_version_nodots}{,.opt-?}.pyc

%changelog
* Sun Oct 04 2020 Andy Mender <andymenderunix@gmail.com> - 0.0.1-4
- Enable in-source builds
- Switch RPM_BUILD_ROOT to buildroot macro

* Sat Oct 03 2020 Dennis Payne <dulsi@identicalsoftware.com> - 0.0.1-3
- Add another missing build requires

* Sat Oct 03 2020 Dennis Payne <dulsi@identicalsoftware.com> - 0.0.1-2
- Add missing build requires

* Tue Sep 22 2020 Dennis Payne <dulsi@identicalsoftware.com> - 0.0.1-1
- Initial spec
