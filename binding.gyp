{
    "targets": [
        {
            "target_name": "expand",
            "sources": [
                "src/expand.cc"
            ],
            "libraries": [
                "-lpostal", "../../../thrid_party/lib"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "../thrid_party/include"
            ]
        },
        {
            "target_name": "parser",
            "sources": [
                "src/parser.cc"
            ],
            "libraries": [
                "-lpostal", "../../../thrid_party/lib"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "../thrid_party/include"
            ]
        }
    ]
}
