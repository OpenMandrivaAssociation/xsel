Summary:	Command line clipboard and X selection tool
Name:		xsel
Version:	1.2.1
Release:	1
License:	MIT
Group:		System/X11
Url:		https://www.kfish.org/software/xsel/
Source0:	https://github.com/kfish/xsel/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xt)
BuildRequires:  pkgconfig(x11)

%description
XSel is a command line or script utility, similar to xclip, that can copy the
primary and secondary X selection, or any highlighted text, to or from a file,
stdin or stdout. It can also append to and delete the clipboard or buffer that
you would paste with the middle mouse button.

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1x*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
