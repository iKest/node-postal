{
    "targets": [
        {
            "target_name": "expand",
            "sources": [
                "src/expand.cc"
            ],
            "libraries": ["C:/msys64/mingw64/lib", "-lpostal"],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                 "C:/msys64/mingw64/include"
            ]
        },
        {
            "target_name": "parser",
            "sources": [
                "src/parser.cc"
            ],
            "libraries": ["C:/msys64/mingw64/lib", "-lpostal"],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "C:/msys64/mingw64/include"
            ]
        }
    ]
}
