#!/usr/bin/env python3
"""Test GLM model setup through Anthropic-compatible API"""

import anthropic

# Configure for GLM models through Anthropic-compatible API
client = anthropic.Anthropic(
    api_key="your-zhipuai-api-key",  # Need to get this from ZhipuAI
    base_url="https://open.bigmodel.cn/api/anthropic"
)

# Test with GLM-4-6 model
message = client.messages.create(
    model="glm-4-6",  # Can also use: glm-4-5, glm-4-air, etc.
    max_tokens=1024,
    messages=[{"role": "user", "content": "Test: Are you working as Kaitiaki Aronui overseer?"}]
)

print(message.content)
