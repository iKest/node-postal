{
    "targets": [
        {
            "target_name": "expand",
            "sources": [
                "src/expand.cc"
            ],
            "libraries": [
                "-L C:\msys64\home\Konstantin\libpostal\libpostal.lib"
               
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                 "C:\msys64\home\Konstantin\libpostal\src"
            ]
        },
        {
            "target_name": "parser",
            "sources": [
                "src/parser.cc"
            ],
            "libraries": [
                "-L C:\msys64\home\Konstantin\libpostal\libpostal.lib"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "C:\msys64\home\Konstantin\libpostal\src"
            ]
        }
    ]
}
