# revision 23092
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-kurmanji
Version:	20111103
Release:	2
Summary:	Kurmanji hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-kurmanji.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Kurmanji (Northern Kurdish) as spoken
in Turkey and by the Kurdish diaspora in Europe, in T1/EC and
UTF-8 encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-kurmanji
%_texmf_language_def_d/hyphen-kurmanji
%_texmf_language_lua_d/hyphen-kurmanji

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-kurmanji <<EOF
\%\% from hyphen-kurmanji:
kurmanji loadhyph-kmr.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-kurmanji <<EOF
\%\% from hyphen-kurmanji:
\addlanguage{kurmanji}{loadhyph-kmr.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-kurmanji <<EOF
-- from hyphen-kurmanji:
	['kurmanji'] = {
		loader = 'loadhyph-kmr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-kmr.pat.txt',
		hyphenation = '',
	},
EOF
