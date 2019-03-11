{
    "variables": {
        "base_path": "C:/msys64/mingw64"
    },
    "targets": [
        {
            "target_name": "expand",
            "sources": [
                "src/expand.cc"
            ],
            "libraries": ["<(base_path)/bin/libpostal.lib"],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                 "<(base_path)/include"
            ]
        },
        {
            "target_name": "parser",
            "sources": [
                "src/parser.cc"
            ],
            "libraries": ["-llibpostal"],
            "library_dirs": ["-L<(base_path)/lib"],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "<(base_path)/include"
            ]
        }
    ]
}
