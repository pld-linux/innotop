Summary:	A MySQL and InnoDB monitor program
Name:		innotop
Version:	1.6.0
Release:	1
License:	GPL v2+ or Artistic
Group:		Applications/Databases
URL:		http://sourceforge.net/projects/innotop
Source0:	http://dl.sourceforge.net/innotop/%{name}-%{version}.tar.gz
# Source0-md5:	3f90e94b96b9c27bf2a162f85df75dcb
BuildRequires:	perl-DBD-mysql
BuildRequires:	perl-DBI
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-Term-ReadKey
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
innotop connects to a MySQL database server and retrieves information
from it, then displays it in a manner similar to the UNIX top program.
innotop uses the data from SHOW VARIABLES, SHOW GLOBAL STATUS, SHOW
FULL PROCESSLIST, and SHOW ENGINE INNODB STATUS, among other things.

%prep
%setup -q

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{perl_vendorarch}/auto/innotop/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL
%attr(755,root,root) %{_bindir}/innotop
%{perl_vendorlib}/InnoDBParser.pm
%{_mandir}/man3/InnoDBParser.3pm*
%{_mandir}/man1/innotop.1*
