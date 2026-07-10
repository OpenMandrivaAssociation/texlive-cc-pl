%global tl_name cc-pl
%global tl_revision 58602

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02.3
Release:	%{tl_revision}.1
Summary:	Polish extension of Computer Concrete fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cc-pl
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cc-pl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cc-pl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
These Metafont sources rely on the availability of the Metafont 'Polish'
fonts and of the Metafont sources of the original Concrete fonts. Adobe
Type 1 versions of the fonts are included.

