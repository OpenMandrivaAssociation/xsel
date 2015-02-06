Summary:	Command line clipboard and X selection tool
Name:		xsel
Version:	1.2.0
Release:	2
License:	MIT
Group:		System/X11
Url:		http://www.vergenet.net/~conrad/software/xsel/
Source0:	http://www.vergenet.net/~conrad/software/xsel/download/xsel-%{version}.tar.gz
# Applied upstream (BZ#690214)
Patch0:		xsel-1.2.0-MAX_NUM_TARGETS.patch
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xt)

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
%setup -q
%patch0 -p1 -b .MAX_NUM_TARGETS

%build
%configure2_5x
%make

%install
%makeinstall_std



