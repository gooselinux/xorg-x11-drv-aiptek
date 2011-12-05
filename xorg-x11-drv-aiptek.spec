%global tarball xf86-input-aiptek
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/input

Summary:   Xorg X11 aiptek input driver
Name:      xorg-x11-drv-aiptek
Version: 1.3.0
Release: 2%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6
BuildRequires: xorg-x11-util-macros >= 1.3.0

Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6

%description 
X.Org X11 aiptek input driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/aiptek_drv.so
%{_mandir}/man4/aiptek.4*

%changelog
* Wed Jan 06 2010 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-2
- Use global instead of define per Packaging Guidelines.

* Fri Sep 11 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.3.0-1
- aiptek 1.3.0
- aiptek-1.2.0-abi.patch: Drop
- Require xorg-x11-util-macros 1.3.0

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Peter Hutterer <peter.hutterer@redhat.com> 1.2.0-2
- aiptek-1.2.0-abi.patch: cope with XINPUT ABI 7.

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.2.0-1.1
- ABI bump

* Tue Feb 24 2009 Peter Hutterer <peter.hutterer@redhat.com> - 1.2.0-1
- aiptek 1.2.0

* Thu Mar 20 2008 Adam Jackson <ajax@redhat.com> 1.1.1-1
- aiptek 1.1.1

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.1-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.0.1-5
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.0.1-4
- Update BuildRequires and Requires.

* Tue Feb 20 2007 Adam Jackson <ajax@redhat.com> 1.0.1-3
- ExclusiveArch -> ExcludeArch
- Don't own directories already owned by Xorg

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-2
- rebuild

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.0.1-1
- Bump to 1.0.1 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.0.0.5-1
- Updated xorg-x11-drv-aiptek to version 1.0.0.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.4-1
- Updated xorg-x11-drv-aiptek to version 1.0.0.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.2-1
- Updated xorg-x11-drv-aiptek to version 1.0.0.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.0.0.1-1
- Updated xorg-x11-drv-aiptek to version 1.0.0.1 from X11R7 RC1
- Fix *.la file removal.
* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.0.0-0
- Initial spec file for aiptek input driver generated automatically
  by my xorg-driverspecgen script.
