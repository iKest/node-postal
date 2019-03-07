{
    "targets": [
        {
            "target_name": "expand",
            "sources": [
                "src/expand.cc"
            ],
            "libraries": ["-LC:/msys64/mingw64/lib", "-llibpostal"],
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
            "libraries": ["-LC:/msys64/mingw64/lib", "-llibpostal"],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "C:/msys64/mingw64/include"
            ]
        }
    ]
}
