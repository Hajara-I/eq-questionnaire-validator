import ast
import os.path

from setuptools import setup

try:
    from eq_validator import __version__ as version
except ImportError:
    version = str(
        ast.literal_eval(
            open(
                os.path.join(
                    os.path.dirname(__file__), "eq_validator", "__init__.py"
                ),
                "r",
            )
            .read()
            .split("=")[-1]
            .strip()
        )
    )

setup(
    name="eq_validator",
    version=version,
    description="Translations infrastructure for EQ Questionnaire Runner",
    url="https://github.com/Hajara-I/eq-questionnaire-validator",
    author="Hajara-I",
    author_email="",
    license="MIT",
    packages=["eq_validator", "eq_validator.cli"],
    install_requires=[
        "python",
        "Flask",
        "jsonpointer",
        "structlog",
        "python-dateutil",
        "jsonschema",
        "jsonpath-rw",
        "jsonpath-rw-ext",
        "eq-translations"
    ],
    zip_safe=False,
)