Summary:	Command line tool to create/retrieve/delete accounting objects
Name:		nfacct
Version:	1.0.0
Release:	2
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://www.netfilter.org/projects/nfacct/index.html
Source0:	http://www.netfilter.org/projects/nfacct/files/%{name}-%{version}.tar.bz2
Source1:	http://www.netfilter.org/projects/nfacct/files/%{name}-%{version}.tar.bz2.sig
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libnetfilter_acct) >= 1.0.0
BuildRequires:	pkgconfig(libmnl) >= 1.0.0

%description
nfacct is the command line tool that allows to manipulate the Netfilter's
extended accounting infrastructure.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_sbindir}/nfacct
%{_mandir}/man8/nfacct.8*

