%define	module	File-Grep
%define	name	perl-%{module}
%define	version	0.02
%define	release	1mdk

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A grep function taking a list of files as argument
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/M/MN/MNEYLON/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}
Buildrequires:	perl-devel
Requires:	perl 
Buildarch:	noarch

%description
File::Grep provides similar functionality as perl's builtin grep, map,
and foreach commands, but iterating over a passed filelist instead of
arrays.  While trivial, this module can provide a quick dropin when
such functionality is needed.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/*/*

