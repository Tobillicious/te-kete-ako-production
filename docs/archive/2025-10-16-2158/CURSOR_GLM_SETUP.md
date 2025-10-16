# 🚀 Setting Up GLM Zhipu AI in Cursor IDE

**Your Subscription:** GLM Coding Plan (¥20/月)  
**Purpose:** Use GLM-4.6 and other models for coding assistance in Cursor  
**Benefit:** 1/7 price of Claude, 3x usage, supports networking + multimodal

---

## ⚡ Quick Setup (3 Steps)

### Step 1: Get Your GLM API Key

1. Go to [Zhipu AI Platform](https://open.bigmodel.cn)
2. Log in to your account
3. Navigate to API Keys section
4. Copy your API key (starts with your subscription key)

### Step 2: Configure Cursor IDE

#### Method A: Using OpenAI-Compatible Endpoint

**Cursor Settings:**
1. Open Cursor Settings (`Cmd + ,` or `Ctrl + ,`)
2. Go to **"Models"** section
3. Click **"Add Model"** or **"OpenAI API Key"**
4. Add custom configuration:

```
Base URL: https://open.bigmodel.cn/api/paas/v4/
API Key: [Your GLM API Key]
Model: glm-4.6
```

**Note:** Zhipu AI provides OpenAI-compatible API, so Cursor can use it directly!

#### Method B: Using as Override

In Cursor settings, you can override the model provider:

```json
{
  "models": {
    "override": {
      "provider": "openai-compatible",
      "baseURL": "https://open.bigmodel.cn/api/paas/v4/",
      "apiKey": "YOUR_GLM_API_KEY",
      "model": "glm-4.6"
    }
  }
}
```

### Step 3: Test It!

1. Open any file in Te Kete Ako project
2. Press `Cmd + K` (or `Ctrl + K`) to activate Cursor AI
3. Ask: "Explain this code"
4. Verify it's using GLM model (should be faster and cost-effective!)

---

## 🎯 Recommended Models for Different Tasks

### For Coding (Your Main Use Case):

**GLM-4.6** - Flagship (Best for complex code)
- **Context:** 200K tokens (can see entire files!)
- **Use for:** Complex refactoring, architecture design, debugging
- **Command:** Set as default model in Cursor

**GLM-4.5-Air** - Best Price/Performance
- **Context:** 128K tokens
- **Use for:** Quick edits, code completion, standard coding tasks
- **Command:** Use for day-to-day coding

**GLM-Z1-AirX** - Fastest (8x speed)
- **Context:** 32K tokens
- **Use for:** Quick answers, simple edits, autocomplete
- **Command:** Use when you need instant responses

### For Te Kete Ako Specific Tasks:

**Content Generation:** GLM-4.6 or GLM-4.5
**Math Content:** GLM-Z1-Air (enhanced reasoning)
**Visual Analysis:** GLM-4.5V (if you need to analyze images/videos)
**Quick Scripts:** GLM-4.5-Air or GLM-Z1-AirX

---

## 💻 Cursor IDE Integration Examples

### Example 1: Generate Python Script

In Cursor, press `Cmd + K` and ask:
```
"Create a script to generate Year 9 Science lessons about 
traditional Māori astronomy with cultural protocols"
```

With GLM-4.6's 200K context, it can reference your entire codebase structure!

### Example 2: Refactor Existing Code

Select code in any file, press `Cmd + K`:
```
"Refactor this to use environment variables instead of 
hardcoded values, following our project patterns"
```

### Example 3: Debug Issues

In problematic file, press `Cmd + L` for chat:
```
"Why isn't this worksheet generating correctly? 
Check against our lesson template structure"
```

### Example 4: Code Review

Select code, ask:
```
"Review this for security issues, especially API key exposure"
```

GLM-4.6 can help catch the security blunders we documented!

---

## 🔧 Advanced Configuration

### Using Multiple GLM Models in Cursor

You can configure multiple models and switch between them:

**Settings → Models → Add Multiple:**

1. **Primary (GLM-4.6)** - For complex tasks
   ```
   Name: GLM-4.6 Flagship
   Base URL: https://open.bigmodel.cn/api/paas/v4/
   Model: glm-4.6
   ```

2. **Fast (GLM-Z1-AirX)** - For quick tasks
   ```
   Name: GLM-Z1 Fast
   Base URL: https://open.bigmodel.cn/api/paas/v4/
   Model: glm-z1-airx
   ```

3. **Economical (GLM-4.5-Air)** - For bulk work
   ```
   Name: GLM-4.5 Air
   Base URL: https://open.bigmodel.cn/api/paas/v4/
   Model: glm-4.5-air
   ```

Then switch between them in Cursor's model selector!

---

## 🎓 Specific Use Cases for Te Kete Ako Development

### 1. Generate Content Scripts
```
"Create a Python script that generates Year 8 Social Studies 
lessons about Te Tiriti o Waitangi, following our 6-level 
nested structure and cultural protocols"
```

**Use:** GLM-4.6 (needs full context understanding)

### 2. Fix Bugs
```
"Debug why the worksheet print CSS isn't working correctly"
```

**Use:** GLM-4.5-Air (sufficient for bug fixing)

### 3. Code Review
```
"Review this multi-agent script for security issues and 
potential improvements"
```

**Use:** GLM-4.6 (thorough analysis)

### 4. Quick Edits
```
"Add error handling to this function"
```

**Use:** GLM-Z1-AirX (fast response)

### 5. Refactoring
```
"Refactor these 5 similar scripts into one reusable module"
```

**Use:** GLM-4.6 (complex refactoring needs big context)

---

## 💰 Cost Optimization with Cursor

**Your GLM Coding Plan includes:**
- ¥20/month base tier
- Access to GLM-4.6 flagship
- 3x usage compared to Claude equivalent
- Supports networking search
- Multimodal understanding

**Best practices:**
- Use GLM-4.6 for complex/important tasks
- Use GLM-4.5-Air for routine coding
- Use GLM-Z1-AirX for quick answers
- This maximizes your subscription value!

---

## 🔍 Verification

### Test if it's working:

1. **Open Cursor**
2. **Press `Cmd + L`** (chat)
3. **Ask:** "What model are you?"
4. **Should respond:** Using GLM-4.6 or whichever model you configured

### Common Issues:

**If connection fails:**
- Check API key is correct
- Verify base URL: `https://open.bigmodel.cn/api/paas/v4/`
- Ensure subscription is active
- Check network connection (VPN if needed?)

**If model not responding well:**
- Try different model (GLM-4.5-Air vs GLM-4.6)
- Check context window limits
- Verify API quota not exceeded

---

## 📚 Documentation Links

- **Zhipu AI Docs:** https://docs.bigmodel.cn
- **Model Overview:** https://docs.bigmodel.cn/cn/guide/start/model-overview
- **API Guide:** Check Zhipu docs for API usage
- **Cursor Docs:** Check Cursor documentation for custom model setup

---

## 🎯 Next Steps for You

1. **Get your GLM API key** from Zhipu platform
2. **Configure Cursor** with GLM-4.6
3. **Test on simple task** (explain a code file)
4. **Gradually switch** more tasks to GLM
5. **Document quality** comparison with other models
6. **Optimize usage** based on task type

---

## 💡 Pro Tips

**For Te Kete Ako development:**
- GLM-4.6's 200K context can hold entire lesson plans + examples
- Perfect for generating comprehensive educational content
- May have better cultural sensitivity (Chinese AI understanding cultural protocols)
- Coding Plan designed specifically for IDE integration
- Fast models (AirX) great for rapid iteration

**Cost savings:**
- Switch primary IDE model from Claude/GPT-4 to GLM
- Save expensive API calls for when absolutely needed
- GLM subscription gives you predictable monthly cost

---

**Your GLM Coding Plan subscription is designed exactly for this use case!**

Let me know if you need help with specific Cursor configuration! 🚀

