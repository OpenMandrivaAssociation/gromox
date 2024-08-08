# For the php module
%global _disable_ld_no_undefined 1
%global build_ldflags %{build_ldflags} -Wl,--allow-shlib-undefined

Name: gromox
Version: 2.30
Release: 1
Source0: https://github.com/grommunio/gromox/releases/download/gromox-%{version}/gromox-%{version}.tar.zst
Summary: Central groupware server component of grommunio
URL: https://github.com/grommunio/gromox
License: AGPL-3.0
Group: Servers/Groupware
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: pkgconfig(libHX)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(krb5-gssapi)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(ldap)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libxml-2.0)
BUildRequires: pkgconfig(libxxhash)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(tinyxml2)
BuildRequires: pkgconfig(vmime)
BuildRequires: pkgconfig(mariadb)
BuildRequires: php-devel
BuildRequires: slibtool
# Some optional deps we currently don't want
#BuildRequires: pkgconfig(ldns)
#BuildRequires: pkgconfig(libesedb)
#BuildRequires: pkgconfig(libolecf)
#BuildRequires: pkgconfig(libpff)

# Currently out-of-tree builds aren't supported,
# but declarative build does OOT
#BuildSystem: autotools

%patchlist
gromox-2.30-workaround-clang-bug-97005.patch

%description
Gromox is the central groupware server component of grommunio. It is capable of
serving as a drop-in replacement for Microsoft Exchange. Connectivity options
include RPC/HTTP (Outlook Anywhere), MAPI/HTTP, EWS, IMAP, POP3, an SMTP-speaking
LDA, and a PHP module with a MAPI function subset. Components can scale-out over
multiple hosts.

%prep
%autosetup -p1
slibtoolize --force

%conf
%configure

%build
%make_build

%install
%make_install

%files
%{_sysconfdir}/php.d/mapi.ini
%{_bindir}/gromox-abktconv
%{_bindir}/gromox-abktpull
%{_bindir}/gromox-compress
%{_bindir}/gromox-dbop
%{_bindir}/gromox-dscli
%{_bindir}/gromox-e2ghelper
%{_bindir}/gromox-eml2mbox
%{_bindir}/gromox-eml2mt
%{_bindir}/gromox-exm2eml
%{_bindir}/gromox-exm2ical
%{_bindir}/gromox-exm2mt
%{_bindir}/gromox-exm2vcf
%{_bindir}/gromox-ical2mt
%{_bindir}/gromox-kdb2mt
%{_bindir}/gromox-mailq
%{_bindir}/gromox-mbop
%{_bindir}/gromox-mbox2mt
%{_bindir}/gromox-mkmidb
%{_bindir}/gromox-mkprivate
%{_bindir}/gromox-mkpublic
%{_bindir}/gromox-mt2exm
%{_bindir}/gromox-vcf2mt
%{_unitdir}/gromox-delivery-queue.service
%{_unitdir}/gromox-delivery.service
%{_unitdir}/gromox-event.service
%{_unitdir}/gromox-http.service
%{_unitdir}/gromox-imap.service
%{_unitdir}/gromox-midb.service
%{_unitdir}/gromox-pop3.service
%{_unitdir}/gromox-snapshot.service
%{_unitdir}/gromox-snapshot.timer
%{_unitdir}/gromox-timer.service
%{_unitdir}/gromox-zcore.service
%{_sysusersdir}/sysusers-gromox.conf
%{_tmpfilesdir}/tmpfiles-gromox.conf
%{_libdir}/libgromox_common.so*
%{_libdir}/libgromox_dbop.so*
%{_libdir}/libgromox_email.so*
%{_libdir}/libgromox_epoll.so*
%{_libdir}/libgromox_exrpc.so*
%{_libdir}/libgromox_mapi.so*
%{_libdir}/libgromox_rpc.so*
%{_libdir}/libgxh_ews.so*
%{_libdir}/libgxh_mh_emsmdb.so*
%{_libdir}/libgxh_mh_nsp.so*
%{_libdir}/libgxh_oab.so*
%{_libdir}/libgxh_oxdisco.so*
%{_libdir}/libgxm_alias_resolve.so*
%{_libdir}/libgxm_exmdb_local.so*
%{_libdir}/libgxp_exchange_emsmdb.so*
%{_libdir}/libgxp_exchange_nsp.so*
%{_libdir}/libgxp_exchange_rfr.so*
%{_libdir}/libgxs_authmgr.so*
%{_libdir}/libgxs_dnsbl_filter.so*
%{_libdir}/libgxs_event_proxy.so*
%{_libdir}/libgxs_event_stub.so*
%{_libdir}/libgxs_exmdb_provider.so*
%{_libdir}/libgxs_ldap_adaptor.so*
%{_libdir}/libgxs_midb_agent.so*
%{_libdir}/libgxs_mysql_adaptor.so*
%{_libdir}/libgxs_ruleproc.so*
%{_libdir}/libgxs_timer_agent.so*
%{_libdir}/libgxs_user_filter.so*
%{_libdir}/php/extensions/mapi.so
%{_libdir}/security/pam_gromox.so
%{_libexecdir}/gromox
%{_datadir}/gromox
%{_mandir}/man4/alias_resolve.4gx*
%{_mandir}/man4/authmgr.4gx*
%{_mandir}/man4/autodiscover.4gx*
%{_mandir}/man4/dnsbl_filter.4gx*
%{_mandir}/man4/event_proxy.4gx*
%{_mandir}/man4/event_stub.4gx*
%{_mandir}/man4/ews.4gx*
%{_mandir}/man4/exchange_emsmdb.4gx*
%{_mandir}/man4/exchange_nsp.4gx*
%{_mandir}/man4/exchange_rfr.4gx*
%{_mandir}/man4/exmdb_local.4gx*
%{_mandir}/man4/exmdb_provider.4gx*
%{_mandir}/man4/ldap_adaptor.4gx*
%{_mandir}/man4/mapi.4gx*
%{_mandir}/man4/mh_emsmdb.4gx*
%{_mandir}/man4/mh_nsp.4gx*
%{_mandir}/man4/midb_agent.4gx*
%{_mandir}/man4/mod_cache.4gx*
%{_mandir}/man4/mod_fastcgi.4gx*
%{_mandir}/man4/mod_rewrite.4gx*
%{_mandir}/man4/mysql_adaptor.4gx*
%{_mandir}/man4/pam_gromox.4gx*
%{_mandir}/man4/timer_agent.4gx*
%{_mandir}/man4/user_filter.4gx*
%{_mandir}/man5/gromox-selinux.5*
%{_mandir}/man5/gromox.cfg.5*
%{_mandir}/man7/gromox.7*
%{_mandir}/man7/mapi.7gx*
%{_mandir}/man8/cgkrepair.8gx*
%{_mandir}/man8/delivery-queue.8gx*
%{_mandir}/man8/delivery.8gx*
%{_mandir}/man8/event.8gx*
%{_mandir}/man8/gromox-abktconv.8*
%{_mandir}/man8/gromox-abktpull.8*
%{_mandir}/man8/gromox-compress.8*
%{_mandir}/man8/gromox-dbop.8*
%{_mandir}/man8/gromox-dscli.8*
%{_mandir}/man8/gromox-eml2mbox.8*
%{_mandir}/man8/gromox-eml2mt.8*
%{_mandir}/man8/gromox-exm2eml.8*
%{_mandir}/man8/gromox-exm2ical.8*
%{_mandir}/man8/gromox-exm2mt.8*
%{_mandir}/man8/gromox-exm2vcf.8*
%{_mandir}/man8/gromox-kdb2mt.8*
%{_mandir}/man8/gromox-mailq.8*
%{_mandir}/man8/gromox-mbop.8*
%{_mandir}/man8/gromox-mkmidb.8*
%{_mandir}/man8/gromox-mkprivate.8*
%{_mandir}/man8/gromox-mkpublic.8*
%{_mandir}/man8/gromox-mt2exm.8*
%{_mandir}/man8/gromox-snapshot.8*
%{_mandir}/man8/http.8gx*
%{_mandir}/man8/imap.8gx*
%{_mandir}/man8/kdb-uidextract-limited.8*
%{_mandir}/man8/kdb-uidextract.8*
%{_mandir}/man8/midb.8gx*
%{_mandir}/man8/pop3.8gx*
%{_mandir}/man8/timer.8gx*
%{_mandir}/man8/zcore.8gx*
