# revision 15878
# category Package
# catalog-ctan /fonts/cc-pl
# catalog-date 2009-09-24 20:53:04 +0200
# catalog-license pd
# catalog-version 1.02.2
Name:		texlive-cc-pl
Version:	1.02.2
Release:	1
Summary:	Polish extension of Computer Concrete fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cc-pl
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cc-pl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cc-pl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3

%description
These MetaFont sources rely on the availability of the MetaFont
'Polish' fonts and of the MetaFont sources of the original
Concrete fonts. Adobe Type 1 versions of the fonts are
included.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/cc-pl/ccpl.map
%{_texmfdistdir}/fonts/source/public/cc-pl/fic_mic.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pccsc10.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcmi10.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcr10.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcr5.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcr6.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcr7.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcr8.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcr9.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcsl10.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcslc9.mf
%{_texmfdistdir}/fonts/source/public/cc-pl/pcti10.mf
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pccsc10.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcmi10.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcr10.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcr5.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcr6.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcr7.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcr8.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcr9.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcslc9.tfm
%{_texmfdistdir}/fonts/tfm/public/cc-pl/pcti10.tfm
%{_texmfdistdir}/fonts/type1/public/cc-pl/pccsc10.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcmi10.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcr10.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcr5.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcr6.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcr7.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcr8.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcr9.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcsl10.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcslc9.pfb
%{_texmfdistdir}/fonts/type1/public/cc-pl/pcti10.pfb
%doc %{_texmfdistdir}/doc/fonts/cc-pl/README.cc-pl
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
