Summary:	Tools to manipulate elf files
Summary(pl):	Narzêdzia do modyfikowania plików ELF
Name:		mklibs
Version:	0.1
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.pwr.wroc.pl/pub/linux/debian/dists/potato/main/source/admin/boot-floppies_2.2.17.tar.gz
# Source0-md5:	89e3ff165d8748d0f717195a5b4ce082
Patch0:		%{name}-pld.patch
Requires:	binutils
Requires:	glibc-pic >= 2.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Marcus Brinkmann's magic script from Debian boot-floppies package.
This utilitiy helps to reduce the necessary libraries to only include
the symbols needed to run a given set of executables. Run mklibs
--help to get some info. For details refer to /usr/bin/mklibs file
itself.

%description -l pl
Magiczny skrypt Marcusa Brinkmanna z debianowego pakietu
boot-floppies. To narzêdzie pomaga zmniejszyæ potrzebne biblioteki
tak, by zawiera³y jedynie symbole potrzebne dla podanego zbioru
binarek. Pomoc mo¿na uzyskaæ przez "mklibs --help", szczegó³y w samym
pliku /usr/bin/mklibs.

%prep
%setup -q -n boot-floppies-2.2.17
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install scripts/rootdisk/mklibs.sh $RPM_BUILD_ROOT%{_bindir}/mklibs
##|sed 's/libc-2.1.2/libc-2.2/g; s/libm-2.1.2/libm-2.2/g; s/ld-2.1.2/ld-2.2/g' \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
