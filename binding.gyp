{
    "variables": {
        "base_path": "C:\msys64\mingw64"
    },
    "targets": [
        {
            "target_name": "expand",
            "sources": [
                "src/expand.cc"
            ],
            "libraries": ["-lpostal"],
            "library_dirs": ["<(base_path)/lib"],
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
            "libraries": ["-lpostal"],
            "library_dirs": ["<(base_path)/lib"],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "<(base_path)/include"
            ]
        }
    ]
}
