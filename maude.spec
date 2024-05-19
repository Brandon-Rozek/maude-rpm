Name:     maude
Version:  3.4
Release:  %autorelease
Summary:  Language based on Rewriting Logic 
License:  GPL-2.0-or-later
URL:      https://maude.cs.illinois.edu/w/index.php/The_Maude_System
Source:   https://github.com/SRI-CSL/Maude/archive/refs/tags/Maude%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libsigsegv-devel
BuildRequires:  yices-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libbuddy
BuildRequires:  libtecla

# Fixes import to yices.h
Patch0: maude-3.4-yices-import.patch

Patch1: maude-3.4-search-datadir.patch

%description
Maude is a high-performance reflective language and system supporting both
equational and rewriting logic specification and programming.

%prep
%setup -q -n Maude-Maude3.4
%patch -P 0 -p0
%patch -P 1 -p1


%build

mkdir Opt
cd Opt

cat <<EOF > configure
#!/bin/sh
../configure "$@" --prefix=/usr
EOF
chmod u+x ./configure

%configure --with-yices2=yes --with-cvc4=no --enable-compiler
%make_build

%install
cd Opt
%make_install

%check
cd Opt
make check

%files
%{_bindir}/maude
%{_datadir}/file.maude
%{_datadir}/linear.maude
%{_datadir}/machine-int.maude
%{_datadir}/metaInterpreter.maude
%{_datadir}/model-checker.maude
%{_datadir}/prelude.maude
%{_datadir}/prng.maude
%{_datadir}/smt.maude
%{_datadir}/socket.maude
%{_datadir}/term-order.maude
%{_datadir}/time.maude


%license COPYING
%doc README.md ChangeLog AUTHORS

%changelog
%autochangelog
