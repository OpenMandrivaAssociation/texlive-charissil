%global tl_name charissil
%global tl_revision 78931

Name:		texlive-%{tl_name}
Epoch:		1
Version:	6.101
Release:	%{tl_revision}.1
Summary:	CharisSIL fonts with support for all LaTeX engines
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/charissil
License:	ofl lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/charissil.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/charissil.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the CharisSIL family of fonts adapted by SIL
International from Bitstream Charter in TrueType format, with support
for LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX.

