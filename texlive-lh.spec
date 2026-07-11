%global tl_name lh
%global tl_revision 77838

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.5g
Release:	%{tl_revision}.1
Summary:	Cyrillic fonts that support LaTeX standard encodings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/cyrillic/lh
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lh.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lh.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lh.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ec)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The LH fonts address the problem of the wide variety of alphabets that
are written with Cyrillic-style characters. The fonts are the original
basis of the set of T2* and X2 encodings that are now used when LaTeX
users need to write in Cyrillic languages. Macro support in standard
LaTeX encodings is offered through the latex-cyrillic and t2 bundles,
and the package itself offers support for other (more traditional)
encodings. The fonts, in the standard T2* and X2 encodings are available
in Adobe Type 1 format, in the CM-Super family of fonts. The package
also offers its own LaTeX support for OT2 encoded fonts, CM bright
shaped fonts and Concrete shaped fonts.

