%define	upstream_name	 File-Grep
%define	upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	A grep function taking a list of files as argument
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MN/MNEYLON/%{upstream_name}-%{upstream_version}.tar.bz2

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
File::Grep provides similar functionality as perl's builtin grep, map,
and foreach commands, but iterating over a passed filelist instead of
arrays.  While trivial, this module can provide a quick dropin when
such functionality is needed.

%prep
%setup -n %{upstream_name}-%{upstream_version}

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
