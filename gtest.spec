Name:           gtest
Version:        1.8.0
Release:        1%{?dist}
Summary:        Google's C++ test framework

License:        BSD
URL:            https://github.com/google/googletest
Source0:        https://github.com/google/googletest/archive/release-%{version}.tar.gz
Patch0:         googletest-release-1.8.0-install-LIB_SUFFIX.patch
Patch1:         googletest-release-1.8.0-soname.patch

BuildRequires:  cmake >= 2.6.4

%description
Google's framework for writing C++ tests on a variety of platforms (GNU/Linux,
Mac OS X, Windows, Windows CE, and Symbian). Based on the xUnit architecture.
Supports automatic test discovery, a rich set of assertions, user-defined
assertions, death tests, fatal and non-fatal failures, various options for
running the tests, and XML test report generation.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n googletest-release-%{version}
%patch0 -p1
%patch1 -p1


%build
mkdir build
pushd build
%{cmake} -DBUILD_GTEST=ON -DBUILD_GMOCK=ON ..
make %{?_smp_mflags}
popd


%install
rm -rf %{buildroot}
pushd build
%make_install
popd


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc
%{_libdir}/*.so.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Tue Aug 22 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.8.0-1
- Initial release
