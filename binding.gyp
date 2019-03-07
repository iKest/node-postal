{
    "targets": [
        {
            "target_name": "expand",
            "sources": [
                "src/expand.cc"
            ],
            "libraries": [
                "../src/thrid_party/lib"
               
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                 "src/thrid_party/include"
            ]
        },
        {
            "target_name": "parser",
            "sources": [
                "src/parser.cc"
            ],
            "libraries": [
                "../src/thrid_party/lib"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "src/thrid_party/include"
            ]
        }
    ]
}
