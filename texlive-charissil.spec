%global tl_name charissil
%global tl_revision 78931
%global tl_version 6.101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	CharisSIL fonts with support for all LaTeX engines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/charissil
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/charissil.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/charissil.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This package provides the CharisSIL family of fonts adapted by SIL
International from Bitstream Charter in TrueType format, with support
for LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from charissil:
Map charssil.map
TL_DROPIN_EOF
