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
            "libraries": ["-llibpostal"],
            "library_dirs": ["<(base_path)/bin"],
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
            "library_dirs": ["<(base_path)/bin"],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "<(base_path)/include"
            ]
        }
    ]
}
