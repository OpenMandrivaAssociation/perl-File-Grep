%define	upstream_name	 File-Grep
%define	upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	A grep function taking a list of files as argument
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MN/MNEYLON/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
File::Grep provides similar functionality as perl's builtin grep, map,
and foreach commands, but iterating over a passed filelist instead of
arrays.  While trivial, this module can provide a quick dropin when
such functionality is needed.

%prep
%setup -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 402137
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2009.0
+ Revision: 241216
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.02-1mdv2008.0
+ Revision: 67612
- use %%mkrel


* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdk
- new version
- spec cleanup
- rpmbuildupdate aware
- better url
- fix directory ownership
- enable tests
- don't ship manifest

* Thu Jan 29 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-2mdk
- bzip2

* Wed Jan 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-1mdk
- from Robin Rosenberg <robin.rosenberg@dewire.com> : 
	- initial contrib import. Needed for building Captive-NTFS

