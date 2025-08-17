
## Chosen authentication for boto3 + Bedrock
There are many ways to authenticate with AWS services using `boto3`, but the recommended way is to use the `boto3` library.
We capture the following from the user and store it securely:
- AWS Access Key ID
- AWS Secret Access Key
- AWS Region - this is the region where the Bedrock service is available and where the model will be deployed. We use the region to show the available models 

In the future we can expand this to include other authentication methods, such as:
- TODO: [Bedrock API Key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html) - short or long term key for API access without any other secret sharing, in line with other providers like OpenAI or Anthropic configuration
- Lower preference: AWS Profile Based Authentication (AWS Session Token) - allows for temporary credentials and assume the role of execution context

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

#### [RECOMMENDED & CHOSEN] Configure multiple indexes
```toml
# pyproject.toml
# Index for boto3 package
[[tool.uv.index]]
name = "boto3"
url = "https://pypi.org/simple"

# Default index for all other packages
[[tool.uv.index]]
url = "https://download.pytorch.org/whl/cpu"
# This will allow uv to resolve dependencies from both indexes
```

Then run:
```shell
uv add boto3
```
---

#### Other Options


##### Use `--index-strategy unsafe-best-match`

```shell
uv add boto3 --index-strategy unsafe-best-match
```

##### Use `--frozen` flag
```shell
uv add boto3 --frozen
```
This will skip the locking and syncing process, allowing you to add the package without resolving dependencies.