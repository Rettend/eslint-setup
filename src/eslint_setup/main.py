import os
import json


def main():
    with open("eslint.config.js", "w") as f:
        f.write("import antfu from '@antfu/eslint-config'\n\nexport default antfu()")

    os.makedirs(".vscode", exist_ok=True)
    settings_file = ".vscode/settings.json"

    if os.path.exists(settings_file):
        with open(settings_file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    config = {
        "prettier.enable": False,
        "editor.formatOnSave": False,
        "editor.codeActionsOnSave": {
            "source.fixAll.eslint": "explicit",
            "source.organizeImports": "never",
        },
        "eslint.rules.customizations": [
            {"rule": "style/*", "severity": "warn", "fixable": True},
            {"rule": "format/*", "severity": "warn", "fixable": True},
            {"rule": "*-indent", "severity": "warn", "fixable": True},
            {"rule": "*-spacing", "severity": "warn", "fixable": True},
            {"rule": "*-spaces", "severity": "warn", "fixable": True},
            {"rule": "*-order", "severity": "warn", "fixable": True},
            {"rule": "*-dangle", "severity": "warn", "fixable": True},
            {"rule": "*-newline", "severity": "warn", "fixable": True},
            {"rule": "*quotes", "severity": "warn", "fixable": True},
            {"rule": "*semi", "severity": "warn", "fixable": True},
        ],
        "eslint.validate": [
            "javascript",
            "javascriptreact",
            "typescript",
            "typescriptreact",
            "vue",
            "html",
            "markdown",
            "json",
            "jsonc",
            "yaml",
            "toml",
            "xml",
            "gql",
            "graphql",
            "astro",
            "svelte",
            "css",
            "less",
            "scss",
            "pcss",
            "postcss",
        ],
    }
    data.update(config)

    with open(settings_file, "w") as f:
        json.dump(data, f, indent=2)
    
    print("eslint_setup done")


if __name__ == "__main__":
    main()
