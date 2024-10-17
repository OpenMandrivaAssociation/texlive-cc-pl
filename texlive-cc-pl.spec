Name:		texlive-cc-pl
Version:	58602
Release:	2
Summary:	Polish extension of Computer Concrete fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cc-pl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cc-pl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cc-pl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
These MetaFont sources rely on the availability of the MetaFont
'Polish' fonts and of the MetaFont sources of the original
Concrete fonts. Adobe Type 1 versions of the fonts are
included.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/cc-pl
%{_texmfdistdir}/fonts/source/public/cc-pl
%{_texmfdistdir}/fonts/tfm/public/cc-pl
%{_texmfdistdir}/fonts/type1/public/cc-pl
%doc %{_texmfdistdir}/doc/fonts/cc-pl

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
