import json

from anthropic import AsyncAnthropic
from openai import AsyncOpenAI
from google import genai
import boto3 # TODO: use aioboto3 for async support later on
import asyncio

def _get_boto3_client(access_key, secret_key, region):
    return boto3.client(
        "bedrock",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )

def _get_inference_profile_prefix(region: str) -> str:
    if region.startswith("us-"):
        return "us"
    elif region.startswith("eu-"):
        return "eu"
    elif region.startswith("ap-"):
        return "apac"
    else:
        return ""

def _list_models_sync(access_key: str, secret_key: str, region: str) -> list[str]:
    client = boto3.client(
        "bedrock",
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    response = client.list_foundation_models()

    inference_profile_prefix = _get_inference_profile_prefix(region)

    invokable_ids = []
    for m in response["modelSummaries"]:
        model_id = m["modelId"]
        provider = m.get("providerName", "")
        if provider.lower() != "anthropic":
            # skip non-Anthropic models
            continue

        if "inferenceTypesSupported" in m and ("INFERENCE_PROFILE" in m["inferenceTypesSupported"]):
            # use the profile ARN (required for some Anthropic models etc.)
            invokable_ids.append(f"{inference_profile_prefix}.{model_id}")
        else:
            # use modelId directly
            invokable_ids.append(model_id)

    return invokable_ids


async def list_available_openai_compatible_models(url: str, api_key: str) -> list[str]:
    client = AsyncOpenAI(api_key=api_key, base_url=url)
    models = (await client.models.list()).data
    if models:
        return list(map(lambda x: x.id, models))
    return []


async def list_available_anthropic_models(api_key: str) -> list[str]:
    client = AsyncAnthropic(api_key=api_key)
    return list(map(lambda x: x.id, (await client.models.list(limit=50)).data))


async def list_available_google_models(api_key: str) -> list[str]:
    client = genai.Client(api_key=api_key)
    return list(map(lambda x: x.name, client.models.list(config={"page_size": 50})))


async def list_available_bedrock_models(access_key: str, secret_key: str, region: str) -> list[str]:
    return await asyncio.to_thread(_list_models_sync, access_key, secret_key, region)
