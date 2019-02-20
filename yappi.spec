#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : yappi
Version  : 1.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/d2/92/7cd637a19fa2a10c0e55a44f8b36bcb83f0e1943ba8f1fb5edb15c819f2e/yappi-1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d2/92/7cd637a19fa2a10c0e55a44f8b36bcb83f0e1943ba8f1fb5edb15c819f2e/yappi-1.0.tar.gz
Summary  : Yet Another Python Profiler
Group    : Development/Tools
License  : MIT
Requires: yappi-bin = %{version}-%{release}
Requires: yappi-python = %{version}-%{release}
Requires: yappi-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : nose

%description
# Yappi
**Y**et **A**nother **P**ython **P**rof**i**ler, but this time support Multithread/CPU time profiling.

%package bin
Summary: bin components for the yappi package.
Group: Binaries

%description bin
bin components for the yappi package.


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

%description python3
python3 components for the yappi package.


%prep
%setup -q -n yappi-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1550688183
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/yappi

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
