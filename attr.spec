#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : attr
Version  : 2.4.47
Release  : 26
URL      : http://download.savannah.gnu.org/releases/attr/attr-2.4.47.src.tar.gz
Source0  : http://download.savannah.gnu.org/releases/attr/attr-2.4.47.src.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: attr-bin
Requires: attr-lib
Requires: attr-doc
Requires: attr-locales
Patch1: testsuite-xfs.patch

%description
_________________________________
Package home: http://savannah.nongnu.org/projects/attr

%package bin
Summary: bin components for the attr package.
Group: Binaries

%description bin
bin components for the attr package.


%package dev
Summary: dev components for the attr package.
Group: Development
Requires: attr-lib
Requires: attr-bin

%description dev
dev components for the attr package.


%package doc
Summary: doc components for the attr package.
Group: Documentation

%description doc
doc components for the attr package.


%package lib
Summary: lib components for the attr package.
Group: Libraries

%description lib
lib components for the attr package.


%package locales
Summary: locales components for the attr package.
Group: Default

%description locales
locales components for the attr package.


%prep
%setup -q -n attr-2.4.47
%patch1 -p1

%build
%configure --disable-static INSTALL_USER=root \
INSTALL_GROUP=root \
--enable-nls \
--enable-shared \
--disable-static
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install install install-lib install-dev DESTDIR=%{buildroot}
%find_lang attr
## make_install_append content
%check
fs=$(stat -f -c '%T' .)
if [ "$fs" = "tmpfs" ]
then
echo IGNORING TEST FAILURES AS RUNNING ON TMPFS
make %{?_smp_mflags} tests || true
else
make %{?_smp_mflags} tests
fi
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/attr
/usr/bin/getfattr
/usr/bin/setfattr

%files dev
%defattr(-,root,root,-)
/usr/include/attr/attributes.h
/usr/include/attr/error_context.h
/usr/include/attr/libattr.h
/usr/include/attr/xattr.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/attr/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man2/*
%doc /usr/share/man/man3/*
%exclude /usr/share/man/man5/attr.5

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f attr.lang 
%defattr(-,root,root,-)

