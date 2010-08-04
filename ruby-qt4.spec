# TODO:
# - pl is corrupted (
# - file /usr/bin/rbqtapi from install of ruby-qt4-qtruby-1.4.10-0.1.pentium4 conflicts with file from package kdebindings-ruby-qt-3.5.9-2.i686
# - complete spec (BRs,...)
# - switch to ruby_vendor{lib,arch}dirs - probably there is a problem with /usr/share/cmake/Modules/FindRuby.cmake:41: \
#   EXECUTE_PROCESS(COMMAND ${RUBY_EXECUTABLE} -r vendor-specific -e "print 'true'"
# - fix qwt issue
#
%define		origname	qt4-qtruby
%define		qtver		4.6.3

Summary:	Ruby bindings for the Qt4 GUI library
Summary(pl.UTF-8):	Dowiązania ruby dla biblioteki Qt4 GUI
Name:		ruby-qt4
Version:	2.1.0
Release:	1
License:	GPL v2
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/71843/%{origname}-%{version}.tar.gz
# Source0-md5:	b1720fd928a6de35b543c6e83d5f1fe0
URL:		http://rubyforge.org/projects/korundum/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.0
BuildRequires:	qscintilla2-devel
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildConflicts:	qwt-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for the Qt4 GUI library.

%description -l pl.UTF-8
Dowiązania ruby dla biblioteki Qt4 GUI.

%package devel
Summary:	Ruby bindings development files for Qt4 GUI
Summary(pl.UTF-8):	Pliki nagĹ~BĂłwkowe dowiązań ruby dla Qt4 GUI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Ruby bindings development files for Qt4 GUI.

%description devel -l pl.UTF-8
Pliki nagĹ~BĂłwkowe dowiązań ruby dla Qt4 GUI.

%prep
%setup -q -n %{origname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}" \
	-DRUBY_EXECUTABLE="%{__ruby}" \
	-DCMAKE_VERBOSE_MAKEFILE=1 \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/rbqtapi
%attr(755,root,root) %{_bindir}/rbrcc
%attr(755,root,root) %{_bindir}/rbuic4
%attr(755,root,root) %{_bindir}/smokeapi
%attr(755,root,root) %{_bindir}/smokegen
%attr(755,root,root) %{_libdir}/libcppparser.so
%attr(755,root,root) %ghost %{_libdir}/libqtruby4shared.so.?
%attr(755,root,root) %{_libdir}/libqtruby4shared.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokebase.so.?
%attr(755,root,root) %{_libdir}/libsmokebase.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtcore.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtdbus.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtdbus.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtgui.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtgui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtnetwork.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtnetwork.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtopengl.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtopengl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtscript.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtscript.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtsql.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtsql.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtsvg.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtsvg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqttest.so.?
%attr(755,root,root) %{_libdir}/libsmokeqttest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtuitools.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtuitools.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtwebkit.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtwebkit.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtxml.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtxml.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmokeqtxmlpatterns.so.?
%attr(755,root,root) %{_libdir}/libsmokeqtxmlpatterns.so.*.*.*
%attr(755,root,root) %{_libdir}/smokegen/generator_dump.so
%attr(755,root,root) %{_libdir}/smokegen/generator_smoke.so
%{_datadir}/smokegen
%{_libdir}/ruby/site_ruby/1.8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqtruby4shared.so
%attr(755,root,root) %{_libdir}/libsmokebase.so
%attr(755,root,root) %{_libdir}/libsmokeqtcore.so
%attr(755,root,root) %{_libdir}/libsmokeqtdbus.so
%attr(755,root,root) %{_libdir}/libsmokeqtgui.so
%attr(755,root,root) %{_libdir}/libsmokeqtnetwork.so
%attr(755,root,root) %{_libdir}/libsmokeqtopengl.so
%attr(755,root,root) %{_libdir}/libsmokeqtscript.so
%attr(755,root,root) %{_libdir}/libsmokeqtsql.so
%attr(755,root,root) %{_libdir}/libsmokeqtsvg.so
%attr(755,root,root) %{_libdir}/libsmokeqttest.so
%attr(755,root,root) %{_libdir}/libsmokeqtuitools.so
%attr(755,root,root) %{_libdir}/libsmokeqtwebkit.so
%attr(755,root,root) %{_libdir}/libsmokeqtxml.so
%attr(755,root,root) %{_libdir}/libsmokeqtxmlpatterns.so
%{_includedir}/smoke.h
%{_includedir}/smoke
%{_includedir}/smokegen
%{_includedir}/qtruby
