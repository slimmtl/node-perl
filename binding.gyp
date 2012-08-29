{
    'targets': [
        {
            'target_name': 'perl',
            'sources': [
                './src/perl_bindings.cc',
                './src/perlxsi.c'
            ],
            'libraries': [
                '<!@(perl -MExtUtils::Embed -e ldopts)'
            ],
            'cflags!': [ '-fno-exceptions' ],
            'cflags_cc!': [ '-fno-exceptions' ],
            'cflags': [
                '<!@(perl utils/libperl.pl)'
                '<!@(perl -MExtUtils::Embed -e ccopts)'
            ]
        },
    ]
}
