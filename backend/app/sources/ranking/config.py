DOCUMENTATION_KEYWORDS = {

    "readme",
    "guide",
    "manual",
    "documentation",
    "docs",
    "architecture",
    "design",
    "overview",
    "getting_started",
    "quickstart",

}

CONFIGURATION_FILENAMES = {

    "package.json",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",

    "requirements.txt",
    "pyproject.toml",
    "poetry.lock",
    "setup.py",

    "dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",

    "makefile",

    "platformio.ini",

    "pubspec.yaml",

    "pom.xml",
    "build.gradle",

}

SOURCE_DIRECTORIES = {

    "src",
    "app",
    "backend",
    "frontend",
    "server",
    "client",
    "core",
    "lib",
    "modules",
    "services",
    "components",

}

LOW_PRIORITY_DIRECTORIES = {

    "tests",
    "test",
    "examples",
    "sample",
    "samples",

}

MAX_RESULTS = 100

MINIMUM_SCORE = 20

WEIGHTS = {

    "semantic": 60,

    "query": 20,

    "documentation": 10,

    "configuration": 5,

    "directory": 3,

    "source_code": 5,

    "size": 2,

}