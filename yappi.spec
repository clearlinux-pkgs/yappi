#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yappi
Version  : 1.2.5
Release  : 16
URL      : https://files.pythonhosted.org/packages/a5/c6/1edb532eb1f8db311288a058883d549bebd6e028a42f331819970d5f16a6/yappi-1.2.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/a5/c6/1edb532eb1f8db311288a058883d549bebd6e028a42f331819970d5f16a6/yappi-1.2.5.tar.gz
Summary  : Yet Another Python Profiler
Group    : Development/Tools
License  : MIT
Requires: yappi-bin = %{version}-%{release}
Requires: yappi-license = %{version}-%{release}
Requires: yappi-python = %{version}-%{release}
Requires: yappi-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
<p align="center">
<img src="https://raw.githubusercontent.com/sumerc/yappi/master/Misc/logo.png" alt="yappi">
</p>

%package bin
Summary: bin components for the yappi package.
Group: Binaries
Requires: yappi-license = %{version}-%{release}

%description bin
bin components for the yappi package.


%package license
Summary: license components for the yappi package.
Group: Default

%description license
license components for the yappi package.


%package python
Summary: python components for the yappi package.
Group: Default
Requires: yappi-python3 = %{version}-%{release}

%description python
python components for the yappi package.


%package python3
Summary: python3 components for the yappi package.
Group: Default
Requires: python3-core
Provides: pypi(yappi)

%description python3
python3 components for the yappi package.


%prep
%setup -q -n yappi-1.2.5
cd %{_builddir}/yappi-1.2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588007591
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yappi
cp %{_builddir}/yappi-1.2.5/LICENSE %{buildroot}/usr/share/package-licenses/yappi/de3afc59d872a7c19e2040e9b14e73bc3057dd2e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/yappi

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yappi/de3afc59d872a7c19e2040e9b14e73bc3057dd2e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
