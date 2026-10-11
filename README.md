# VerifyPulse MCP Server & Autonomous Agent Client

Public Model Context Protocol (MCP) server card and client interface for **VerifyPulse** (`https://verifypulse-seven.vercel.app`), the sub-140ms B2B email deliverability, DNS security, and lead intelligence engine on Base L2 USDC.

---

## ⚡ What is VerifyPulse?

VerifyPulse provides developer-grade email verification and domain diagnostics via x402 machine-to-machine micropayments and standard REST APIs:
- **RFC 5322 Syntax & Mailbox Format**
- **Authoritative DNS MX Record Queries**
- **3,800+ Disposable & Temporary Domain Filtering**
- **Zero-Send SMTP Handshake Emulation (`HELO` + `MAIL FROM` + `RCPT TO`)**
- **RFC 7208 SPF 10-Lookup Limit & DMARC Alignment Inspector**

---

## 🤖 Remote MCP Server (Streamable HTTP)

Autonomous AI agents (Claude Desktop, Cursor, Antigravity, OpenHands) can connect directly to the hosted VerifyPulse MCP server:

```json
{
  "mcpServers": {
    "verifypulse": {
      "command": "npx",
      "args": ["-y", "@verifypulse/mcp-server"],
      "env": {
        "VERIFYPULSE_API_URL": "https://verifypulse-seven.vercel.app/mcp"
      }
    }
  }
}
```

Or connect via streamable HTTP endpoint:
- **Endpoint**: `POST https://verifypulse-seven.vercel.app/mcp`
- **Protocol**: JSON-RPC 2.0 (Model Context Protocol)

---

## 💎 On-Chain Base Mainnet x402 Micropayments

VerifyPulse supports the HTTP 402 Payment Required specification on Base Mainnet (Chain ID 8453). Agents without credit cards can pay per call using USDC:

- **Token**: USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` on Base)
- **Settlement Wallet**: `0x42871B99A3AA942D3B8EC7E43D37979886E856cA`
- **Unit Cost**: $0.01 USDC per email verification call

### Available Endpoints:
- `GET https://verifypulse-seven.vercel.app/v1/x402/verify-email?email=test@example.com` ($0.01 USDC)
- `GET https://verifypulse-seven.vercel.app/v1/x402/dns-audit?domain=example.com` ($0.01 USDC)
- `GET https://verifypulse-seven.vercel.app/v1/x402/compliance-dmarc?domain=example.com` ($0.01 USDC)
- `GET https://verifypulse-seven.vercel.app/v1/x402/agent-provision` ($3.00 USDC for 3,000 non-expiring credits)

---

## 🚀 Quick Start (Python Client)

```python
import urllib.request
import json

def verify_email(email: str, api_key: str = None) -> dict:
    url = f"https://verifypulse-seven.vercel.app/v1/verify"
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["X-API-Key"] = api_key
    
    req = urllib.request.Request(
        url,
        data=json.dumps({"email": email, "check_smtp": False}).encode(),
        headers=headers
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

# Test verification
result = verify_email("founder@stripe.com")
print(result)
```

---

## 📜 Links & Documentation
- **Live Platform**: [https://verifypulse-seven.vercel.app](https://verifypulse-seven.vercel.app)
- **OpenAPI Schema**: [https://verifypulse-seven.vercel.app/openapi.json](https://verifypulse-seven.vercel.app/openapi.json)
- **Well-Known x402**: [https://verifypulse-seven.vercel.app/.well-known/x402](https://verifypulse-seven.vercel.app/.well-known/x402)
- **Maintainer**: [MohDev212](https://github.com/MohDev212)
