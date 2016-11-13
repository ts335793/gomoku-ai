load("//tensorflow/core:platform/default/build_config.bzl", "tf_proto_library")

package(default_visibility = ["//gomoku"])

cc_library(
    name = "board",
    hdrs = ["board.h"],
    srcs = ["board.cc"],
    deps = [
        "//tensorflow/core:framework_headers_lib",
        "//third_party/eigen3",
    ],
)

cc_test(
    name = "board_test",
    srcs = ["board_test.cc"],
    deps = [
        ":board",
        "//tensorflow/core:test",
    ],
)

cc_library(
    name = "feature",
    hdrs = ["feature.h"],
    srcs = ["feature.cc"],
    deps = [
        ":board",
        "//tensorflow/core:framework_headers_lib",
        "//third_party/eigen3",
    ],
)

cc_test(
    name = "feature_test",
    srcs = ["feature_test.cc"],
    deps = [
        ":feature",
        "//tensorflow/core:test",
    ],
)

cc_library(
    name = "actor",
    hdrs = ["actor.h"],
    srcs = ["actor.cc"],
    deps = [
        ":board",
        ":feature",
    ],
)

tf_proto_library(
    name = "recording_proto",
    srcs = ["recording.proto"],
    cc_api_version = 2,
    visibility = ["//gomoku"],
)