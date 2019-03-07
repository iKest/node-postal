{
    "targets": [
        {
            "target_name": "expand",
            "sources": [
                "src/expand.cc"
            ],
            "libraries": [
                "-lC:/msys64/home/Konstantin/libpostal/libpostal.lib",
                "-L/C:/msys64/home/Konstantin/libpostal/.lib"
               
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                 "C:/msys64/home/Konstantin/libpostal"
            ]
        },
        {
            "target_name": "parser",
            "sources": [
                "src/parser.cc"
            ],
            "libraries": [
                "-lC:/msys64/home/Konstantin/libpostal/libpostal.lib",
                "-L/C:/msys64/home/Konstantin/libpostal/.lib"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "C:/msys64/home/Konstantin/libpostal"
            ]
        }
    ]
}
