# Needed for the PHP module (not linking to php symbols that are there when loaded into php)
%define _disable_ld_no_undefined 1

Name:		gromox
Version:	2.46
Release:	1
Source0:	https://github.com/grommunio/gromox/releases/download/gromox-%{version}/gromox-%{version}.tar.zst
Summary:	Groupware server backend for grommunio
URL:		https://github.com/grommunio/gromox
License:	AGPL-3.0
Group:		Servers
BuildRequires:	autoconf automake slibtool
BuildRequires:	pkgconfig(wmime)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(fmt)
BuildRequires:	pkgconfig(libHX)
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(tinyxml2)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	php-devel

%description
Gromox is the central groupware server component of grommunio.
It is capable of serving as a drop-in replacement for Microsoft Exchange.
Connectivity options include RPC/HTTP (Outlook Anywhere), MAPI/HTTP,
EWS, IMAP, POP3, an SMTP-speaking LDA, and a PHP module with a MAPI
function subset.

Components can scale-out over multiple hosts.

%prep
%autosetup -p1
export LIBTOOL=slibtool
./qconf --help

%conf
%configure

%build
%make_build

%install
%make_install

%files
%{_sysconfdir}/php.d/mapi.ini
%{_bindir}/gromox-*
%{_unitdir}/*
%{_sysusersdir}/sysusers-gromox.conf
%{_tmpfilesdir}/tmpfiles-gromox.conf
# It doesn't make sense to split those into
# lib packages, they're not meant to be used
# by anything but gromox (and can't be, because
# the corresponding headers aren't installed)
%{_libdir}/*.so*
%{_libdir}/php/extensions/mapi.so
%{_libdir}/security/pam_gromox.so
%{_libexecdir}/gromox
%{_datadir}/gromox
%{_mandir}/man?/*
