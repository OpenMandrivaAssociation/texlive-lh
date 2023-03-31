Name:		texlive-lh
Version:	15878
Release:	2
Summary:	Cyrillic fonts that support LaTeX standard encodings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/cyrillic/lh
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lh.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lh.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lh.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-ec

%description
The LH fonts address the problem of the wide variety of
alphabets that are written with Cyrillic-style characters. The
fonts are the original basis of the set of T2* and X2 encodings
that are now used when LaTeX users need to write in Cyrillic
languages. Macro support in standard LaTeX encodings is offered
through the cyrillic and t2 bundles, and the package itself
offers support for other (more traditional) encodings. The
fonts, in the standard T2* and X2 encodings are available in
Adobe Type 1 format, in the CM-Super family of fonts. The
package also offers its own LaTeX support for OT2 encoded
fonts, CM bright shaped fonts and Concrete shaped fonts.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/lh/base/fikparm.mf
%{_texmfdistdir}/fonts/source/lh/base/lcyrbeg.mf
%{_texmfdistdir}/fonts/source/lh/base/lcyrdefs.mf
%{_texmfdistdir}/fonts/source/lh/base/ldbroman.mf
%{_texmfdistdir}/fonts/source/lh/base/ldcsc.mf
%{_texmfdistdir}/fonts/source/lh/base/ldroman.mf
%{_texmfdistdir}/fonts/source/lh/base/ldtexset.mf
%{_texmfdistdir}/fonts/source/lh/base/ldtextit.mf
%{_texmfdistdir}/fonts/source/lh/base/ldtitle.mf
%{_texmfdistdir}/fonts/source/lh/base/lebroman.mf
%{_texmfdistdir}/fonts/source/lh/base/lecsc.mf
%{_texmfdistdir}/fonts/source/lh/base/leroman.mf
%{_texmfdistdir}/fonts/source/lh/base/letextit.mf
%{_texmfdistdir}/fonts/source/lh/base/lgcspl.mf
%{_texmfdistdir}/fonts/source/lh/base/lgcyracc.mf
%{_texmfdistdir}/fonts/source/lh/base/lgcyri.mf
%{_texmfdistdir}/fonts/source/lh/base/lgcyrl.mf
%{_texmfdistdir}/fonts/source/lh/base/lgcyrsp.mf
%{_texmfdistdir}/fonts/source/lh/base/lgcyrsym.mf
%{_texmfdistdir}/fonts/source/lh/base/lgcyru.mf
%{_texmfdistdir}/fonts/source/lh/base/lgengsym.mf
%{_texmfdistdir}/fonts/source/lh/base/lgidigit.mf
%{_texmfdistdir}/fonts/source/lh/base/lgilig.mf
%{_texmfdistdir}/fonts/source/lh/base/lgitalp.mf
%{_texmfdistdir}/fonts/source/lh/base/lgocyrac.mf
%{_texmfdistdir}/fonts/source/lh/base/lgpunct.mf
%{_texmfdistdir}/fonts/source/lh/base/lgrdigit.mf
%{_texmfdistdir}/fonts/source/lh/base/lgrlig.mf
%{_texmfdistdir}/fonts/source/lh/base/lgromp.mf
%{_texmfdistdir}/fonts/source/lh/base/lgrusi.mf
%{_texmfdistdir}/fonts/source/lh/base/lgrusl.mf
%{_texmfdistdir}/fonts/source/lh/base/lgrusu.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2comi.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2coml.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2comu.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2loi.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2lol.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2lou.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2slvi.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2slvl.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2slvu.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2upi.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2upl.mf
%{_texmfdistdir}/fonts/source/lh/base/lgt2upu.mf
%{_texmfdistdir}/fonts/source/lh/base/lkligtbl.mf
%{_texmfdistdir}/fonts/source/lh/base/llbligtb.mf
%{_texmfdistdir}/fonts/source/lh/base/llcligtb.mf
%{_texmfdistdir}/fonts/source/lh/base/lliligtb.mf
%{_texmfdistdir}/fonts/source/lh/base/llmligtb.mf
%{_texmfdistdir}/fonts/source/lh/base/llrligtb.mf
%{_texmfdistdir}/fonts/source/lh/base/llvligtb.mf
%{_texmfdistdir}/fonts/source/lh/base/lwnligs.mf
%{_texmfdistdir}/fonts/source/lh/base/lxpseudo.mf
%{_texmfdistdir}/fonts/source/lh/base/lycyracc.mf
%{_texmfdistdir}/fonts/source/lh/base/lypseudo.mf
%{_texmfdistdir}/fonts/source/lh/base/nodraw.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/irslb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/irsli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/irslo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/irslq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/irsltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbegin.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbmo10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbmo17.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbmo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbmo9.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbmr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbmr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbmr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbmr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbso10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbso17.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbso8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbso9.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbsr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbsr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbsr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbsr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbtl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsbto10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rscodes.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rslb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsliker.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rslo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rslq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsob10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsobx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsobx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsobx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsobx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsobx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsobx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsobxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsobxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsocc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsorm10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsorm5.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsorm6.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsorm7.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsorm8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsorm9.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsosl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsosl5.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsosl6.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsosl7.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsosl8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsosl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsoslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsoti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsqi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rssq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-XSlav/rsssdc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/00readme.txt
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccb10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccbx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccbx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccbx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccbx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccbx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccbxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/ccbxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concb10pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concbx10pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concbx12pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concbx5pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concbx6pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concbx7pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concbx8pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concbx9pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concbxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/concc9pt.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eob10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eobx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eobx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eobx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eobx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eobx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eobx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eobxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eobxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-conc/eoslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/ilhcsc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/ilhtt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/illhss8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/illhssb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/illhssi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbrbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbrsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbrsl17.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbrsl8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhbrsl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcb10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcbx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcbx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcbx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcbx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcbx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcbxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcbxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhccsc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcodes.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcr5.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcr6.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcr7.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcsl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhcti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhliker.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhsltl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/lhtl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/llhss8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/llhssb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-lcy/llhssi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/ilwnss8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/ilwnssb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/ilwnssi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/iwncsc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/iwntt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/lwnss8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/lwnssb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/lwnssi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbrbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbrsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbrsl17.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbrsl8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnbrsl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncb10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncbx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncbx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncbx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncbx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncbx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncbxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncbxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnccsc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncodes.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncr5.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncr6.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncr7.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncsl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wncti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnliker.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wnsltl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-ot2/wntl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/ilalb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/ilali8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/ilalo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/ilalq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/ilaltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labmo10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labmo17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labmo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labmo9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labmr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labmr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labmr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labmr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labso10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labso17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labso8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labso9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labsr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labsr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labsr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labsr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labtl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/labto10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/lacodes.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/lalb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/lali8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laliker.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/lalo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/lalq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laob10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laobx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laobx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laobx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laobx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laobx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laobx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laobxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laobxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laocc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laorm10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laorm5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laorm6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laorm7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laorm8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laorm9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laosl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laosl5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laosl6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laosl7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laosl8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laosl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laoslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laoti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/laqi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/lasq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2a/lassdc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/ilblb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/ilbli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/ilblo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/ilblq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/ilbltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbmo10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbmo17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbmo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbmo9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbmr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbmr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbmr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbmr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbso10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbso17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbso8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbso9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbsr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbsr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbsr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbsr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbtl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbbto10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbcodes.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lblb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbliker.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lblo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lblq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbob10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbobx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbobx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbobx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbobx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbobx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbobx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbobxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbobxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbocc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lborm10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lborm5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lborm6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lborm7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lborm8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lborm9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbosl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbosl5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbosl6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbosl7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbosl8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbosl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lboslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lboti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbqi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbsq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2b/lbssdc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/ilclb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/ilcli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/ilclo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/ilclq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/ilcltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbmo10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbmo17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbmo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbmo9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbmr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbmr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbmr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbmr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbso10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbso17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbso8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbso9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbsr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbsr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbsr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbsr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbtl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcbto10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lccodes.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lclb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcliker.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lclo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lclq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcob10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcobx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcobx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcobx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcobx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcobx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcobx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcobxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcobxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcocc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcorm10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcorm5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcorm6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcorm7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcorm8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcorm9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcosl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcosl5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcosl6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcosl7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcosl8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcosl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcoslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcoti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcqi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcsq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2c/lcssdc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ildlb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ildli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ildlo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ildlq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ildltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbmo10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbmo17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbmo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbmo9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbmr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbmr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbmr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbmr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbso10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbso17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbso8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbso9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbsr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbsr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbsr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbsr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbtl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldbto10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldcodes.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldlb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldliker.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldlo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldlq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldob10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldobx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldobx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldobx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldobx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldobx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldobx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldobxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldobxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldocc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldorm10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldorm5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldorm6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldorm7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldorm8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldorm9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldosl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldosl5.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldosl6.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldosl7.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldosl8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldosl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldoslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldoti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldqi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldsq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-t2d/ldssdc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/irxlb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/irxli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/irxlo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/irxlq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/irxltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbbx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbmo10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbmo17.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbmo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbmo9.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbmr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbmr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbmr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbmr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbso10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbso17.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbso8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbso9.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbsr10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbsr17.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbsr8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbsr9.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbtl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxbto10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxcodes.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxlb8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxli8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxliker.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxlo8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxlq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxltt8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxob10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxobx10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxobx5.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxobx6.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxobx7.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxobx8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxobx9.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxobxsl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxobxti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxocc10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxorm10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxorm5.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxorm6.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxorm7.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxorm8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxorm9.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxosl10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxosl5.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxosl6.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxosl7.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxosl8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxosl9.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxoslc9.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxoti10.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxqi8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxsq8.mf
%{_texmfdistdir}/fonts/source/lh/lh-x2/rxssdc10.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgbersta.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgberstb.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgberstc.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcacci.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcaccl.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcaccu.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcmodi.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcmodl.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcmodu.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcvaci.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcvacl.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgcvacu.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgt2slxi.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgt2slxl.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgt2slxu.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgunici.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgunicl.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lgunicu.mf
%{_texmfdistdir}/fonts/source/lh/nont2/lhberest.mf
%{_texmfdistdir}/fonts/source/lh/specific/lgcrusl.mf
%{_texmfdistdir}/fonts/source/lh/specific/lgcyrcl.mf
%{_texmfdistdir}/fonts/source/lh/specific/lgcyrcu.mf
%{_texmfdistdir}/fonts/source/lh/specific/lgnoncl.mf
%{_texmfdistdir}/fonts/source/lh/specific/lgnoncu.mf
%{_texmfdistdir}/fonts/source/lh/specific/lgrucl.mf
%{_texmfdistdir}/fonts/source/lh/specific/lgrucu.mf
%{_texmfdistdir}/tex/latex/lh/lh-lcy.sty
%{_texmfdistdir}/tex/latex/lh/lh-lcyccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-lcyxccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-ot2.sty
%{_texmfdistdir}/tex/latex/lh/lh-ot2ccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-ot2xccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-t2accr.sty
%{_texmfdistdir}/tex/latex/lh/lh-t2axccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-t2bccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-t2bxccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-t2cccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-t2cxccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-x2ccr.sty
%{_texmfdistdir}/tex/latex/lh/lh-x2xccr.sty
%{_texmfdistdir}/tex/latex/lh/nfssfox.tex
%{_texmfdistdir}/tex/plain/lh/testfox.tex
%{_texmfdistdir}/tex/plain/lh/testkern.tex
%doc %{_texmfdistdir}/doc/fonts/lh/README
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/beresta.tex
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/berestax.tex
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/lacodes.tex
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/lbcodes.tex
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/lccodes.tex
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/ldcodes.tex
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/rxcodes.tex
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/txcodes.tex
%doc %{_texmfdistdir}/doc/fonts/lh/beresta/yycodes.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/allenc.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/allenc0.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/allenc1.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/allenc2.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/allenc3.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/allenc4.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog-beresta.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog-short.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog.lh
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog1.lh
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog1.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog2.lh
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog2.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog3.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog4.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog5.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog6.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/katalog7.t2
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/lh-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/lh-text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/lh-texx.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/lh-texy.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2a-fmap-short.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2a-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2a-text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2b-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2b-text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2c-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2c-text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2d-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/t2d-text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/testLHtxt.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/uc-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/wn-comp.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/wn-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/wn-text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/x2-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/x2-text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/xsl-fmap.tex
%doc %{_texmfdistdir}/doc/fonts/lh/fonttest/xsl-text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/install
%doc %{_texmfdistdir}/doc/fonts/lh/lhfonts/T1inT2.en
%doc %{_texmfdistdir}/doc/fonts/lh/lhfonts/fonttest.en
%doc %{_texmfdistdir}/doc/fonts/lh/lhfonts/lhfont35.en
%doc %{_texmfdistdir}/doc/fonts/lh/lhfonts/lhfont35.ru
%doc %{_texmfdistdir}/doc/fonts/lh/lhfonts/lhfonts.hst
%doc %{_texmfdistdir}/doc/fonts/lh/manifest.txt
%doc %{_texmfdistdir}/doc/fonts/lh/readme35c.1st
%doc %{_texmfdistdir}/doc/fonts/lh/readme35g.1st
%doc %{_texmfdistdir}/doc/fonts/lh/samples/lh-lcy.tex
%doc %{_texmfdistdir}/doc/fonts/lh/samples/lh-lcytext.tex
%doc %{_texmfdistdir}/doc/fonts/lh/samples/lh-ot2.tex
%doc %{_texmfdistdir}/doc/fonts/lh/samples/lh-ot2text.tex
%doc %{_texmfdistdir}/doc/fonts/lh/samples/lh-t2a.tex
%doc %{_texmfdistdir}/doc/fonts/lh/samples/lh-t2atext.tex
#- source
%doc %{_texmfdistdir}/source/fonts/lh/dvidrv.mfj
%doc %{_texmfdistdir}/source/fonts/lh/dvidrvlh.mfj
%doc %{_texmfdistdir}/source/fonts/lh/tex/00readme.txt
%doc %{_texmfdistdir}/source/fonts/lh/tex/01cm-lh.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/03cm-wn.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/04cm-vf.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/11ex-rs.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/11ex-rx.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/12ex-la.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/13ex-lb.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/14ex-lc.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/15ex-ld.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/20cm-ct.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/21cm-ic.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/22cm-wc.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/23cm-mc.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/24cm-kc.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/25cm-uc.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/30cm-lx.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/31cm-ix.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/32cm-wx.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/33cm-mx.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/34cm-kx.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/46cm-ly.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/46cm-lz.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/47ex-tx.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/91berest.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/92check.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/92cm-xx.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/99-CMstd.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/99-T2enc.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/99allenc.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/99tstenc.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/cfhead.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/cfstdedt.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/cod-edt.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/enc-t2.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntaddcm.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntaddec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntallcm.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntallec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntbasec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntbercm.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntberec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntbricm.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntbriec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntconcm.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntconec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntinvcm.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntinvec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntmincm.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fntminec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fnttstcm.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/fnttstec.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/likerdat.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/likergrp.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/likermac.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/rliker.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/setter.tex
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh-XSlav/00readme
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh-lcy/00readme
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh-ot2/00readme
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh-t2a/00readme
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh-t2b/00readme
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh-t2c/00readme
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh-t2d/00readme
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh-x2/00readme
%doc %{_texmfdistdir}/source/fonts/lh/tex/wrk/lh_temp/00readme
%doc %{_texmfdistdir}/source/latex/lh/00readme.txt
%doc %{_texmfdistdir}/source/latex/lh/lcyfonts.fdd
%doc %{_texmfdistdir}/source/latex/lh/lcyfonts.ins
%doc %{_texmfdistdir}/source/latex/lh/nfssfox.dtx
%doc %{_texmfdistdir}/source/latex/lh/nfssfox.ins
%doc %{_texmfdistdir}/source/latex/lh/ot2fonts.fdd
%doc %{_texmfdistdir}/source/latex/lh/ot2fonts.ins
%doc %{_texmfdistdir}/source/latex/lh/t2ccfonts.fdd
%doc %{_texmfdistdir}/source/latex/lh/t2ccfonts.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
