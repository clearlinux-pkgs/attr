#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x154343260542DF34 (brandon@ifup.co)
#
Name     : attr
Version  : 2.4.47
Release  : 32
URL      : http://download.savannah.gnu.org/releases/attr/attr-2.4.47.src.tar.gz
Source0  : http://download.savannah.gnu.org/releases/attr/attr-2.4.47.src.tar.gz
Source99 : http://download.savannah.gnu.org/releases/attr/attr-2.4.47.src.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+ LGPL-2.1
Requires: attr-bin
Requires: attr-lib
Requires: attr-doc
Requires: attr-locales
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
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
Provides: attr-devel

%description dev
dev components for the attr package.


%package dev32
Summary: dev32 components for the attr package.
Group: Default
Requires: attr-lib32
Requires: attr-bin
Requires: attr-dev

%description dev32
dev32 components for the attr package.


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


%package lib32
Summary: lib32 components for the attr package.
Group: Default

%description lib32
lib32 components for the attr package.


%package locales
Summary: locales components for the attr package.
Group: Default

%description locales
locales components for the attr package.


%prep
%setup -q -n attr-2.4.47
%patch1 -p1
pushd ..
cp -a attr-2.4.47 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1495410068
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
%configure --disable-static INSTALL_USER=root \
INSTALL_GROUP=root \
--enable-nls \
--enable-shared \
--disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static INSTALL_USER=root \
INSTALL_GROUP=root \
--enable-nls \
--enable-shared \
--disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1495410068
rm -rf %{buildroot}
pushd ../build32/
%make_install32 install install-lib install-dev DESTDIR=%{buildroot}
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install install install-lib install-dev DESTDIR=%{buildroot}
%find_lang attr
## make_install_append content
%check
make %{?_smp_mflags} tests || true
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
/usr/lib64/libattr.so

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libattr.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/attr/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man2/*
%doc /usr/share/man/man3/*
%exclude /usr/share/man/man5/attr.5

%files lib
%defattr(-,root,root,-)
/usr/lib64/libattr.so.1
/usr/lib64/libattr.so.1.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libattr.so.1
/usr/lib32/libattr.so.1.1.0

%files locales -f attr.lang
%defattr(-,root,root,-)

