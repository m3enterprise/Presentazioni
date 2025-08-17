


## Adding `boto3` to `pyproject.toml`

```shell
uv add boto3 
```

Gives an error:
```text
uv add boto3
  × No solution found when resolving dependencies for split (python_full_version == '3.11.*' and platform_machine == 'aarch64' and sys_platform == 'linux'):
  ╰─▶ Because only certifi==2022.12.7 is available and docling>=2.43.0 depends on certifi>=2024.7.4, we can conclude that docling>=2.43.0 cannot be used.
      And because only the following versions of docling are available:
          docling<=2.43.0
          docling==2.44.0
      and your project depends on docling>=2.43.0, we can conclude that your project's requirements are unsatisfiable.

      hint: `certifi` was found on https://download.pytorch.org/whl/cpu, but not at the requested version (certifi>=2024.7.4). A compatible version may be
      available on a subsequent index (e.g., https://pypi.org/simple). By default, uv will only consider versions that are published on the first index that
      contains a given package, to avoid dependency confusion attacks. If all indexes are equally trusted, use `--index-strategy unsafe-best-match` to consider
      all versions from all indexes, regardless of the order in which they were defined.
  help: If you want to add the package regardless of the failed resolution, provide the `--frozen` flag to skip locking and syncing.
```

### Workaround options

#### Use `--index-strategy unsafe-best-match`

```shell
uv add boto3 --index-strategy unsafe-best-match
```

####