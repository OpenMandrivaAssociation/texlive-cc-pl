%global tl_name cc-pl
%global tl_revision 58602
%global tl_version 1.02.3

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Polish extension of Computer Concrete fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cc-pl
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cc-pl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cc-pl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
These Metafont sources rely on the availability of the Metafont 'Polish'
fonts and of the Metafont sources of the original Concrete fonts. Adobe
Type 1 versions of the fonts are included.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from cc-pl:
MixedMap ccpl.map
TL_DROPIN_EOF
