Copied from [Bedrock Converse API Example](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime/client/converse.html#)


```python
response = client.converse(
    modelId='string',
    messages=[
        {
            'role': 'user'|'assistant',
            'content': [
                {
                    'text': 'string',
                    'image': {
                        'format': 'png'|'jpeg'|'gif'|'webp',
                        'source': {
                            'bytes': b'bytes',
                            's3Location': {
                                'uri': 'string',
                                'bucketOwner': 'string'
                            }
                        }
                    },
                    'document': {
                        'format': 'pdf'|'csv'|'doc'|'docx'|'xls'|'xlsx'|'html'|'txt'|'md',
                        'name': 'string',
                        'source': {
                            'bytes': b'bytes',
                            's3Location': {
                                'uri': 'string',
                                'bucketOwner': 'string'
                            },
                            'text': 'string',
                            'content': [
                                {
                                    'text': 'string'
                                },
                            ]
                        },
                        'context': 'string',
                        'citations': {
                            'enabled': True|False
                        }
                    },
                    'video': {
                        'format': 'mkv'|'mov'|'mp4'|'webm'|'flv'|'mpeg'|'mpg'|'wmv'|'three_gp',
                        'source': {
                            'bytes': b'bytes',
                            's3Location': {
                                'uri': 'string',
                                'bucketOwner': 'string'
                            }
                        }
                    },
                    'toolUse': {
                        'toolUseId': 'string',
                        'name': 'string',
                        'input': {...}|[...]|123|123.4|'string'|True|None
                    },
                    'toolResult': {
                        'toolUseId': 'string',
                        'content': [
                            {
                                'json': {...}|[...]|123|123.4|'string'|True|None,
                                'text': 'string',
                                'image': {
                                    'format': 'png'|'jpeg'|'gif'|'webp',
                                    'source': {
                                        'bytes': b'bytes',
                                        's3Location': {
                                            'uri': 'string',
                                            'bucketOwner': 'string'
                                        }
                                    }
                                },
                                'document': {
                                    'format': 'pdf'|'csv'|'doc'|'docx'|'xls'|'xlsx'|'html'|'txt'|'md',
                                    'name': 'string',
                                    'source': {
                                        'bytes': b'bytes',
                                        's3Location': {
                                            'uri': 'string',
                                            'bucketOwner': 'string'
                                        },
                                        'text': 'string',
                                        'content': [
                                            {
                                                'text': 'string'
                                            },
                                        ]
                                    },
                                    'context': 'string',
                                    'citations': {
                                        'enabled': True|False
                                    }
                                },
                                'video': {
                                    'format': 'mkv'|'mov'|'mp4'|'webm'|'flv'|'mpeg'|'mpg'|'wmv'|'three_gp',
                                    'source': {
                                        'bytes': b'bytes',
                                        's3Location': {
                                            'uri': 'string',
                                            'bucketOwner': 'string'
                                        }
                                    }
                                }
                            },
                        ],
                        'status': 'success'|'error'
                    },
                    'guardContent': {
                        'text': {
                            'text': 'string',
                            'qualifiers': [
                                'grounding_source'|'query'|'guard_content',
                            ]
                        },
                        'image': {
                            'format': 'png'|'jpeg',
                            'source': {
                                'bytes': b'bytes'
                            }
                        }
                    },
                    'cachePoint': {
                        'type': 'default'
                    },
                    'reasoningContent': {
                        'reasoningText': {
                            'text': 'string',
                            'signature': 'string'
                        },
                        'redactedContent': b'bytes'
                    },
                    'citationsContent': {
                        'content': [
                            {
                                'text': 'string'
                            },
                        ],
                        'citations': [
                            {
                                'title': 'string',
                                'sourceContent': [
                                    {
                                        'text': 'string'
                                    },
                                ],
                                'location': {
                                    'documentChar': {
                                        'documentIndex': 123,
                                        'start': 123,
                                        'end': 123
                                    },
                                    'documentPage': {
                                        'documentIndex': 123,
                                        'start': 123,
                                        'end': 123
                                    },
                                    'documentChunk': {
                                        'documentIndex': 123,
                                        'start': 123,
                                        'end': 123
                                    }
                                }
                            },
                        ]
                    }
                },
            ]
        },
    ],
    system=[
        {
            'text': 'string',
            'guardContent': {
                'text': {
                    'text': 'string',
                    'qualifiers': [
                        'grounding_source'|'query'|'guard_content',
                    ]
                },
                'image': {
                    'format': 'png'|'jpeg',
                    'source': {
                        'bytes': b'bytes'
                    }
                }
            },
            'cachePoint': {
                'type': 'default'
            }
        },
    ],
    inferenceConfig={
        'maxTokens': 123,
        'temperature': ...,
        'topP': ...,
        'stopSequences': [
            'string',
        ]
    },
    toolConfig={
        'tools': [
            {
                'toolSpec': {
                    'name': 'string',
                    'description': 'string',
                    'inputSchema': {
                        'json': {...}|[...]|123|123.4|'string'|True|None
                    }
                },
                'cachePoint': {
                    'type': 'default'
                }
            },
        ],
        'toolChoice': {
            'auto': {}
            ,
            'any': {}
            ,
            'tool': {
                'name': 'string'
            }
        }
    },
    guardrailConfig={
        'guardrailIdentifier': 'string',
        'guardrailVersion': 'string',
        'trace': 'enabled'|'disabled'|'enabled_full'
    },
    additionalModelRequestFields={...}|[...]|123|123.4|'string'|True|None,
    promptVariables={
        'string': {
            'text': 'string'
        }
    },
    additionalModelResponseFieldPaths=[
        'string',
    ],
    requestMetadata={
        'string': 'string'
    },
    performanceConfig={
        'latency': 'standard'|'optimized'
    }
)
```