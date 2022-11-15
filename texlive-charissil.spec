Name:		texlive-charissil
Version:	64998
Release:	1
Summary:	CharisSIL fonts with support for all LaTeX engines
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/charissil
License:	ofl lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/charissil.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/charissil.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the CharisSIL family of fonts adapted by
SIL International from Bitstream Charter in TrueType format,
with support for LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/charissil
%{_texmfdistdir}/fonts/vf/SIL/charissil
%{_texmfdistdir}/fonts/type1/SIL/charissil
%{_texmfdistdir}/fonts/truetype/SIL/charissil
%{_texmfdistdir}/fonts/tfm/SIL/charissil
%{_texmfdistdir}/fonts/map/dvips/charissil
%{_texmfdistdir}/fonts/enc/dvips/charissil
%doc %{_texmfdistdir}/doc/fonts/charissil

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
