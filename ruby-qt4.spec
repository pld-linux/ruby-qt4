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
Release:	0.1
License:	GPL v2
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/71843/%{origname}-%{version}.tar.gz
# Source0-md5:	b1720fd928a6de35b543c6e83d5f1fe0
Patch0:		%{name}-qtruby-debian.patch
Patch1:		%{name}-qtruby-lib64.patch
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
#%patch0 -p1
#%patch1 -p1

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
%attr(755,root,root) %ghost %{_libdir}/libsmokeqt.so.?
%attr(755,root,root) %{_libdir}/libsmokeqt.so.*.*.*
%{ruby_rubylibdir}/Qt.rb
%dir %{ruby_rubylibdir}/Qt
%{ruby_rubylibdir}/Qt/active_item_model.rb
%{ruby_rubylibdir}/Qt/active_table_model.rb
%{ruby_rubylibdir}/Qt/qtruby4.rb
%{ruby_rubylibdir}/Qt3.rb
%{ruby_rubylibdir}/Qt4.rb
%attr(755,root,root) %{ruby_archdir}/qtruby4.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmokeqt.so
